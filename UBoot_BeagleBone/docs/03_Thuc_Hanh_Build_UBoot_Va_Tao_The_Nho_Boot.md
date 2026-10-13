# 🛠️ Chương 3: Hướng Dẫn Thực Hành Biên Dịch U-Boot & Tạo Thẻ Nhớ Khởi Động

> **Mục tiêu thực hành**:
> 1. Thiết lập môi trường biên dịch chéo (Cross-compilation Toolchain) trên máy tính Linux Host.
> 2. Biên dịch mã nguồn U-Boot sinh ra các file nhị phân `MLO` và `u-boot.img`.
> 3. Phân vùng và định dạng thẻ nhớ MicroSD đúng chuẩn phần cứng AM335x.
> 4. Nạp Bootloader và giải thích các quy tắc ghi đĩa bắt buộc.

---

## 1. CHUẨN BỊ MÔI TRƯỜNG & CROSS-COMPILER TOOLCHAIN

Việc biên dịch bootloader cho kiến trúc ARM (Cortex-A8 32-bit `armhf`) cần được thực hiện trên máy tính phát triển (Linux Host x86_64).

### 1.1. Cài đặt các gói phụ thuộc trên Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y \
    build-essential \
    gcc-arm-linux-gnueabihf \
    bison \
    flex \
    libssl-dev \
    bc \
    libncurses-dev \
    device-tree-compiler \
    git \
    python3-setuptools \
    python3-dev \
    python3-pyelftools \
    swig \
    dosfstools \
    parted
```

### 1.2. Kiểm tra phiên bản Toolchain

```bash
arm-linux-gnueabihf-gcc --version
```

Kết quả mong đợi: Trình biên dịch GCC đa nền tảng cho `arm-linux-gnueabihf` sẵn sàng (phiên bản khuyến nghị từ GCC 9.x đến GCC 13.x).

---

## 2. TẢI MÃ NGUỒN VÀ BIÊN DỊCH U-BOOT

### 2.1. Clone mã nguồn từ Denx Git Repository

```bash
# Clone cây mã nguồn chính thức của Das U-Boot
git clone https://source.denx.de/u-boot/u-boot.git
cd u-boot

# Liệt kê các release tag ổn định gần nhất
git tag -l "v202*" | tail -n 10

# Checkout sang một phiên bản ổn định (ví dụ v2024.01)
git checkout v2024.01 -b bbb-build
```

### 2.2. Biên dịch U-Boot cho BeagleBone Black

Thiết lập các biến môi trường chỉ định kiến trúc đích (`ARCH=arm`) và tiền tố trình biên dịch chéo (`CROSS_COMPILE=arm-linux-gnueabihf-`):

```bash
export ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabihf-

# Bước 1: Dọn dẹp sạch sẽ các tệp sinh ra từ các lần build trước
make distclean

# Bước 2: Nạp cấu hình phần cứng mặc định cho dòng AM335x
make am335x_evm_defconfig

# (Tùy chọn) Mở giao diện ncurses để tùy chỉnh tính năng nếu cần:
# make menuconfig

