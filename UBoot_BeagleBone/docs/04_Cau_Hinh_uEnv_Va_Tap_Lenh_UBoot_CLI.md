# 🖥️ Chương 4: Cấu Hình uEnv.txt & Từ Điển Lệnh U-Boot CLI

> **Mục tiêu học tập**:
> 1. Hiểu sâu bản chất cơ chế nạp biến môi trường từ file `uEnv.txt`.
> 2. Thành thạo cấu hình mẫu `uEnv.txt` để khởi động Linux Kernel tùy biến.
> 3. Nắm vững từ điển tra cứu các lệnh U-Boot CLI phục vụ phát triển và gỡ lỗi hệ thống nhúng.

---

## 1. BẢN CHẤT CƠ CHẾ HOẠT ĐỘNG CỦA `uEnv.txt`

Trong U-Boot, các biến môi trường mặc định được biên dịch cứng (hardcoded) vào mã nguồn. Tuy nhiên, việc phải biên dịch lại U-Boot mỗi khi muốn đổi tham số dòng lệnh kernel (`bootargs`) hoặc đổi địa chỉ nạp là rất bất tiện.

Để giải quyết vấn đề này, các bo mạch TI AM335x và BeagleBone tích hợp cơ chế nạp cấu hình động từ file **`uEnv.txt`**:
- **Cơ chế nạp**: U-Boot đọc nội dung file văn bản `uEnv.txt` vào RAM tại địa chỉ `scriptaddr` (hoặc `loadaddr`), sau đó gọi lệnh nội bộ `env import -t ${loadaddr} ${filesize}` để phân tích cú pháp dạng `key=value` và nạp trực tiếp vào bảng biến môi trường trong RAM.
- **Vị trí tìm kiếm mặc định**:
  1. Phân vùng 1 (FAT32): `/uEnv.txt`
  2. Phân vùng 2 (ext4): `/boot/uEnv.txt`
- **Quy tắc định dạng**: File phải được lưu dưới dạng văn bản thuần túy (Plain text) với ký tự kết thúc dòng là **Unix (LF `\n`)**. Nếu tạo file trên Windows (dùng CRLF `\r\n`), U-Boot sẽ parse lỗi và coi ký tự `\r` là một phần của tên biến hoặc giá trị!

---

## 2. FILE CẤU HÌNH `uEnv.txt` HOÀN CHỈNH CHO BEAGLEBONE BLACK

Dưới đây là một file `uEnv.txt` mẫu được cấu trúc chuyên nghiệp, có chú thích chi tiết từng biến:

```ini
# ==============================================================================
# BeagleBone Black - Production uEnv.txt Configuration
# ==============================================================================

# 1. Cấu hình cổng Serial Console
# Lưu ý: Kernel hiện đại (>= 4.x/5.x) dùng ttyS0; Kernel rất cũ (3.8.x) dùng ttyO0
console=ttyS0,115200n8

# 2. Bản đồ địa chỉ nạp trên DDR3 RAM (Base: 0x80000000)
loadaddr=0x82000000
fdtaddr=0x88000000
rdaddr=0x88080000

# 3. Tên và đường dẫn các file nhị phân của Linux
bootdir=/boot
bootfile=zImage
fdtfile=am335x-boneblack.dtb

# 4. Xác định thiết bị và phân vùng chứa Root Filesystem
# mmc 0: Thẻ nhớ MicroSD; mmc 1: eMMC onboard
mmcdev=0
bootpart=0:2
mmcroot=/dev/mmcblk0p2 ro
mmcrootfstype=ext4 rootwait

# 5. Tham số dòng lệnh Linux Kernel (bootargs)
# - console: Chỉ định UART xuất log
# - root: Thiết bị chứa rootfs
# - ro: Mount rootfs ở chế độ Read-Only ban đầu (systemd sẽ remount rw sau)
# - rootwait: Chờ thẻ nhớ MMC sẵn sàng trước khi panic
# - earlycon: Cho phép kernel in log cực sớm trước khi driver tty hoàn tất nạp
optargs=earlycon=uart8250,mmio32,0x44e09000
mmcargs=setenv bootargs console=${console} root=${mmcroot} rootfstype=${mmcrootfstype} ${optargs} panic=10

# 6. Các macro nạp file từ phân vùng ext4 vào RAM
loadimage=load mmc ${bootpart} ${loadaddr} ${bootdir}/${bootfile}
loadfdt=load mmc ${bootpart} ${fdtaddr} ${bootdir}/dtbs/${fdtfile}

# 7. Kịch bản chạy tự động (U-Boot sẽ tự động kích hoạt biến 'uenvcmd')
uenvcmd=echo "==== [1/3] Đang nạp Linux Kernel zImage ===="; \
        run loadimage; \
        echo "==== [2/3] Đang nạp Device Tree Blob ===="; \
        run loadfdt; \
        echo "==== [3/3] Đang thiết lập bootargs ===="; \
        run mmcargs; \
        echo "==== Khởi động Linux Kernel qua bootz... ===="; \
        bootz ${loadaddr} - ${fdtaddr}
```

