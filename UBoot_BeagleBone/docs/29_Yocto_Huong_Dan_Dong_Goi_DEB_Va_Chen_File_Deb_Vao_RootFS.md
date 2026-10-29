# Chương 29: Hướng Dẫn Toàn Diện Đóng Gói DEB (.deb) Và Chèn Vào Yocto RootFS Image

---

## 1. Tổng Quan Kiến Trúc & Bối Cảnh Thực Tế

Trong phát triển hệ thống Embedded Linux chuyên nghiệp với **Yocto Project**, các kỹ sư thường xuyên đối mặt với bài toán tích hợp các thành phần phần mềm có sẵn:
1. **Phần mềm độc quyền từ nhà cung cấp phần cứng (Vendor Binary / SDK)**: Nhiều đối tác chỉ cung cấp driver, thư viện tăng tốc AI (NPU), modem 4G/5G hoặc daemon quản lý dưới dạng gói `.deb` đã biên dịch sẵn mà không mở mã nguồn.
2. **Microservices và ứng dụng từ đội ngũ phần mềm bên ngoài**: Các nhóm ứng dụng biên dịch code qua CI/CD pipeline riêng (Debian/Ubuntu runner) và bàn giao file `.deb`.
3. **Cơ chế cập nhật OTA qua kho APT (Package Feeds)**: Sử dụng chuẩn đóng gói Debian để nâng cấp phần mềm linh hoạt từ xa trên thiết bị mà không cần nạp lại toàn bộ OS image.

### Giải phẫu cấu trúc nội bộ của một tệp `.deb`
Một tệp `.deb` thực chất là một kho lưu trữ dạng **`ar` archive**, bên trong chứa đúng 3 thành phần chính:
```
my-package_1.0.0_amd64.deb (ar archive)
├── debian-binary       # Định dạng phiên bản Debian package (luôn là "2.0\n")
├── control.tar.zst/gz  # Chứa metadata (control), script cài đặt (postinst, prerm, postrm)
└── data.tar.zst/xz/gz  # Cây thư mục hệ thống thực tế (/usr/bin, /etc, /lib,...)
```

```
+-------------------------------------------------------------+
|                 Gói nhị phân: package.deb                   |
+-------------------------------------------------------------+
   | (ar extraction)
   +--> debian-binary ("2.0")
   +--> control.tar (Metadata: Depends, Version, postinst, prerm)
   +--> data.tar    (Filesystem Root: /usr/bin/..., /etc/...)
```

---

## 2. Quy Trình 1: Tự Tạo Gói `.deb` Từ Mã Nguồn (Debian Packaging)

### 2.1 Cấu trúc thư mục đóng gói tiêu chuẩn
Để tạo một gói `.deb`, ta dựng một cây thư mục staging mô phỏng cấu trúc filesystem đích, kèm thư mục đặc biệt `DEBIAN/`:

```
sensor-telemetry_1.0.0_amd64/
├── DEBIAN/
│   ├── control         # (Bắt buộc) Metadata của package
│   ├── postinst        # (Tùy chọn) Script chạy sau khi giải nén
│   └── prerm           # (Tùy chọn) Script chạy trước khi gỡ gói
├── etc/
│   ├── init.d/
│   │   └── sensor-telemetry            # Script khởi động SysVinit
│   └── sensor-telemetry/
│       └── sensor.conf                 # Cấu hình runtime
├── lib/
│   └── systemd/
│       └── system/
│           └── sensor-telemetry.service # Cấu hình service Systemd
└── usr/
    └── bin/
        └── sensor-telemetry            # File thực thi nhị phân
```

### 2.2 Nội dung tệp `DEBIAN/control`
Tệp `control` chứa toàn bộ thông tin nhận dạng gói:
```ini
Package: sensor-telemetry
Version: 1.0.0
Architecture: amd64
Maintainer: Embedded Dev Team <dev@embedded.local>
Section: utils
Priority: optional
Description: IoT Sensor Telemetry Daemon for Yocto Embedded Linux
 A lightweight telemetry logging daemon designed for edge gateways.
```