# Bước 3: Biên dịch toàn bộ SPL và U-Boot Proper (dùng tất cả CPU core)
make -j$(nproc)
```

---

## 3. PHÂN TÍCH CÁC FILE OUTPUT SINH RA SAU KHI BIÊN DỊCH

Sau khi quá trình `make` hoàn tất thành công, trong thư mục nguồn sẽ xuất hiện các file quan trọng sau:

| Tên file | Vị trí thư mục | Kích thước xấp xỉ | Ý nghĩa kỹ thuật |
| :--- | :--- | :--- | :--- |
| **`MLO`** | Thư mục gốc `u-boot/` | ~70 KB - 105 KB | File SPL nhị phân đã được gắn **GP Header (8 byte)** ở đầu. Đây là file ROM Code của AM335x nạp trực tiếp vào On-Chip SRAM. |
| **`u-boot.img`** | Thư mục gốc `u-boot/` | ~600 KB - 900 KB | Bản U-Boot Proper hoàn chỉnh có gắn **u-boot header (64 byte)**, được SPL nạp vào DDR3 RAM tại `0x80800000`. |
| `u-boot-dtb.img` | Thư mục gốc `u-boot/` | ~600 KB - 900 KB | U-Boot Proper đã đóng gói kèm theo Device Tree Blob (`.dtb`). |
| `spl/u-boot-spl.bin` | `spl/` | ~70 KB - 105 KB | File SPL nhị phân thô (chưa có GP Header 8 byte). |
| `spl/u-boot-spl` | `spl/` | ~1.5 MB - 3 MB | File định dạng **ELF** của SPL có chứa đầy đủ symbol gỡ lỗi (dùng khi debug bằng JTAG/GDB). |
| `u-boot` | Thư mục gốc `u-boot/` | ~8 MB - 15 MB | File định dạng **ELF** của U-Boot Proper chứa symbol gỡ lỗi. |

### Kiểm tra GP Header trong file `MLO` bằng `hexdump`:

```bash
hexdump -C -n 16 MLO
```

Kết quả hiển thị:
```
00000000  68 96 01 00 00 04 2f 40  14 00 00 ea 14 f0 9f e5  |h...../@........|
```
- `68 96 01 00`: Kích thước file SPL (`0x00019668` = 104,040 bytes $\approx$ 101.6 KB, nhỏ hơn giới hạn 109 KB).
- `00 04 2f 40`: Địa chỉ đích nạp trong RAM (`0x402F0400`, chính là địa chỉ On-Chip SRAM).

---

## 4. QUY TRÌNH PHÂN VÙNG VÀ ĐỊNH DẠNG THẺ NHỚ MICROSD

ROM Code của AM335x có những yêu cầu phần cứng rất khắt khe đối với cấu trúc thẻ nhớ:
1. **Phải sử dụng bảng phân vùng MBR (Master Boot Record)**, **KHÔNG ĐƯỢC** dùng GPT (GUID Partition Table).
2. Phân vùng đầu tiên phải được định dạng **FAT32** (hoặc FAT16) và **phải bật cờ Boot (Active flag)**.

### 4.1. Xác định đúng tên thiết bị thẻ nhớ

Cắm thẻ nhớ MicroSD vào máy tính qua đầu đọc thẻ và chạy:
```bash
lsblk
```
> [!CAUTION]
> Xác định chính xác ký hiệu ổ đĩa của thẻ nhớ (ví dụ `/dev/sdb`, `/dev/sdc` hoặc `/dev/mmcblk0`). **Tuyệt đối không chạy lệnh trên ổ cứng hệ thống (`/dev/sda` hay `/dev/nvme0n1`) để tránh mất toàn bộ dữ liệu máy tính!**

Trong phần hướng dẫn dưới đây, chúng ta quy ước thẻ nhớ là biến môi trường `$DISK`:
```bash
export DISK=/dev/sdX
```

### 4.2. Xóa sạch bảng phân vùng cũ

```bash
# Xóa sạch 10MB đầu tiên của thẻ để loại bỏ hoàn toàn GPT hoặc MBR cũ
sudo dd if=/dev/zero of=${DISK} bs=1M count=10 status=progress
```

### 4.3. Tạo phân vùng MBR chuẩn bằng `parted`

Chúng ta chia thẻ nhớ thành 2 phân vùng:
- **Phân vùng 1 (`${DISK}1`)**: 64 MB, định dạng FAT32, dùng chứa Bootloader (`MLO`, `u-boot.img`, `uEnv.txt`).
- **Phân vùng 2 (`${DISK}2`)**: Phần dung lượng còn lại của thẻ nhớ, định dạng ext4, dùng chứa Linux Kernel (`zImage`), Device Tree (`.dtb`) và Root Filesystem.

```bash
sudo parted --script ${DISK} \
    mklabel msdos \
    mkpart primary fat32 1MiB 64MiB \
    set 1 boot on \
    mkpart primary ext4 64MiB 100%
```

Kiểm tra lại cấu trúc vừa tạo:
```bash
sudo parted ${DISK} print
```

### 4.4. Định dạng hệ thống tệp

```bash
# Định dạng phân vùng 1 thành FAT32, đặt nhãn (label) là "BOOT"
sudo mkfs.vfat -F 32 -n "BOOT" ${DISK}1

# Định dạng phân vùng 2 thành ext4, đặt nhãn là "rootfs"
sudo mkfs.ext4 -F -L "rootfs" ${DISK}2
```

---

## 5. NẠP BOOTLOADER VÀO THẺ NHỚ (2 PHƯƠNG PHÁP)

### PHƯƠNG PHÁP 1: Nạp qua FAT Filesystem (Phổ biến & Khuyên dùng cho MicroSD)

> [!IMPORTANT]
> **Sự thật về quy tắc sao chép `MLO` đầu tiên (First File Myth vs Reality)**:
> - Trong cộng đồng lập trình nhúng, thường có lưu truyền rằng *"Bắt buộc phải copy MLO đầu tiên, nếu copy sau thì ROM Code không nhận"*. 
> - **Thực tế kỹ thuật**: ROM Code của AM335x hoàn toàn có khả năng phân tích danh mục thư mục FAT để tìm kiếm chuỗi tên file `MLO`. Tuy nhiên, ROM Code đòi hỏi số sector ghi nhận trong bảng phân vùng MBR phải đồng nhất tuyệt đối với số sector khai báo trong Boot Sector của hệ thống tệp FAT. 
> - Việc sao chép file `MLO` ngay lập tức sau khi chạy `mkfs.vfat` đảm bảo metadata của `MLO` nằm ngay tại **Cluster đầu tiên** của thư mục gốc (`Root Directory Entry`), giúp tốc độ tìm kiếm của ROM Code đạt mức tức thì và tránh mọi rủi ro lỗi phân mảnh thư mục.

Thực hiện sao chép theo đúng trình tự:

```bash
# 1. Tạo thư mục mount tạm và mount phân vùng 1
mkdir -p /tmp/bbb_boot
sudo mount ${DISK}1 /tmp/bbb_boot

