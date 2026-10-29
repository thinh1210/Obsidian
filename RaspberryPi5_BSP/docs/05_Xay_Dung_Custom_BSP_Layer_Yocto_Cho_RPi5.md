# 📦 Chương 5: Xây Dựng Custom BSP Layer Yocto Cho Raspberry Pi 5

---

## 🏗️ 1. TẠI SAO PHẢI XÂY DỰNG CUSTOM BSP LAYER TRÊN YOCTO?

Khi chuyển giao một sản phẩm nhúng ra thị trường thương mại, bạn **không bao giờ** sử dụng hệ điều hành Raspberry Pi OS (Debian) thông thường bởi các nhược điểm:
- Dung lượng quá nặng (vài GB), chứa nhiều gói thừa thãi không cần thiết.
- Tốc độ khởi động chậm (15–30 giây).
- Không có cơ chế cập nhật hệ điều hành atomic an toàn (dễ bị brick máy nếu mất điện đột ngột).
- Không kiểm soát được phiên bản của từng gói phần mềm và lỗ hổng bảo mật (CVEs).

**Yocto Project (Poky Scarthgap 5.0 LTS)** là tiêu chuẩn công nghiệp số 1 thế giới giúp bạn:
1. Xây dựng một bản phân phối Linux siêu nhẹ (chỉ từ 30MB đến 150MB), khởi động trong **dưới 3 giây**.
2. **Tổng hợp tự động toàn bộ driver linh kiện phần cứng, Device Tree Overlays, và tệp cấu hình bootloader** thành một file ảnh đĩa duy nhất (`.wic`) chỉ với một câu lệnh `bitbake`.

---

## 📂 2. CẤU TRÚC THƯ MỤC CHUẨN CỦA LAYER `meta-custom-rpi5`