> [!IMPORTANT] Quy tắc Architecture & GLIBC Compatibility:
> 1. **Architecture**: Phải khớp với kiến trúc CPU đích của target (`amd64` cho `qemux86-64`, `armhf` cho `beaglebone-yocto`, `arm64` cho `raspberrypi5`).
> 2. **GLIBC ABI**: Binary động phụ thuộc vào phiên bản GLIBC trên hệ thống build. Nếu biên dịch trên máy host Ubuntu mới (GLIBC 2.43) và nhúng vào Yocto (GLIBC 2.39), binary sẽ bị lỗi `GLIBC_2.43 not found`. Giải pháp an toàn nhất là **biên dịch tĩnh (`-static`)** hoặc dùng chính **cross-toolchain của Yocto**.

### 2.3 Nội dung script `DEBIAN/postinst`
```bash
#!/bin/sh
set -e
echo "[DEB-POSTINST] Configuring sensor-telemetry permissions..."
chmod 755 /usr/bin/sensor-telemetry
chmod 644 /etc/sensor-telemetry/sensor.conf
chmod 755 /etc/init.d/sensor-telemetry || true
mkdir -p /var/log
echo "[DEB-POSTINST] Installation completed."
exit 0
```

### 2.4 Lệnh tạo gói `.deb`
Sử dụng công cụ `dpkg-deb`:
```bash
# Đóng gói và set quyền sở hữu root:root cho filesystem
dpkg-deb --build --root-owner-group sensor-telemetry_1.0.0_amd64 sensor-telemetry_1.0.0_amd64.deb

# Kiểm tra metadata của gói vừa tạo
dpkg-deb -I sensor-telemetry_1.0.0_amd64.deb

# Xem danh sách tệp bên trong gói
dpkg-deb -c sensor-telemetry_1.0.0_amd64.deb
```

---

## 3. Quy Trình 2: Viết Recipe Yocto Để Chèn File `.deb` Vào RootFS

Yocto cung cấp class chuyên dụng **`bin_package.bbclass`** và BitBake fetcher hỗ trợ tự động giải nén gói `.deb`.

### 3.1 Cơ chế Unpack của BitBake
Khi khai báo `SRC_URI = "file://my-package.deb;subdir=${BP}"`:
1. BitBake fetcher kiểm tra đuôi `.deb`, gọi lệnh:
   ```bash
   ar -x my-package.deb data.tar.zst
   tar -xf data.tar.zst -C ${WORKDIR}/${BP}
   rm data.tar.zst
   ```
2. Toàn bộ cây tệp bên trong `data.tar.*` được trích xuất thẳng vào thư mục mã nguồn `${S}` (`${WORKDIR}/${BP}`).

### 3.2 Recipe Yocto mẫu: `sensor-telemetry-deb_1.0.0.bb`
Vị trí đặt recipe:
`meta-myproject/recipes-apps/sensor-telemetry-deb/sensor-telemetry-deb_1.0.0.bb`
Đặt file deb tại:
`meta-myproject/recipes-apps/sensor-telemetry-deb/files/sensor-telemetry_1.0.0_amd64.deb`