# 2. SAO CHÉP MLO ĐẦU TIÊN
sudo cp MLO /tmp/bbb_boot/
sync

# 3. Sao chép U-Boot Proper
sudo cp u-boot.img /tmp/bbb_boot/
sync

# 4. Sao chép hoặc tạo file cấu hình uEnv.txt
cat << 'EOF' | sudo tee /tmp/bbb_boot/uEnv.txt
console=ttyS0,115200n8
loadaddr=0x82000000
fdtaddr=0x88000000
bootfile=zImage
fdtfile=am335x-boneblack.dtb
mmcroot=/dev/mmcblk0p2 ro
mmcrootfstype=ext4 rootwait
mmcargs=setenv bootargs console=${console} root=${mmcroot} rootfstype=${mmcrootfstype} panic=10
loadimage=load mmc 0:2 ${loadaddr} /boot/${bootfile}
loadfdt=load mmc 0:2 ${fdtaddr} /boot/dtbs/${fdtfile}
uenvcmd=echo Nạp Linux từ SD...; run loadimage; run loadfdt; run mmcargs; bootz ${loadaddr} - ${fdtaddr}
EOF
sync

# 5. Tháo mount an toàn trước khi rút thẻ
sudo umount /tmp/bbb_boot
```

---

### PHƯƠNG PHÁP 2: Nạp RAW Flashing theo Sector (Dùng cho eMMC hoặc môi trường không Filesystem)

SoC AM335x hỗ trợ chế độ **Raw Mode Booting** khi đọc eMMC hoặc thẻ nhớ. Trong chế độ này, ROM Code không cần đọc hệ thống tệp FAT mà đọc trực tiếp dữ liệu từ các offset sector cố định:

- **Vị trí của MLO**: Phải nằm tại offset **128 KB** (tương đương sector số 256, với sector = 512 bytes).
- **Vị trí của `u-boot.img`**: Phải nằm tại offset **384 KB** (tương đương sector số 768).

Lệnh ghi trực tiếp bằng `dd`:

```bash
# Ghi MLO tại offset 128KB (seek=1 với block size 128k)
sudo dd if=MLO of=${DISK} seek=1 bs=128k status=progress
sync

# Ghi u-boot.img tại offset 384KB (seek=1 với block size 384k hoặc seek=3 với bs=128k)
sudo dd if=u-boot.img of=${DISK} seek=1 bs=384k status=progress
sync
```

Phương pháp này thường được sử dụng khi flash bootloader vào chip eMMC nội (`/dev/mmcblk1`) của BeagleBone Black để không chiếm dụng phân vùng FAT.

---

## 6. KIỂM THỬ KHỞI ĐỘNG TRÊN BO MẠCH

1. Rút thẻ MicroSD ra khỏi máy tính, cắm vào khe cắm thẻ MicroSD của bo mạch BeagleBone Black.
2. Kết nối cáp chuyển đổi **USB-to-TTL Serial 3.3V** vào hàng chân J1 trên bo mạch:
   - **Chân 1 (GND - chấm màu trắng)**: Nối vào GND của cáp.
   - **Chân 4 (RX)**: Nối vào TX của cáp.
   - **Chân 5 (TX)**: Nối vào RX của cáp.
3. Mở chương trình theo dõi Serial trên máy Host:
   ```bash
   picocom -b 115200 /dev/ttyUSB0
   # Hoặc dùng minicom / screen:
   # screen /dev/ttyUSB0 115200
   ```
4. **Bấm giữ nút S2 (BOOT Button)** trên BeagleBone Black, sau đó cắm cáp nguồn Mini-USB hoặc nguồn 5V.
5. Giữ nút S2 khoảng 2-3 giây rồi nhả ra.
6. Quan sát màn hình terminal: Log khởi động của **SPL** và **U-Boot Proper** sẽ xuất hiện rõ ràng:

```
U-Boot SPL 2024.01-bbb-build (Oct 10 2026 - 22:30:00 +0700)
Trying to boot from MMC1


U-Boot 2024.01-bbb-build (Oct 10 2026 - 22:30:00 +0700)

CPU  : AM335X-GP rev 2.1
Model: TI AM335x BeagleBone Black
DRAM:  512 MiB
Core:  160 devices, 18 uclasses, devicetree: separate
WDT:   Started wdt@44e35000 with servicing every 1000ms (60s timeout)
NAND:  0 MiB
MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
Loading Environment from FAT... OK
Hit any key to stop autoboot:  2 
```
Nếu bạn nhìn thấy thông điệp trên, xin chúc mừng: Bạn đã hoàn thành việc tự tay build và nạp U-Boot thành công!
