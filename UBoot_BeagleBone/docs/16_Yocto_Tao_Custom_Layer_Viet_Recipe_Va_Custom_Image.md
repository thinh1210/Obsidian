# 🛠️ Chương 16 (Yocto 6): Tạo Custom Layer, Viết Recipe Ứng Dụng & Custom Image

> **Mục tiêu thực hành nâng cao**:
> 1. Tự tạo một Layer mới mang tên `meta-myproject` chuẩn theo quy cách của Yocto Project.
> 2. Viết một Recipe C/C++ hoàn chỉnh (`my-app_1.0.bb`) từ mã nguồn nội bộ.
> 3. Tùy chỉnh gói có sẵn bằng kỹ thuật `.bbappend`.
> 4. Đóng gói ứng dụng vào một Custom Image riêng biệt và kiểm thử trên QEMU.

---

## 1. TẠO CUSTOM LAYER MỚI VỚI `bitbake-layers`

Để giữ cho mã nguồn của Poky và các layer bên thứ ba sạch sẽ, mọi tùy biến riêng của công ty hoặc dự án cá nhân **bắt buộc phải được đặt trong một layer độc lập**.

Đứng tại thư mục `build-qemuarm/`, chạy lệnh:

```bash
# 1. Tạo layer mới mang tên meta-myproject tại thư mục cha
bitbake-layers create-layer ../meta-myproject

# 2. Đăng ký layer mới này vào file bblayers.conf
bitbake-layers add-layer ../meta-myproject

# 3. Kiểm tra xem layer đã được kích hoạt thành công chưa:
bitbake-layers show-layers
```

### Cấu trúc thư mục được tự động sinh ra:
```
meta-myproject/
├── conf/
│   └── layer.conf            # Khai báo tên layer, mức ưu tiên (priority), tương thích phiên bản
├── COPYING.MIT
├── README
└── recipes-example/
    └── example/
        └── example_0.1.bb
```

---

## 2. VIẾT RECIPE CHO ỨNG DỤNG C CỦA BẠN (`my-app_1.0.bb`)

Chúng ta sẽ tạo một ứng dụng C đơn giản mang tên `my-app` in ra thông điệp hệ thống và nhấp nháy đèn LED.

### Bước 2.1: Tạo cấu trúc thư mục recipe
```bash
mkdir -p ../meta-myproject/recipes-apps/my-app/files
cd ../meta-myproject/recipes-apps/my-app
```

### Bước 2.2: Viết mã nguồn C (`files/main.c`)
Tạo file `files/main.c`:

```c
#include <stdio.h>
#include <unistd.h>

int main(void) {
    printf("=========================================\n");
    printf(" Xin chao! Ung dung My-App tren Yocto OS \n");
    printf(" Build boi Embedded Engineer: Thinh     \n");
    printf("=========================================\n");

    int count = 0;
    while (count < 3) {
        printf("[My-App] Tien trinh dang chay binh thuong... (lan %d)\n", ++count);
        sleep(1);
    }

    printf("[My-App] Hoan tat chuong trinh thanh cong!\n");
    return 0;
}
```

### Bước 2.3: Viết `files/Makefile`
Tạo file `files/Makefile` hỗ trợ biên dịch chéo:

```makefile
CC ?= gcc
CFLAGS ?= -Wall -O2

all: my-app

my-app: main.o
	$(CC) $(LDFLAGS) -o my-app main.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

clean:
	rm -f my-app *.o

.PHONY: all clean
```

### Bước 2.4: Viết nội dung Recipe `my-app_1.0.bb`
Tạo file `my-app_1.0.bb`:

```python
SUMMARY = "Chuong trinh C mau danh cho he thong nhung Yocto"
DESCRIPTION = "Ung dung don gian minh hoa cach dong goi ma nguon C vao RootFS"
HOMEPAGE = "https://github.com/myuser/my-app"
SECTION = "apps"

# Giấy phép bản quyền (Dùng MIT đơn giản cho dự án nội bộ)
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

# Khai báo các file nguồn nằm trong thư mục con files/
SRC_URI = "file://main.c \
           file://Makefile"

# Thư mục chứa mã nguồn giải nén (nằm trong WORKDIR)
S = "${WORKDIR}"

# Tác vụ biên dịch (Tự động gọi Makefile bằng trình biên dịch chéo)
do_compile() {
    oe_runmake
}

# Tác vụ cài đặt file nhị phân vào thư mục giả lập D
do_install() {
    # 1. Tạo thư mục đích /usr/bin trong RootFS giả lập
    install -d ${D}${bindir}

    # 2. Copy file nhị phân my-app với quyền thực thi 0755 (rwxr-xr-x)
    install -m 0755 ${S}/my-app ${D}${bindir}/my-app
}

# Khai báo file nhị phân thuộc về gói chính ${PN}
FILES:${PN} = "${bindir}/my-app"
```