Dưới đây là cấu trúc thiết kế của Layer BSP tùy biến **`meta-custom-rpi5`** (đã được tạo sẵn tại thư mục [`/home/thinh/rpi5_bsp_workspace/meta-custom-rpi5/`](file:///home/thinh/rpi5_bsp_workspace/meta-custom-rpi5)):

```text
meta-custom-rpi5/
├── conf/
│   ├── layer.conf                             # Khai báo mức ưu tiên và phụ thuộc của Layer
│   └── machine/
│       └── custom-rpi5.conf                   # Định nghĩa Bo Mạch Máy Tính Tùy Biến
├── recipes-bsp/
│   └── bootfiles/
│       └── rpi-config_%.bbappend              # Tự động tùy biến config.txt lúc sinh image
├── recipes-kernel/
│   └── linux/
│       ├── files/
│       │   ├── custom-hardware.cfg            # Kernel config fragment bật CAN, IIO, DRM
│       │   └── custom-components-rpi5.dts     # Device Tree Overlay nhắm vào RP1
│       └── linux-raspberrypi_%.bbappend       # Nhúng overlay và fragment vào kernel build
├── recipes-drivers/
│   ├── custom-sensor-i2c/
│   │   ├── files/
│   │   │   ├── custom_sensor.c                # Mã nguồn C Driver Cảm Biến I2C
│   │   │   └── Makefile                       # Makefile Kbuild
│   │   └── custom-sensor-i2c_1.0.bb           # Recipe biên dịch out-of-tree module .ko
│   └── custom-gpio-actuator/
│       ├── files/
│       │   ├── custom_actuator.c              # Mã nguồn C Driver Relay/Actuator
│       │   └── Makefile                       # Makefile Kbuild
│       └── custom-gpio-actuator_1.0.bb        # Recipe biên dịch module actuator
└── recipes-core/
    └── images/
        └── custom-rpi5-industrial-image.bb    # Recipe sinh Image WIC đóng gói toàn diện
```

---

## 📝 3. GIẢI PHÃU TỪNG TỆP TIN CỐT LÕI TRONG BSP LAYER

### 3.1 Tệp khai báo Layer: `conf/layer.conf`
Tệp tin này đăng ký layer với BitBake và xác định các layer phụ thuộc (`meta-raspberrypi` và `core`):

```bitbake
# Chúng ta có thư mục conf và classes, thêm vào BBPATH
BBPATH .= ":${LAYERDIR}"

# Chúng ta có các thư mục recipes, thêm vào BBFILES
BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
            ${LAYERDIR}/recipes-*/*/*.bbappend"

BBFILE_COLLECTIONS += "meta-custom-rpi5"
BBFILE_PATTERN_meta-custom-rpi5 = "^${LAYERDIR}/"
BBFILE_PRIORITY_meta-custom-rpi5 = "10"

LAYERDEPENDS_meta-custom-rpi5 = "core raspberrypi"
LAYERSERIES_COMPAT_meta-custom-rpi5 = "scarthgap"
```

---

### 3.2 Tệp định nghĩa bo mạch: `conf/machine/custom-rpi5.conf`
Tệp cấu hình máy kế thừa toàn bộ nền tảng BCM2712 từ `meta-raspberrypi`, đồng thời bổ sung các định nghĩa riêng của bo mạch phần cứng công nghiệp:

```bitbake
# Kế thừa cấu hình tiêu chuẩn của raspberrypi5 từ meta-raspberrypi
require conf/machine/raspberrypi5.conf

# Đặt tên định danh cho bo mạch công nghiệp tùy biến
MACHINENAME = "Custom Raspberry Pi 5 Industrial Gateway"

# Bật sẵn các bus ngoại vi trong firmware config.txt
ENABLE_I2C = "1"
ENABLE_SPI_BUS = "1"
ENABLE_UART = "1"

# Bổ sung các Device Tree Overlays tùy biến vào danh sách biên dịch và nạp boot
RPI_KERNEL_DEVICETREE_OVERLAYS:append = " \
    overlays/custom-components-rpi5.dtbo \
"

# Cấu hình tự động nạp các Kernel Modules lúc khởi động
KERNEL_MODULE_AUTOLOAD += " \
    custom_sensor \
    custom_actuator \
    mcp251x \
"
```

---

### 3.3 Tùy biến Kernel: `recipes-kernel/linux/linux-raspberrypi_%.bbappend`
Nhiệm vụ: Tự động đưa cấu hình kernel fragment (`custom-hardware.cfg`) và biên dịch Device Tree Overlay mới nhúng vào phân vùng boot:

```bitbake
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += " \
    file://custom-hardware.cfg \
    file://custom-components-rpi5.dts \
"

# Copy file .dts vào thư mục nguồn của Kernel trước khi biên dịch Device Tree
do_configure:prepend() {
    cp ${WORKDIR}/custom-components-rpi5.dts ${S}/arch/arm64/boot/dts/overlays/
}
```

Nội dung tệp cấu hình Kernel fragment **`custom-hardware.cfg`**:
```kconfig
# Kích hoạt SocketCAN và Driver MCP2515
CONFIG_CAN=y
CONFIG_CAN_RAW=y
CONFIG_CAN_DEV=y
CONFIG_CAN_MCP251X=m

# Kích hoạt Industrial I/O (IIO) cho các cảm biến nhiệt/áp
CONFIG_IIO=y
CONFIG_IIO_BUFFER=y
CONFIG_BMP280=m
CONFIG_BMP280_I2C=m

# Kích hoạt DRM/KMS cho màn hình hiển thị SPI
CONFIG_DRM=y
CONFIG_DRM_KMS_HELPER=y
CONFIG_TINYDRM_ST7789V=m

# Kích hoạt PCIe Gen 3 và NVMe Host
CONFIG_BLK_DEV_NVME=y
CONFIG_PCIE_BRCMSTB=y
```

---

### 3.4 Tự động thêm chỉ thị vào `config.txt`: `recipes-bsp/bootfiles/rpi-config_%.bbappend`
Giúp tệp `config.txt` trên phân vùng FAT tự động có các cờ kích hoạt PCIe Gen 3 và các overlays mà không cần người dùng tự gõ bằng tay:

```bitbake
do_deploy:append() {
    CONFIG="${DEPLOYDIR}/${BOOTFILES_DIR_NAME}/config.txt"

    echo "" >> $CONFIG
    echo "# === Cấu hình tự động bởi meta-custom-rpi5 ===" >> $CONFIG
    echo "dtparam=pciex1=on" >> $CONFIG
    echo "dtparam=pciex1_gen=3" >> $CONFIG
    echo "dtoverlay=custom-components-rpi5" >> $CONFIG
    echo "dtparam=cooling_fan=on" >> $CONFIG
}
```

---

### 3.5 Recipe đóng gói Driver Out-of-tree: `custom-sensor-i2c_1.0.bb`
Sử dụng class **`module`** của Yocto, BitBake sẽ tự động dùng đúng Cross-Compiler ARM64 để biên dịch file mã nguồn C thành tệp nhị phân `.ko`:

```bitbake
SUMMARY = "Custom I2C Sensor Driver for Raspberry Pi 5"
LICENSE = "GPL-2.0-only"
LIC_FILES_CHKSUM = "file://COPYING;md5=b234ee4d69f5fce44864b12a9c32a738"

inherit module

SRC_URI = " \
    file://Makefile \
    file://custom_sensor.c \
    file://COPYING \
"

S = "${WORKDIR}"

RPROVIDES:${PN} += "kernel-module-custom-sensor"
```

---

### 3.6 Recipe sinh Image hoàn chỉnh: `recipes-core/images/custom-rpi5-industrial-image.bb`
Gom toàn bộ các thành phần: Kernel, Driver linh kiện, công cụ chẩn đoán phần cứng, thư viện lập trình vào một tệp ảnh đĩa `.wic`:

```bitbake
SUMMARY = "Bản Phân Phối Linux Nhúng Hoàn Chỉnh Cho Raspberry Pi 5"
DESCRIPTION = "Tích hợp toàn bộ Driver linh kiện, SocketCAN, IIO, GPIO và công cụ chẩn đoán"

IMAGE_INSTALL = " \
    packagegroup-core-boot \
    \
    /* 1. Các Driver Linh Kiện Tự Viết & In-Tree */ \
    custom-sensor-i2c \
    custom-gpio-actuator \
    kernel-module-mcp251x \
    kernel-module-bmp280-i2c \
    kernel-module-tinydrm-st7789v \
    \
    /* 2. Thư viện & Công cụ chẩn đoán phần cứng */ \
    libgpiod \
    libgpiod-tools \
    i2c-tools \
    can-utils \
    spitools \
    pciutils \
    usbutils \
    \
    /* 3. Tiện ích quản trị hệ thống */ \
    openssh \
    openssh-sftp-server \
    htop \
    curl \
"

inherit core-image

# Định dạng tệp ảnh đĩa đầu ra (wic.bz2 nạp trực tiếp vào thẻ nhớ hoặc NVMe)
IMAGE_FSTYPES = "wic.bz2 wic.bmap"

# Cung cấp thêm 500MB vùng nhớ trống trên rootfs cho người dùng cài ứng dụng
IMAGE_ROOTFS_EXTRA_SPACE = "512000"
```

---

## 🚀 4. QUY TRÌNH THỰC THI BIÊN DỊCH TRÊN TERMINAL (STEP-BY-STEP)

Dưới đây là các câu lệnh chuẩn xác để khởi chạy tiến trình build trên máy tính phát triển Ubuntu:

```bash
# Bước 1: Tạo thư mục làm việc và clone các layer cần thiết
mkdir -p ~/rpi5-yocto-build && cd ~/rpi5-yocto-build

git clone -b scarthgap git://git.yoctoproject.org/poky
git clone -b scarthgap https://github.com/openembedded/meta-openembedded.git
git clone -b scarthgap https://github.com/agherzan/meta-raspberrypi.git

# Liên kết layer custom của chúng ta vào workspace
ln -s /home/thinh/rpi5_bsp_workspace/meta-custom-rpi5 ./meta-custom-rpi5

# Bước 2: Khởi tạo môi trường BitBake
source poky/oe-init-build-env build

# Bước 3: Đăng ký các Layer vào build/conf/bblayers.conf
bitbake-layers add-layer ../meta-openembedded/meta-oe
bitbake-layers add-layer ../meta-raspberrypi
bitbake-layers add-layer ../meta-custom-rpi5

# Bước 4: Cấu hình bo mạch đích trong build/conf/local.conf
# Sửa dòng MACHINE ??= "qemux86-64" thành:
echo 'MACHINE = "custom-rpi5"' >> conf/local.conf
echo 'INIT_MANAGER = "systemd"' >> conf/local.conf

# Bước 5: Kích hoạt biên dịch toàn bộ hệ thống BSP
bitbake custom-rpi5-industrial-image
```

Sau khi quá trình biên dịch hoàn tất (thường mất 45–90 phút trong lần build đầu tiên tùy cấu hình CPU), tệp ảnh đĩa sẵn sàng xuất xưởng nằm tại:
`build/tmp/deploy/images/custom-rpi5/custom-rpi5-industrial-image-custom-rpi5.rootfs.wic.bz2`

Chỉ cần giải nén và ghi thẳng vào thẻ nhớ MicroSD:
```bash
bunzip2 -k custom-rpi5-industrial-image-custom-rpi5.rootfs.wic.bz2
sudo dd if=custom-rpi5-industrial-image-custom-rpi5.rootfs.wic of=/dev/sdX bs=4M status=progress conv=fsync
```

Cắm thẻ nhớ vào Raspberry Pi 5 và cấp nguồn $\rightarrow$ Hệ thống sẽ tự động khởi tạo 100% linh kiện phần cứng mà bạn đã cấu hình!

---
*Tiếp theo: [Chương 6: Xây Dựng BSP Với Buildroot Alternative](./06_Xay_Dung_BSP_Voi_Buildroot_Alternative.md)*