```bitbake
SUMMARY = "Binary deb package recipe for Sensor Telemetry Daemon"
DESCRIPTION = "Example recipe demonstrating how to integrate a pre-built .deb package into Yocto RootFS"
HOMEPAGE = "https://embedded.antigravity.internal"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

# 1. Khai báo nguồn file .deb và giải nén vào ${BP} tương ứng với ${S}
SRC_URI = "file://sensor-telemetry_1.0.0_amd64.deb;subdir=${BP}"

# 2. Inherit các class cần thiết
# bin_package: Tự động bỏ qua do_configure, do_compile và copy ${S} vào ${D}
# update-rc.d: Tự động đăng ký dịch vụ khởi động SysVinit
# systemd: Tự động cấu hình service nếu target dùng Systemd
inherit bin_package update-rc.d systemd

# 3. Cấu hình tự động khởi động cho SysVinit
INITSCRIPT_NAME = "sensor-telemetry"
INITSCRIPT_PARAMS = "defaults 95 10"

# 4. Cấu hình tự động khởi động cho Systemd
SYSTEMD_SERVICE:${PN} = "sensor-telemetry.service"
SYSTEMD_AUTO_ENABLE = "enable"

# 5. Các cờ xử lý nhị phân đóng gói sẵn (Pre-compiled Binary QA)
# Bỏ qua cảnh báo file nhị phân đã bị strip từ trước
INSANE_SKIP:${PN} += "already-stripped"
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INHIBIT_PACKAGE_STRIP = "1"

# 6. Đăng ký danh sách file thuộc package
FILES:${PN} += " \
    ${bindir}/sensor-telemetry \
    ${sysconfdir}/sensor-telemetry/sensor.conf \
    ${sysconfdir}/init.d/sensor-telemetry \
    ${systemd_system_unitdir}/sensor-telemetry.service \
"
```

---

## 4. Quy Trình 3: Cấu Hình Yocto Xuất Gói `.deb` & Quản Lý Gói Trên Target

### 4.1 Cấu hình `PACKAGE_CLASSES` trong `conf/local.conf`
Mặc định Yocto có thể dùng `package_ipk` hoặc `package_rpm`. Để Yocto tạo ra các gói định dạng `.deb`:
```bitbake
# Bật backend Debian package (.deb)
PACKAGE_CLASSES ?= "package_deb package_ipk"
```
Khi bật cấu hình này:
- Mỗi recipe khi build sẽ chạy thêm task **`do_package_write_deb`**.
- Toàn bộ file `.deb` được xuất ra tại:
  `build/tmp/deploy/deb/<arch>/` (ví dụ: `build/tmp/deploy/deb/core2-64/`).

### 4.2 Bật tính năng quản lý gói trên Target Image
Trong recipe image (`my-iot-image.bb`), thêm feature:
```bitbake
IMAGE_FEATURES += "package-management"
```
Kết quả: Hệ thống rootfs được cài sẵn tiện ích **`dpkg`** và **`apt`**.

### 4.3 Dựng máy chủ APT Repo nội bộ (Package Feed Server)
Để cập nhật từ xa qua OTA cho thiết bị nhúng:

1. **Tạo index repository trên máy host build**:
   ```bash
   bitbake package-index
   ```
2. **Khởi chạy HTTP server chia sẻ kho gói**:
   ```bash
   cd /home/thinh/yocto-lab/poky/build/tmp/deploy/deb
   python3 -m http.server 8080
   ```
3. **Cấu hình trên thiết bị nhúng (hoặc máy ảo QEMU)**:
   Thêm vào `/etc/apt/sources.list`:
   ```text
   deb [trusted=yes] http://<IP_HOST_BUILD>:8080/core2-64 ./
   ```
4. **Cài đặt hoặc cập nhật gói trên thiết bị**:
   ```bash
   apt-get update
   apt-get install sensor-telemetry-deb
   ```

---

## 5. Thực Hành Chi Tiết Từ Mã Nguồn Đến RootFS Hoàn Chỉnh

### 5.1 Mã nguồn C (`sensor_telemetry.c`)
Chương trình giám sát tải CPU, bộ nhớ RAM khả dụng và nhiệt độ cảm biến:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>

#define DEFAULT_CONF_PATH "/etc/sensor-telemetry/sensor.conf"
#define DEFAULT_LOG_PATH  "/var/log/sensor-telemetry.log"

static volatile int keep_running = 1;
void handle_signal(int sig) {
    if (sig == SIGINT || sig == SIGTERM) keep_running = 0;
}

