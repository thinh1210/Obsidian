# 🚀 Chương 5: Hướng Dẫn Thực Hành Từng Bước (Build Image & Chạy Mô Phỏng QEMU)

> **Mục tiêu thực hành**:
> 1. Thiết lập máy tính Host đầy đủ các gói phụ thuộc chuẩn của Yocto Project.
> 2. Clone mã nguồn Poky phiên bản LTS ổn định (**Scarthgap 5.0**).
> 3. Khởi tạo môi trường, cấu hình `local.conf` và build thành công `core-image-minimal`.
> 4. Chạy mô phỏng hệ điều hành vừa build trên máy ảo **QEMU ARM** trực tiếp trên terminal.
> 5. Chuyển đổi cấu hình để xuất xưởng file Image nạp bo mạch phần cứng thật (**BeagleBone Black**).

---

## 1. YÊU CẦU PHẦN CỨNG MÁY HOST & CÀI ĐẶT GÓI PHỤ THUỘC

### 1.1. Yêu cầu phần cứng khuyến nghị
- **Hệ điều hành Host**: Ubuntu 22.04 LTS hoặc 24.04 LTS (x86_64).
- **Dung lượng ổ cứng trống**: Tối thiểu **60 GB - 100 GB** (SSD để có tốc độ build tối ưu).
- **Bộ nhớ RAM**: Tối thiểu **8 GB** (khuyến nghị 16 GB hoặc bật thêm Swap 8-16 GB).
- **CPU**: Càng nhiều nhân càng tốt (4 cores / 8 threads trở lên).

### 1.2. Cài đặt các gói phần mềm bắt buộc trên Ubuntu
Chạy lệnh sau trên terminal của máy tính Host:

```bash
sudo apt update
sudo apt install -y \
    gawk wget git diffstat unzip texinfo gcc build-essential \
    chrpath socat cpio python3 python3-pip python3-pexpect \
    xz-utils debianutils iputils-ping python3-git python3-jinja2 \
    libegl1 libsdl1.2-dev zstd lz4 file locales
```
*(Lưu ý: Trên các bản Ubuntu mới từ 24.04 / 26.04 trở đi, `liblz4-tool` được đổi thành `lz4`, và `libegl1-mesa` được thay bằng `libegl1`).*

Thiết lập chuẩn ký tự Locale UTF-8 (Yocto bắt buộc):
```bash
sudo locale-gen en_US.UTF-8
export LANG=en_US.UTF-8
```

---

## 2. TẢI MÃ NGUỒN POKY (NHÁNH LTS SCARTHGAP)

Tạo thư mục làm việc và clone mã nguồn Poky từ Git repository chính thức:

```bash
mkdir -p ~/yocto-lab
cd ~/yocto-lab

# Clone nhánh Long Term Support (LTS) Scarthgap (hỗ trợ tới năm 2028)
git clone -b scarthgap git://git.yoctoproject.org/poky
cd poky
```

---

## 3. KHỞI TẠO MÔI TRƯỜNG BUILD (BUILD ENVIRONMENT INITIALIZATION)

Để bắt đầu làm việc, bạn chạy lệnh `source`:

```bash
source oe-init-build-env build-qemuarm
```

### Script `oe-init-build-env` thực hiện những gì?
1. Đưa đường dẫn các công cụ của BitBake (`poky/bitbake/bin`) vào biến môi trường `$PATH` của shell.
2. Thiết lập biến `$BUILDDIR` trỏ vào thư mục `~/yocto-lab/poky/build-qemuarm`.
3. Tự động sinh ra 2 file cấu hình mẫu `conf/local.conf` và `conf/bblayers.conf` nếu thư mục này chưa có.
4. Chuyển dấu nhắc terminal vào thẳng thư mục `build-qemuarm/`.

---

## 4. CẤU HÌNH `conf/local.conf` CHO MÁY ẢO QEMU ARM

Mở file cấu hình bằng trình soạn thảo:
```bash
nano conf/local.conf
```

Chỉnh sửa hoặc xác nhận các thông số sau:

```ini
# 1. Chọn máy ảo mô phỏng ARM
MACHINE ??= "qemuarm"

# 2. Định dạng gói cài đặt tối ưu cho nhúng
PACKAGE_CLASSES ?= "package_ipk"

# 3. Kích hoạt đăng nhập root không mật khẩu và công cụ gỡ lỗi
EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-debug"

# 4. Tối ưu số luồng CPU (Giả sử máy bạn có 8 cores)
BB_NUMBER_THREADS = "8"
PARALLEL_MAKE = "-j 8"

# 5. Cấu hình thư mục cache tập trung (Tùy chọn nhưng rất khuyến khích)
DL_DIR ?= "${TOPDIR}/../downloads"
SSTATE_DIR ?= "${TOPDIR}/../sstate-cache"
```