> [!NOTE]
> **Giải thích lệnh `bootz ${loadaddr} - ${fdtaddr}`**:
> Cú pháp lệnh `bootz` gồm 3 tham số:
> `bootz <địa chỉ Kernel> <địa chỉ Ramdisk/Initrd> <địa chỉ Device Tree>`
> Khi hệ thống không sử dụng Ramdisk (nạp rootfs trực tiếp từ thẻ nhớ), tham số thứ hai được thay bằng dấu gạch ngang `-`.

---

## 3. TỪ ĐIỂN TRA CỨU CÁC LỆNH U-BOOT CLI THÔNG DỤNG

Khi kết nối cáp Serial UART0 với BeagleBone Black, nhấn một phím bất kỳ trong thời gian đếm ngược để vào cửa sổ lệnh U-Boot prompt (`=>`).

### 3.1. Nhóm lệnh quản lý thẻ nhớ & lưu trữ (MMC/eMMC)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `mmc list` | `mmc list` | `mmc list` | Liệt kê danh sách các bộ điều khiển MMC trên bo mạch (`OMAP SD/MMC: 0`, `OMAP SD/MMC: 1`). |
| `mmc dev` | `mmc dev <dev_num> [part_num]` | `mmc dev 0` | Chuyển ngữ cảnh làm việc sang MMC 0 (MicroSD) hoặc MMC 1 (eMMC). |
| `mmc info` | `mmc info` | `mmc info` | In thông số kỹ thuật của thiết bị MMC đang chọn: dung lượng, phiên bản chuẩn, bus width (4-bit hay 8-bit), tốc độ truyền. |
| `mmc part` | `mmc part` | `mmc part` | Hiển thị bảng phân vùng (Partition Table) trên thiết bị MMC hiện tại kèm start sector, số lượng block và tên phân vùng. |
| `mmc rescan` | `mmc rescan` | `mmc rescan` | Quét lại bus MMC (dùng khi vừa rút ra cắm lại thẻ nhớ trong lúc U-Boot đang bật). |

---

### 3.2. Nhóm lệnh thao tác hệ thống tập tin (File Systems)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `fatls` | `fatls <interface> <dev:part> [directory]` | `fatls mmc 0:1` | Liệt kê danh sách file và thư mục trong phân vùng FAT32. |
| `fatload` | `fatload <interface> <dev:part> <addr> <filename>` | `fatload mmc 0:1 0x82000000 zImage` | Nạp một file từ phân vùng FAT vào bộ nhớ RAM tại địa chỉ chỉ định. Biến `${filesize}` sẽ tự động lưu kích thước byte thực tế vừa đọc. |
| `ext4ls` | `ext4ls <interface> <dev:part> [directory]` | `ext4ls mmc 0:2 /boot` | Liệt kê danh sách file trong thư mục trên phân vùng ext4. |
| `ext4load` | `ext4load <interface> <dev:part> <addr> <filename>` | `ext4load mmc 0:2 0x88000000 /boot/am335x-boneblack.dtb` | Nạp file từ phân vùng ext4 vào RAM. |
| `load` | `load <interface> <dev:part> <addr> <filename>` | `load mmc 0:2 0x82000000 /boot/zImage` | **Lệnh nạp đa năng (Khuyên dùng)**: Tự động phát hiện định dạng phân vùng (FAT hay ext2/3/4) và nạp file vào RAM. |

---

### 3.3. Nhóm lệnh quản lý biến môi trường (Environment Variables)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `printenv` | `printenv [variable_name]` | `printenv bootargs` | In toàn bộ các biến môi trường hoặc in một biến cụ thể. |
| `setenv` | `setenv <variable_name> [value]` | `setenv bootdelay 5` | Thiết lập hoặc cập nhật biến môi trường trong RAM. Nếu bỏ trống value (`setenv myvar`), biến sẽ bị xóa. |
| `saveenv` | `saveenv` | `saveenv` | Ghi đè toàn bộ biến môi trường hiện tại từ RAM vào bộ nhớ lưu trữ vĩnh viễn (eMMC/MicroSD). |
| `env default` | `env default -a` | `env default -a` | Khôi phục toàn bộ biến môi trường về giá trị mặc định được biên dịch trong mã nguồn. |
| `run` | `run <variable_name>` | `run uenvcmd` | Thực thi một chuỗi các câu lệnh được lưu trong biến môi trường. Các câu lệnh phân tách nhau bằng dấu chấm phẩy `;`. |

---

### 3.4. Nhóm lệnh khởi động hệ điều hành (Boot Commands)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `bootz` | `bootz <kernel_addr> [initrd_addr] <fdt_addr>` | `bootz 0x82000000 - 0x88000000` | Khởi động Linux Kernel dạng nén `zImage` (chuẩn ARM hiện đại). |
| `bootm` | `bootm <kernel_addr> [initrd_addr] [fdt_addr]` | `bootm 0x82000000` | Khởi động Kernel kiểu legacy `uImage` (tạo bởi công cụ `mkimage`). |
| `boot` | `boot` | `boot` | Thực thi lệnh khởi động mặc định được lưu trong biến `bootcmd`. |