---

## 3. BIÊN DỊCH VÀ KIỂM THỬ ĐỘC LẬP RECIPE VỪA VIẾT

Quay trở lại thư mục build và chạy lệnh biên dịch riêng cho `my-app`:

```bash
cd ~/yocto-lab/poky/build-qemuarm
bitbake my-app
```

Nếu thành công không có lỗi, BitBake sẽ tải, build và tạo ra file gói `.ipk` tại:
`tmp/deploy/ipk/cortexa15t2hf-neon/my-app_1.0-r0_cortexa15t2hf-neon.ipk`.

---

## 4. TẠO CUSTOM IMAGE ĐỂ ĐÓNG GÓI ỨNG DỤNG

Để ứng dụng `my-app` tự động xuất hiện trong hệ điều hành khi bo mạch khởi động, chúng ta tạo một file image riêng:

Tạo file: `../meta-myproject/recipes-core/images/my-custom-image.bb`:

```python
# Kế thừa image tối giản core-image-minimal của Poky
require recipes-core/images/core-image-minimal.bb

SUMMARY = "Custom Image tich hop ung dung my-app"
DESCRIPTION = "He dieu hanh nhung rut gon da tich hop san my-app de kiem thu"

# Tự động nạp gói my-app vào danh sách gói cài đặt của RootFS
IMAGE_INSTALL += " \
    my-app \
"
```

---

## 5. BUILD VÀ KIỂM CHỨNG TRÊN MÁY ẢO QEMU

1. Thực hiện build image hoàn chỉnh:
   ```bash
   bitbake my-custom-image
   ```
2. Khởi động máy ảo QEMU:
   ```bash
   runqemu qemuarm nographic
   ```
3. Đăng nhập bằng tài khoản `root`.
4. Chạy trực tiếp chương trình vừa viết:
   ```bash
   root@qemuarm:~# which my-app
   /usr/bin/my-app

   root@qemuarm:~# my-app
   =========================================
    Xin chao! Ung dung My-App tren Yocto OS 
    Build boi Embedded Engineer: Thinh     
   =========================================
   [My-App] Tien trinh dang chay binh thuong... (lan 1)
   [My-App] Tien trinh dang chay binh thuong... (lan 2)
   [My-App] Tien trinh dang chay binh thuong... (lan 3)
   [My-App] Hoan tat chuong trinh thanh cong!
   ```

Ứng dụng C tùy biến của bạn đã được tích hợp thành công tuyệt đối vào hệ thống Linux Yocto xuất xưởng!

---

## 6. HƯỚNG DẪN CHI TIẾT TÙY BIẾN `my-custom-image` VÀ `my-iot-image`

Khi muốn thêm bớt phần mềm, thay đổi dịch vụ hệ thống, đặt mật khẩu hoặc can thiệp vào cấu trúc hệ điều hành xuất xưởng, bạn thao tác trực tiếp trên 2 file công thức Image sau:

### 6.1. Vị trí chính xác của 2 file trên máy tính của bạn:
- **`my-custom-image`**: `~/yocto-lab/meta-myproject/recipes-core/images/my-custom-image.bb`
- **`my-iot-image`**: `~/yocto-lab/meta-myproject/recipes-core/images/my-iot-image.bb`

---

### 6.2. Các kỹ thuật tùy biến phổ biến nhất

#### A. Thêm hoặc bớt các gói phần mềm (`IMAGE_INSTALL`)
Mở file `.bb` tương ứng và bổ sung tên gói vào biến `IMAGE_INSTALL`:

