# ⚙️ Chương 2: Giải Phẫu File Cấu Hình local.conf & bblayers.conf

> **Tài liệu tham khảo chính thức**:
> - [Yocto Project Reference Manual: Local Configuration](https://docs.yoctoproject.org/ref-manual/variables.html)
> - [BitBake User Manual: Syntax and Operators](https://docs.yoctoproject.org/bitbake/bitbake-user-manual/bitbake-user-manual-metadata.html)

---

## 1. THƯ MỤC CẤU HÌNH `build/conf/` ĐƯỢC TẠO RA KHI NÀO?

Khi bạn thiết lập môi trường bằng lệnh:
```bash
source oe-init-build-env [build-directory]
```
Một thư mục làm việc (mặc định là `build/`) sẽ được khởi tạo. Bên trong thư mục này chứa thư mục con `conf/` với 2 tệp tin cấu hình sống còn:
- **`build/conf/local.conf`**: Cấu hình môi trường build cục bộ của nhà phát triển (chọn phần cứng, chọn định dạng gói, tối ưu CPU, cấu hình cache).
- **`build/conf/bblayers.conf`**: Khai báo danh sách các Layer (`meta-*`) mà BitBake sẽ phân tích cú pháp.

---

## 2. GIẢI PHẪU CHI TIẾT FILE `build/conf/local.conf`

Dưới đây là từng chỉ thị quan trọng nhất trong `local.conf` cùng ý nghĩa kỹ thuật:

### 2.1. Chọn phần cứng mục tiêu (`MACHINE`)
```ini
MACHINE ??= "qemuarm"
```
- **Ý nghĩa**: Xác định kiến trúc và bo mạch mà bạn muốn build hệ điều hành.
- **Giá trị phổ biến**:
  - `qemux86-64`: Máy ảo giả lập x86_64 PC (chạy rất nhanh trên máy tính phát triển).
  - `qemuarm`: Máy ảo giả lập ARM Cortex-A15 32-bit.
  - `beaglebone-yocto`: Bo mạch thật BeagleBone Black (SoC TI AM335x).
  - `raspberrypi4-64`: Bo mạch Raspberry Pi 4 (64-bit ARMv8).
- **Cú pháp `??=`**: Đây là toán tử gán mặc định yếu (Weak default assignment). Nếu biến `MACHINE` chưa được định nghĩa ở biến môi trường shell, nó sẽ nhận giá trị này.

---

### 2.2. Chọn chính sách phân phối (`DISTRO`)
```ini
DISTRO ?= "poky"
```
- **Ý nghĩa**: Định nghĩa bộ quy tắc phân phối Linux (chọn Init System, thư viện C, toolchain).
- **Các tùy chọn có sẵn**:
  - `poky`: Bản phân phối tiêu chuẩn (dùng `glibc` và `SysVinit`).
  - `poky-tiny`: Bản phân phối siêu tối giản (dùng `musl` libc, bỏ gần như toàn bộ tính năng không cần thiết để đạt rootfs siêu nhỏ < 5MB).
  - `poky-systemd`: Bản phân phối cấu hình sẵn hệ thống khởi động hiện đại `systemd`.

---

### 2.3. Định dạng đóng gói phần mềm (`PACKAGE_CLASSES`)
```ini
PACKAGE_CLASSES ?= "package_ipk"
```
- **Ý nghĩa**: Xác định định dạng gói cài đặt phần mềm trong rootfs:
  - `package_ipk`: Định dạng `.ipk` (sử dụng trình quản lý `opkg`). **Đây là lựa chọn tốt nhất cho các hệ thống nhúng hạn chế tài nguyên** vì `opkg` cực kỳ nhẹ và tiêu tốn rất ít RAM/Flash.
  - `package_deb`: Định dạng `.deb` (sử dụng trình quản lý `dpkg`/`apt` quen thuộc như Debian/Ubuntu).
  - `package_rpm`: Định dạng `.rpm` (sử dụng `dnf` hoặc `rpm`, tiêu chuẩn mặc định cũ của Poky).

---

### 2.4. Tính năng hình ảnh bổ sung (`EXTRA_IMAGE_FEATURES`)
```ini
EXTRA_IMAGE_FEATURES ?= "debug-tweaks tools-debug ssh-server-openssh"
```
- **Ý nghĩa**: Kích hoạt nhanh các tính năng hệ thống mà không cần sửa recipe của image:
  - `debug-tweaks`: **Vô cùng quan trọng trong giai đoạn phát triển**. Cho phép đăng nhập người dùng `root` mà không cần nhập mật khẩu, tự động tắt các rào cản bảo mật khi debug.
  - `tools-debug`: Tự động cài đặt các công cụ gỡ lỗi hệ thống (`gdb`, `gdbserver`, `strace`).
  - `ssh-server-openssh` hoặc `ssh-server-dropbear`: Tự động bật dịch vụ SSH daemon để bạn có thể SSH từ máy tính vào board nhúng qua mạng.
  - `package-management`: Cài đặt các công cụ quản lý gói trên board (`opkg` hoặc `apt`), cho phép bạn cài thêm các gói phần mềm mới ngay trên bo mạch lúc runtime mà không cần build lại toàn bộ image.

---

### 2.5. Tối ưu hóa hiệu năng CPU khi Build
```ini
BB_NUMBER_THREADS = "16"
PARALLEL_MAKE = "-j 16"
```
- `BB_NUMBER_THREADS`: Số lượng tác vụ BitBake (Tasks) có thể chạy đồng thời cùng lúc. Quy tắc kinh nghiệm: Đặt bằng số luồng CPU (Thread count) của máy Host.
- `PARALLEL_MAKE`: Số luồng truyền vào lệnh `make -j` khi biên dịch mã nguồn C/C++ của từng gói riêng lẻ.

---

### 2.6. Chia sẻ thư mục Cache để tăng tốc độ Build 80% (`DL_DIR` & `SSTATE_DIR`)
Theo mặc định, mỗi khi bạn tạo một thư mục build mới, BitBake sẽ tải lại mã nguồn từ internet và biên dịch lại từ đầu. Để tái sử dụng tài nguyên giữa nhiều dự án, hãy cấu hình đường dẫn tuyệt đối ra ngoài thư mục build:

```ini
# Thư mục lưu trữ toàn bộ file nén (tarball) tải từ internet về
DL_DIR ?= "/home/thinh/yocto-cache/downloads"

# Thư mục Shared State Cache (chứa kết quả build trung gian tái sử dụng)
SSTATE_DIR ?= "/home/thinh/yocto-cache/sstate-cache"
```
> [!TIP]
> Việc cấu hình chung `DL_DIR` và `SSTATE_DIR` giúp bạn:
> 1. Không bao giờ phải tải lại GCC, Linux Kernel, Glibc khi tạo build mới.
> 2. Tốc độ build lại (Rebuild) giảm từ **3-4 tiếng** xuống chỉ còn **vài phút** nhờ cơ chế SState Cache Hit!

---

### 2.7. Cú pháp gán biến hiện đại (Từ Yocto Kirkstone & Scarthgap)
Kể từ Yocto 3.4 trở đi (bao gồm bản LTS **Scarthgap 5.0** và **Kirkstone 4.0**), cú pháp override đã chính thức chuyển từ dấu gạch dưới `_` sang **dấu hai chấm `:`**:

| Cú pháp cũ (Trước Yocto 3.4) | Cú pháp MỚI (Kirkstone, Scarthgap, Wrynose) | Mục đích |
| :--- | :--- | :--- |
| `IMAGE_INSTALL_append = " pkg"` | `IMAGE_INSTALL:append = " pkg"` | Nối thêm gói vào danh sách cài đặt |
| `SRC_URI_append = " file://x"` | `SRC_URI:append = " file://x"` | Bổ sung file nguồn |
| `do_install_append() { ... }` | `do_install:append() { ... }` | Mở rộng tác vụ `do_install` |
| `PACKAGE_ARCH_machine = "..."` | `PACKAGE_ARCH:machine = "..."` | Gán biến theo Machine cụ thể |

> [!WARNING]
> Khi sử dụng `:append`, **luôn luôn phải có một dấu khoảng trắng** ở đầu chuỗi:
> ```ini
> # ĐÚNG: Có khoảng trắng trước tên gói
> IMAGE_INSTALL:append = " nginx htop"
>
> # SAI: Thiếu khoảng trắng sẽ làm dính tên gói vào gói trước đó thành "core-image-minimalnginx"
> IMAGE_INSTALL:append = "nginx"
> ```

---

## 3. GIẢI PHẪU FILE `build/conf/bblayers.conf`

File `bblayers.conf` cho BitBake biết cần tìm kiếm Recipes ở những thư mục nào:

```ini
# POKY_BBLAYERS_CONF_VERSION is increased each time build/conf/bblayers.conf
# changes incompatibly
POKY_BBLAYERS_CONF_VERSION = "2"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  /home/thinh/poky/meta \
  /home/thinh/poky/meta-poky \
  /home/thinh/poky/meta-yocto-bsp \
  /home/thinh/poky/meta-openembedded/meta-oe \
  /home/thinh/poky/meta-openembedded/meta-python \
  /home/thinh/poky/meta-openembedded/meta-networking \
  /home/thinh/poky/meta-ti/meta-ti-bsp \
  /home/thinh/my-project/meta-custom \
  "
```

### Cách thêm Layer chuẩn mực:
Thay vì mở file `bblayers.conf` ra chỉnh sửa thủ công bằng tay (dễ gõ nhầm đường dẫn), hãy sử dụng lệnh chuẩn của BitBake:

```bash
# Thêm layer tự động:
bitbake-layers add-layer /đường_dẫn_tới/meta-layer

# Xem danh sách các layer đang hoạt động và mức ưu tiên (priority):
bitbake-layers show-layers
```