Lưu file và thoát (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

## 5. BẮT ĐẦU QUÁ TRÌNH BIÊN DỊCH (BUILDING THE IMAGE)

Chạy lệnh BitBake để build hệ thống Linux tối giản:

```bash
bitbake core-image-minimal
```

### Quan sát màn hình tiến trình của BitBake:
```
Loading cache: 100% |#################################################################| Time: 0:00:01
Loaded 1820 entries from dependency cache.
Parsing recipes: 100% |###############################################################| Time: 0:00:25
Parsing of 925 .bb files complete (0 cached, 925 parsed). 1845 targets, 45 skipped.

NOTE: Resolving any missing task queue dependencies
NOTE: Executing Tasks
Currently 8 running tasks (241 of 3120)  8% |#####                                    |
0: glibc-2.39-r0 do_compile (pid 14205)
1: linux-yocto-6.6.21-r0 do_fetch (pid 14208)
...
```
- Lần build đầu tiên sẽ mất khoảng **25 - 45 phút** (tùy thuộc vào tốc độ mạng và CPU) vì BitBake phải build toàn bộ Toolchain, Glibc, Linux Kernel và RootFS.
- Khi màn hình hiện `NOTE: Tasks Summary: Attempted 3120 tasks of which 0 didn't need to be rerun and all succeeded.` $\rightarrow$ **Build thành công 100%!**

---

## 6. CHẠY MÔ PHỎNG HỆ ĐIỀU HÀNH BẰNG QEMU

Ngay sau khi build xong, bạn không cần có phần cứng thật mà có thể chạy thử nghiệm trực tiếp ngay trên terminal thông qua công cụ tích hợp **`runqemu`**:

```bash
runqemu qemuarm nographic
```
*(Tham số `nographic` chỉ định xuất toàn bộ giao diện màn hình ảo ra thẳng terminal hiện tại).*

### Màn hình khởi động thực tế:
```
Starting QEMU: qemu-system-arm -kernel ~/yocto-lab/poky/build-qemuarm/tmp/deploy/images/qemuarm/zImage ...

[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 6.6.21-yocto-standard ...
[    1.450212] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
[    2.102341] EXT4-fs (vda): mounted filesystem with ordered data mode.
[    2.450000] Starting syslogd/klogd: done

Poky (Yocto Project Reference Distro) 5.0 qemuarm /dev/ttyAMA0

qemuarm login: root
root@qemuarm:~# 
```

Bạn gõ lệnh đăng nhập là **`root`** (không cần nhập mật khẩu vì đã bật `debug-tweaks`).

### Khám phá hệ thống nhúng siêu nhỏ:
```bash
# Kiểm tra phiên bản nhân
uname -a

# Kiểm tra dung lượng RootFS (chỉ tiêu tốn khoảng 8MB - 12MB Flash!)
df -h

# Kiểm tra mức tiêu thụ RAM (chỉ chiếm khoảng 15MB - 20MB RAM!)
free -m
```

### Cách thoát khỏi QEMU:
Nhấn tổ hợp phím: **`Ctrl + A`**, sau đó thả tay ra và bấm phím **`X`**.

---

## 7. NÂNG CẤP BUILD CHO PHẦN CỨNG THỰC TẾ (BEAGLEBONE BLACK)

Nếu bạn muốn tạo một bản Linux để nạp trực tiếp vào thẻ nhớ MicroSD cho bo mạch thật **BeagleBone Black**:

1. Mở lại file `conf/local.conf`:
   ```ini
   # Đổi MACHINE thành bo mạch BeagleBone
   MACHINE = "beaglebone-yocto"
   ```
2. Thực thi lệnh build:
   ```bash
   bitbake core-image-minimal
   ```
3. Sau khi build xong, truy cập thư mục kết quả xuất xưởng:
   ```bash
   cd tmp/deploy/images/beaglebone-yocto/
   ls -lh *.wic.xz *.wic
   ```
   Bạn sẽ thấy file image nhị phân có tên: `core-image-minimal-beaglebone-yocto.rootfs.wic.xz` (hoặc `.wic`). Đây là file image đĩa đã được Yocto tự động phân vùng sẵn thành 2 partition (Partition 1 FAT chứa `MLO` + `u-boot.img`; Partition 2 ext4 chứa Linux Kernel + DTB + RootFS).

4. Nạp thẳng vào thẻ nhớ MicroSD bằng `bmaptool` (cực nhanh và an toàn):
   ```bash
   sudo bmaptool copy core-image-minimal-beaglebone-yocto.rootfs.wic.xz /dev/sdX
   ```
   Hoặc bằng lệnh `dd` truyền thống:
   ```bash
   unxz -k core-image-minimal-beaglebone-yocto.rootfs.wic.xz
   sudo dd if=core-image-minimal-beaglebone-yocto.rootfs.wic of=/dev/sdX bs=4M status=progress
   sync
   ```
Cắm thẻ nhớ vào BeagleBone Black, giữ nút S2 khi cắm nguồn $\rightarrow$ Hệ thống Linux Yocto tự build sẽ khởi động mượt mà!