---

### 3.5. Nhóm lệnh thao tác trực tiếp bộ nhớ RAM & Thanh ghi phần cứng (Memory & Register Debugging)

Các lệnh này cho phép lập trình viên nhúng đọc và ghi trực tiếp vào bất kỳ địa chỉ vật lý nào (RAM DDR3 hoặc thanh ghi ngoại vi MMIO):

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `md` | `md.[b\|w\|l\|q] <addr> [count]` | `md.l 0x44E10040 1` | **Memory Display**: Đọc bộ nhớ theo byte (`.b`), 16-bit word (`.w`), 32-bit long (`.l`). Ví dụ trên đọc thanh ghi `control_status` để xem trạng thái SYSBOOT pins. |
| `mw` | `mw.[b\|w\|l\|q] <addr> <val> [count]` | `mw.l 0x82000000 0x12345678 1` | **Memory Write**: Ghi giá trị vào địa chỉ RAM. Rất hữu ích để kiểm tra tính toàn vẹn của RAM DDR3. |
| `mm` | `mm.[b\|w\|l\|q] <addr>` | `mm.l 0x44E10800` | **Memory Modify**: Tương tác ghi giá trị vào ô nhớ với con trỏ tự động tăng sau mỗi lần nhấn Enter. |
| `cmp` | `cmp.[b\|w\|l] <addr1> <addr2> <count>` | `cmp.b 0x82000000 0x83000000 0x1000` | So sánh dữ liệu giữa 2 vùng nhớ trong RAM (kiểm tra sau khi copy hoặc checksum). |

---

### 3.6. Nhóm lệnh thao tác Device Tree Blob (FDT Commands)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `fdt addr` | `fdt addr <addr>` | `fdt addr 0x88000000` | Khai báo cho U-Boot biết vị trí Device Tree Blob đang nằm trong RAM để chuẩn bị thao tác. |
| `fdt print` | `fdt print [path]` | `fdt print /ocp/serial@44e09000` | In toàn bộ hoặc một nhánh cây Device Tree đang nạp trong RAM. |
| `fdt set` | `fdt set <path> <property> [value]` | `fdt set /chosen bootargs "console=ttyS0"` | Thay đổi hoặc bổ sung một thuộc tính trực tiếp trong Device Tree trước khi boot. |
| `fdt resize` | `fdt resize [extra_bytes]` | `fdt resize 8192` | Nới rộng vùng nhớ của DTB trong RAM để chuẩn bị áp dụng các Device Tree Overlay (`.dtbo`). |
| `fdt apply` | `fdt apply <overlay_addr>` | `fdt apply 0x89000000` | Gộp (merge) một file Device Tree Overlay vào cây thiết bị gốc. |

---

### 3.7. Nhóm lệnh kiểm tra ngoại vi (GPIO, I2C)

| Lệnh | Cú pháp | Ví dụ cụ thể | Giải thích chi tiết |
| :--- | :--- | :--- | :--- |
| `gpio status` | `gpio status [-a]` | `gpio status -a` | Hiển thị trạng thái logic (in/out, high/low) của toàn bộ các chân GPIO trên bo mạch. |
| `gpio set` | `gpio set <pin_number>` | `gpio set 53` | Bật chân GPIO lên mức HIGH (GPIO1_21 = Chân 53 tương ứng đèn LED USR0 trên BBB). |
| `gpio clear` | `gpio clear <pin_number>` | `gpio clear 53` | Kéo chân GPIO về mức LOW (Tắt đèn LED USR0). |
| `i2c probe` | `i2c probe` | `i2c probe` | Quét toàn bộ bus I2C hiện tại và in ra danh sách các địa chỉ slave phản hồi ACK (ví dụ: `0x24` = PMIC, `0x50` = EEPROM). |
| `i2c md` | `i2c md <chip> <addr> [count]` | `i2c md 0x50 0.2 16` | Đọc dữ liệu từ thanh ghi của chip I2C (ví dụ đọc 16 byte đầu của chip EEPROM `0x50`). |

---

## 4. TỔNG KẾT BÀI HỌC

1. File `uEnv.txt` là cầu nối mềm dẻo nhất giữa người lập trình và bootloader, cho phép thay đổi tham số boot của Kernel mà không phải biên dịch lại U-Boot.
2. Nắm vững lệnh `load` (generic loader) và `bootz` giúp bạn dễ dàng khởi động hệ thống từ bất kỳ phân vùng lưu trữ nào.
3. Các công cụ gỡ lỗi bộ nhớ như `md` và `mw` là "vũ khí" đắc lực để chẩn đoán lỗi phần cứng, cấu hình thanh ghi và kiểm tra tín hiệu trước khi Kernel khởi chạy.