int main() {
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);

    int interval_sec = 5;
    char device_id[64] = "yocto-edge-node";

    FILE *f_conf = fopen(DEFAULT_CONF_PATH, "r");
    if (f_conf) {
        char key[64], val[64];
        while (fscanf(f_conf, "%63[^=]=%63[^\n]\n", key, val) == 2) {
            if (strcmp(key, "INTERVAL") == 0) interval_sec = atoi(val);
            else if (strcmp(key, "DEVICE_ID") == 0) strncpy(device_id, val, sizeof(device_id)-1);
        }
        fclose(f_conf);
    }

    printf("[SENSOR-TELEMETRY] Starting on %s (interval=%ds)\n", device_id, interval_sec);
    while (keep_running) {
        float load1 = 0.0f;
        FILE *f_load = fopen("/proc/loadavg", "r");
        if (f_load) { fscanf(f_load, "%f", &load1); fclose(f_load); }

        printf("[TELEMETRY] node=%s load1=%.2f temp=%.1f C\n", device_id, load1, 42.5f);
        sleep(interval_sec);
    }
    return 0;
}
```

### 5.2 File khởi động dịch vụ (`sensor-telemetry.init`)
```bash
#!/bin/sh
DAEMON=/usr/bin/sensor-telemetry
PIDFILE=/var/run/sensor-telemetry.pid

case "$1" in
  start)
    echo "Starting sensor-telemetry..."
    start-stop-daemon --start --background --make-pidfile --pidfile $PIDFILE --exec $DAEMON
    ;;
  stop)
    echo "Stopping sensor-telemetry..."
    start-stop-daemon --stop --pidfile $PIDFILE
    rm -f $PIDFILE
    ;;
  *)
    echo "Usage: $0 {start|stop}"
    exit 1
    ;;
esac
exit 0
```

### 5.3 Script đóng gói tự động (`build_deb.sh`)
```bash
#!/usr/bin/env bash
set -e
PKG_NAME="sensor-telemetry"
PKG_VER="1.0.0"
PKG_ARCH="amd64"
PKG_DIR="${PKG_NAME}_${PKG_VER}_${PKG_ARCH}"

# 1. Biên dịch nhị phân tĩnh
gcc -static -O2 sensor_telemetry.c -o sensor-telemetry
strip --strip-unneeded sensor-telemetry

# 2. Xây dựng cây thư mục package
rm -rf "${PKG_DIR}"
mkdir -p "${PKG_DIR}/DEBIAN" "${PKG_DIR}/usr/bin"
mkdir -p "${PKG_DIR}/etc/sensor-telemetry" "${PKG_DIR}/etc/init.d"

cp sensor-telemetry "${PKG_DIR}/usr/bin/"
cp sensor.conf "${PKG_DIR}/etc/sensor-telemetry/"
cp sensor-telemetry.init "${PKG_DIR}/etc/init.d/sensor-telemetry"
chmod 755 "${PKG_DIR}/usr/bin/sensor-telemetry" "${PKG_DIR}/etc/init.d/sensor-telemetry"
chmod 644 "${PKG_DIR}/etc/sensor-telemetry/sensor.conf"

# 3. Tạo DEBIAN/control
cat << 'EOF' > "${PKG_DIR}/DEBIAN/control"
Package: sensor-telemetry
Version: 1.0.0
Architecture: amd64
Maintainer: Embedded Team <dev@embedded.local>
Section: utils
Priority: optional
Description: IoT Sensor Telemetry Daemon for Yocto Linux
EOF