```python
IMAGE_INSTALL += " \
    my-app \
    python3 \
    python3-pip \
    htop \
    curl \
    nano \
    git \
    wpa-supplicant \
    i2c-tools \
"
```
*Lưu ý: Để tìm xem một phần mềm có tên package là gì trong Yocto, bạn có thể tra cứu trên trang [OpenEmbedded Layer Index](https://layers.openembedded.org/) hoặc dùng lệnh `bitbake-layers show-recipes <tên_gói>`.*

---

#### B. Bật / Tắt các tính năng hệ điều hành (`IMAGE_FEATURES`)
Biến `IMAGE_FEATURES` điều khiển các tính năng cốt lõi của Linux mà không cần cài đặt gói thủ công:

```python
IMAGE_FEATURES += " \
    debug-tweaks \
    ssh-server-openssh \
    package-management \
    tools-debug \
"
```
- `debug-tweaks`: Cho phép user `root` đăng nhập không cần mật khẩu.
- `ssh-server-dropbear`: Bật dịch vụ SSH siêu nhẹ (thích hợp cho thiết bị nhúng ít RAM).
- `ssh-server-openssh`: Bật dịch vụ OpenSSH đầy đủ tính năng (hỗ trợ `sftp`, `scp`, `ssh-keygen`).
- `package-management`: Cài đặt trình quản lý gói (`opkg` hoặc `apt`), cho phép gõ lệnh cài thêm phần mềm ngay trên board lúc runtime.
- `read-only-rootfs`: Khóa phân vùng rootfs thành **Read-Only (Chỉ đọc)**. Rất quan trọng cho thiết bị công nghiệp để chống hỏng bộ nhớ Flash khi rút nguồn đột ngột.
- `tools-debug`: Cài sẵn bộ công cụ gỡ lỗi mạnh mẽ (`gdb`, `gdbserver`, `strace`).

---

#### C. Tăng dung lượng bộ nhớ trống cho phân vùng RootFS (`IMAGE_ROOTFS_EXTRA_SPACE`)
Mặc định Yocto sẽ tính toán dung lượng RootFS vừa khít với các gói phần mềm đã cài. Nếu bạn muốn hệ điều hành chừa sẵn dung lượng trống cho người dùng lưu file:

```python
# Đơn vị tính bằng KiloBytes (KB).
# Ví dụ: 51200 KB = 50 MB; 102400 KB = 100 MB
IMAGE_ROOTFS_EXTRA_SPACE = "102400"
```

---

#### D. Đặt mật khẩu hoặc tạo thêm User mới (`extrausers.bbclass`)
Nếu bạn muốn hệ thống có bảo mật người dùng thay vì dùng `debug-tweaks`:

```python
# Kế thừa class quản lý tài khoản người dùng
inherit extrausers

# Đặt mật khẩu cho root và tạo thêm user mới 'thinh'
EXTRA_USERS_PARAMS = " \
    usermod -P 'matkhau123' root; \
    useradd -P 'matkhau123' -s /bin/sh thinh; \
"
```

---

#### E. Chạy lệnh tùy biến sau khi tạo RootFS (`ROOTFS_POSTPROCESS_COMMAND`)
Bạn có thể viết một hàm Shell chạy tự động ngay sau khi RootFS được giải nén xong (trước khi đóng gói thành file `.wic` hoặc `.ext4`). Dùng để đổi Hostname, tạo thư mục riêng hoặc sửa file cấu hình:

```python
# Khai báo hàm shell tùy biến
my_custom_postprocess() {
    # 1. Đổi Hostname của hệ điều hành thành 'my-iot-device'
    echo "my-iot-device" > ${IMAGE_ROOTFS}/etc/hostname

    # 2. Tạo một thư mục riêng /opt/my-data
    mkdir -p ${IMAGE_ROOTFS}/opt/my-data
    echo "He thong duoc tao boi Thinh" > ${IMAGE_ROOTFS}/opt/my-data/info.txt
}

# Đăng ký hàm vào chu trình tạo RootFS của BitBake
ROOTFS_POSTPROCESS_COMMAND += "my_custom_postprocess; "
```

---

## 7. MẸO: TÙY BIẾN NHANH TỪ `conf/local.conf` MÀ KHÔNG SỬA FILE RECIPE

Nếu bạn chỉ muốn thử nghiệm thêm nhanh một vài gói vào image mà không muốn mở file recipe ra sửa, bạn có thể thêm cú pháp Override trực tiếp vào `build/conf/local.conf`:

```ini
# Chỉ thêm gói 'htop' và 'curl' riêng cho phiên bản my-custom-image:
IMAGE_INSTALL:append:pn-my-custom-image = " htop curl"

# Hoặc thêm cho TẤT CẢ các image được build:
CORE_IMAGE_EXTRA_INSTALL += "htop curl"
```
*(Lưu ý: Luôn có dấu khoảng trắng ở đầu chuỗi khi dùng `:append`).*