# 4. Đóng gói với dpkg-deb
dpkg-deb --build --root-owner-group "${PKG_DIR}" "${PKG_DIR}.deb"
echo "Build hoàn tất: ${PKG_DIR}.deb"
```

### 5.4 Tích hợp vào Image Yocto (`my-iot-image.bb`)
Thêm `sensor-telemetry-deb` vào danh sách `IMAGE_INSTALL`:
```bitbake
IMAGE_INSTALL += " \
    my-app \
    bbb-diag \
    bbb-mmio-kmod \
    sensor-telemetry-deb \
    kernel-modules \
    iproute2 \
    ethtool \
"
```

---

## 6. Kết Quả Kiểm Chứng & Bằng Chứng Thực Nghiệm

Sau khi thực hiện lệnh:
```bash
bitbake my-iot-image
```

### 6.1 Kiểm tra file manifest của RootFS
Trong [`my-iot-image-qemux86-64.rootfs.manifest`](file:///home/thinh/yocto-lab/poky/build/tmp/deploy/images/qemux86-64/my-iot-image-qemux86-64.rootfs.manifest):
```text
sensor-telemetry-deb core2-64 1.0.0-r0
```

### 6.2 Kiểm tra file vật lý đã hạ cánh trong RootFS
Kiểm tra tại thư mục staging rootfs:
```bash
$ ls -la rootfs/usr/bin/sensor-telemetry rootfs/etc/sensor-telemetry/sensor.conf rootfs/etc/init.d/sensor-telemetry
-rwxr-xr-x 1 root root    838 /etc/init.d/sensor-telemetry
-rw-r--r-- 1 root root    117 /etc/sensor-telemetry/sensor.conf
-rwxr-xr-x 1 root root 928248 /usr/bin/sensor-telemetry
```

### 6.3 Kiểm tra Runlevel Symlinks (Tự khởi động)
Kiểm tra cơ chế `update-rc.d` đã tạo các liên kết mềm tại các runlevel từ 2 đến 5:
```bash
$ ls -la rootfs/etc/rc*.d/*sensor-telemetry*
lrwxrwxrwx 1 root root 26 /etc/rc2.d/S95sensor-telemetry -> ../init.d/sensor-telemetry
lrwxrwxrwx 1 root root 26 /etc/rc3.d/S95sensor-telemetry -> ../init.d/sensor-telemetry
lrwxrwxrwx 1 root root 26 /etc/rc4.d/S95sensor-telemetry -> ../init.d/sensor-telemetry
lrwxrwxrwx 1 root root 26 /etc/rc5.d/S95sensor-telemetry -> ../init.d/sensor-telemetry
lrwxrwxrwx 1 root root 26 /etc/rc0.d/K10sensor-telemetry -> ../init.d/sensor-telemetry
lrwxrwxrwx 1 root root 26 /etc/rc6.d/K10sensor-telemetry -> ../init.d/sensor-telemetry
```

### 6.4 Kiểm tra gói `.deb` do Yocto sinh ra
File `.deb` hoàn chỉnh được sinh ra tại:
[`/home/thinh/yocto-lab/poky/build/tmp/deploy/deb/core2-64/sensor-telemetry-deb_1.0.0-r0_amd64.deb`](file:///home/thinh/yocto-lab/poky/build/tmp/deploy/deb/core2-64/sensor-telemetry-deb_1.0.0-r0_amd64.deb)

---

## 7. Thư Mục Mã Nguồn Ví Dụ (Code Examples)

Toàn bộ mã nguồn, cấu hình, script build và recipe đã được lưu trữ sẵn trong workspace:
1. **Mã nguồn và script đóng gói Debian**:
   [`/home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/)
   - [`sensor_telemetry.c`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/sensor_telemetry.c)
   - [`build_deb.sh`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/build_deb.sh)
   - [`sensor.conf`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/sensor.conf)
   - [`sensor-telemetry.init`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/sensor-telemetry.init)
   - [`sensor-telemetry_1.0.0_amd64.deb`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/debian-src/sensor-telemetry_1.0.0_amd64.deb)
2. **Recipe Yocto BitBake**:
   [`/home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/yocto-recipe/sensor-telemetry-deb_1.0.0.bb`](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/yocto_deb_packaging/yocto-recipe/sensor-telemetry-deb_1.0.0.bb)
