# 🛠️ Chương 9: Thực Hành Toàn Diện Với BeagleBone Black, Thẻ Nhớ & UART (Phần 1: Cấp Độ Cơ Sở & Trung Cấp)

> [!IMPORTANT]
> **Thiết kế chuyên biệt cho phần cứng hiện có của bạn**:
> Toàn bộ các bài thực hành (Labs) và mã nguồn trong chương này và Chương 10 được thiết kế để **chạy và kiểm chứng 100% chỉ với 3 món đồ bạn đang có**:
> 1. **01 Bo mạch BeagleBone Black (BBB)** (tận dụng tối đa 4 đèn LED `USR0..3`, nút nhấn `S2`, chip EEPROM `I2C0 0x50`, PMIC `0x24`, các thanh ghi nội AM335x và 2 nhân `PRU`).
> 2. **01 Thẻ nhớ MicroSD** (đóng vai trò thiết bị lưu trữ `MLO`, `u-boot.img`, `uEnv.txt`, `zImage`, `.dtb` và `RootFS`).
> 3. **01 Module đọc log UART (USB-to-TTL 3.3V)** cắm vào cổng **J1** (đóng vai trò giao diện điều khiển duy nhất từ lúc cấp nguồn cho tới khi vào Linux).

---

## 🔌 1. THIẾT LẬP KẾT NỐI VẬT LÝ & GIAO DIỆN UART TRÊN MÁY TÍNH

### 1.1. Sơ đồ đấu nối Module USB-UART vào Header J1 (6 chân)
Tìm hàng rào 6 chân đực ký hiệu **J1** nằm sát khe thẻ nhớ MicroSD. Chân số 1 được đánh dấu bằng một **chấm tròn trắng (`●`)** trên bo mạch:

```
  Module USB-to-TTL (3.3V)                 BeagleBone Black (Header J1)
 ┌────────────────────────┐               ┌────────────────────────────┐
 │          GND           │──────────────►│ Chân 1 (●) : GND (Nối đất) │
 │                        │               │ Chân 2     : NC  (Bỏ trống)│
 │                        │               │ Chân 3     : NC  (Bỏ trống)│
 │          TXD           │──────────────►│ Chân 4     : UART0_RX      │
 │          RXD           │◄──────────────│ Chân 5     : UART0_TX      │
 │      VCC (3.3V/5V)     │  (KHÔNG NỐI)  │ Chân 6     : NC  (Bỏ trống)│
 └────────────────────────┘               └────────────────────────────┘
```

### 1.2. Lệnh mở màn hình thu nhận Log & Điều khiển trên Linux (Ubuntu)
Mở Terminal trên máy tính của bạn và chạy lệnh sau trước khi cấp nguồn cho BeagleBone:

```bash
# Cấp quyền truy cập cổng USB Serial (nếu cần) và mở giao diện UART ở tốc độ 115200 baud
sudo chmod 666 /dev/ttyUSB0
picocom -b 115200 /dev/ttyUSB0
```
*(Mẹo: Để thoát khỏi `picocom`, bạn nhấn tổ hợp phím **`Ctrl + A`** sau đó nhấn **`Ctrl + X`**).*

---

## 🟢 2. LAB 1 (CẤP ĐỘ CƠ SỞ): LẬP TRÌNH C USERSPACE CHẨN ĐOÁN THANH GHI, ĐỌC EEPROM I2C0 & ĐIỀU KHIỂN 4 ĐÈN LED

* **Tài liệu đối chiếu**: *Exploring BeagleBone (TS. Derek Molloy)* & *AM335x Technical Reference Manual (SPRUH73)*.
* **Mã nguồn đầy đủ**: [bbb_diag.c](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/01_userspace_c_diag/bbb_diag.c) và [Makefile](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/01_userspace_c_diag/Makefile).
* **Recipe Yocto đã tích hợp**: [bbb-diag_1.0.bb](file:///home/thinh/yocto-lab/meta-myproject/recipes-apps/bbb-diag/bbb-diag_1.0.bb).

### 2.1. Giải phẫu các kỹ thuật cốt lõi trong `bbb_diag.c`

#### A. Đọc trực tiếp thanh ghi vật lý `DEVICE_ID` (`0x44E10600`) từ Userspace
Theo tài liệu **TI AM335x TRM (SPRUH73) - Mục 9.3.1.40**, tại địa chỉ vật lý `0x44E10600` (thuộc khối `Control Module` có địa chỉ cơ sở `0x44E10000`) có một thanh ghi 32-bit tên là `DEVICE_ID`.
Trong Linux Userspace, chúng ta không thể trỏ thẳng con trỏ C vào địa chỉ vật lý `0x44E10600` (sẽ bị lỗi *Segmentation Fault* do MMU chặn). Thay vào đó, ta mở thiết bị `/dev/mem` và dùng hàm hệ thống `mmap()`:

```c
/* Mở thiết bị bộ nhớ vật lý (yêu cầu quyền root) */
int fd = open("/dev/mem", O_RDONLY | O_SYNC);

/* Ánh xạ 8KB (0x2000) bắt đầu từ địa chỉ vật lý 0x44E10000 vào không gian ảo của tiến trình */
void *map_base = mmap(NULL, 0x2000, PROT_READ, MAP_SHARED, fd, 0x44E10000UL);

/* Cộng thêm độ lệch (offset) 0x0600 để trỏ đúng vào thanh ghi DEVICE_ID (0x44E10600) */
volatile uint32_t *device_id_reg = (volatile uint32_t *)((uint8_t *)map_base + 0x0600UL);
uint32_t dev_id = *device_id_reg;
```

**Bảng giải mã bit thanh ghi `DEVICE_ID` (`0x44E10600`)**:

| Bit | Tên trường | Giá trị trên BBB Rev C | Ý nghĩa kỹ thuật |
| :---: | :--- | :---: | :--- |
| `31:28` | `DEVREV` | `0x2` (`0010b`) | Phiên bản Silicon **PG2.1** (hỗ trợ xung nhịp 1GHz) |
| `27:12` | `PARTNUM` | `0xB944` | Mã định danh dòng chip **TI Sitara AM335x** |
| `11:1` | `MFG` | `0x017` | Mã nhà sản xuất JEDEC của **Texas Instruments** |
| `0` | `Reserved` | `1` | Luôn bằng 1 |

---

#### B. Giao tiếp trực tiếp chip EEPROM `24LC32A` trên Bus `I2C0` (`0x50`)
Không cần gắn thêm bất kỳ cảm biến ngoài nào, trên bo mạch BeagleBone Black đã có sẵn chip **EEPROM 4KB** gắn vào bus **`I2C0`** (`/dev/i2c-0`) tại địa chỉ **`0x50`**.

> [!TIP]
> **Tại sao phải dùng cờ `I2C_SLAVE_FORCE` thay vì `I2C_SLAVE`?**
> Khi Linux Kernel khởi động, driver `at24` của nhân đã tự động chiếm giữ địa chỉ `0x50`. Nếu gọi `ioctl(fd, I2C_SLAVE, 0x50)`, hệ thống sẽ trả về lỗi `EBUSY (Device or resource busy)`. Sử dụng **`I2C_SLAVE_FORCE`** cho phép chương trình C của bạn gửi khung truyền I2C trực tiếp xuống chip EEPROM mà không bị Kernel từ chối!

```c
/* Gửi 2 byte địa chỉ ô nhớ [0x00, 0x00] để đưa con trỏ đọc về byte đầu tiên của EEPROM */
uint8_t addr_buf[2] = { 0x00, 0x00 };
write(fd, addr_buf, 2);

/* Đọc 28 bytes cấu trúc Header chuẩn của BeagleBone */
read(fd, &hdr, sizeof(hdr));
```

---

### 2.2. Các lệnh thực thi và Kết quả thu được trên màn hình UART

Sau khi boot BeagleBone và đăng nhập qua cửa sổ UART (`root`), bạn gõ trực tiếp các lệnh sau:

```bash
# 1. Chạy toàn bộ quy trình kiểm tra phần cứng tự động
root@beaglebone:~# bbb_diag all
```

**Kết quả in ra trên màn hình UART của bạn**:
```text
=== [1] KIỂM TRA THANH GHI SOС TI AM335X (SPRUH73 Section 9.3.1.40) ===
  + Địa chỉ vật lý thanh ghi : 0x44E10600
  + Giá trị thô (Raw 32-bit) : 0x2B94402F
  + Mã Part Number           : 0xB944 (TI Sitara AM335x)
  + Mã Nhà sản xuất (JEDEC)  : 0x017 (Texas Instruments)
  + Phiên bản Silicon        : Silicon Revision 2.1 (PG2.1 - Phổ biến nhất trên BBB Rev C) (Code: 0x2)

=== [2] ĐỌC DỮ LIỆU CHIP EEPROM ONBOARD QUA I2C0 (Địa chỉ 0x50) ===
  + Magic Header  : 0xEE3355AA (HỢP LỆ - Chuẩn BeagleBone)
  + Tên Bo Mạch   : A335BNLT (BeagleBone Black / Green)
  + Phiên Bản PCB : 00C0
  + Số Serial     : 22244P160492 (Tuần 22, Năm 2024)

=== [3] CHẠY HIỆU ỨNG ĐÈN ĐUỔI KNIGHT RIDER TRÊN 4 ĐÈN LED USR0-USR3 ===
  -> Chu kỳ 3/3: [   | * |   |   ]
  [+] Hoàn thành! Khôi phục USR0 về chế độ heartbeat mặc định.
```

Bạn cũng có thể điều khiển từng đèn LED riêng lẻ từ cổng UART:
```bash
root@beaglebone:~# bbb_diag led 1 on          # Bật sáng đèn USR1
root@beaglebone:~# bbb_diag led 2 on          # Bật sáng đèn USR2
root@beaglebone:~# bbb_diag led 1 off         # Tắt đèn USR1
root@beaglebone:~# bbb_diag sweep 10          # Chạy đèn đuổi 10 vòng liên tiếp
```

---

## 🟡 3. LAB 2 (CẤP ĐỘ TRUNG CẤP): VIẾT LỆNH CLI TÙY BIẾN TRONG U-BOOT (`bbb_hwinfo`) & KỊCH BẢN `uEnv.txt`

* **Tài liệu đối chiếu**: *FastBit Embedded Linux Step by Step* & *Bootlin Embedded Linux System Development*.
* **Mã nguồn đầy đủ**:
  - Lệnh U-Boot C: [cmd_bbb_hwinfo.c](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/02_uboot_custom_cmd_and_porting/cmd_bbb_hwinfo.c)
  - File cấu hình khởi động: [uEnv_sdcard_boot.txt](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/02_uboot_custom_cmd_and_porting/uEnv_sdcard_boot.txt)

### 3.1. Giải phẫu kỹ thuật điều khiển thanh ghi Bare-metal trong `cmd_bbb_hwinfo.c`

Khi đang ở dấu nhắc `=>` của U-Boot (trước khi Linux Kernel chạy), MMU chưa khóa không gian địa chỉ, do đó bạn có thể đọc/ghi **trực tiếp** mọi thanh ghi phần cứng của chip AM335x bằng hai macro `readl(addr)` và `writel(val, addr)`:

1. **Giải mã trạng thái nút nhấn Boot `S2` qua thanh ghi `CONTROL_STATUS` (`0x44E10040`)**:
   - Ngay tại khoảnh khắc cấp nguồn, ROM Code đọc mức điện áp trên 16 chân `SYSBOOT[15:0]` và chốt (latch) vào 16 bit thấp của thanh ghi `0x44E10040`.
   - Chân nút nhấn **S2** nối trực tiếp vào đường **`SYSBOOT[2]`**:
     - Nếu bạn **không nhấn S2**: `SYSBOOT[4:0] = 11100b` (`0x1C`) $\rightarrow$ Thứ tự boot: `MMC1 (eMMC)` $\rightarrow$ `MMC0 (Thẻ nhớ SD)` $\rightarrow$ `UART0` $\rightarrow$ `USB0`.
     - Nếu bạn **nhấn giữ S2**: `SYSBOOT[4:0] = 11000b` (`0x18`) $\rightarrow$ Thứ tự boot: `SPI0` $\rightarrow$ `MMC0 (Thẻ nhớ SD)` $\rightarrow$ `USB0` $\rightarrow$ `UART0`.
2. **Điều khiển 4 đèn LED `USR0..3` bằng thanh ghi `GPIO1` (`0x4804C000`)**:
   - Đèn `USR0..USR3` nối với các chân **`GPIO1_21` đến `GPIO1_24`**:
   ```c
   /* Bước 1: Xóa các bit 21..24 trong thanh ghi GPIO_OE (0x4804C134) về 0 để đặt làm Output */
   uint32_t oe_val = readl(0x4804C134);
   writel(oe_val & ~(0x0FUL << 21), 0x4804C134);

   /* Bước 2: Ghi bit 1 vào thanh ghi GPIO_SETDATAOUT (0x4804C194) để bật sáng cả 4 đèn */
   writel(0x0FUL << 21, 0x4804C194);

   /* Bước 3: Ghi bit 1 vào thanh ghi GPIO_CLEARDATAOUT (0x4804C190) để tắt cả 4 đèn */
   writel(0x0FUL << 21, 0x4804C190);
   ```

### 3.2. Cách tích hợp `cmd_bbb_hwinfo.c` vào mã nguồn U-Boot

```bash
# 1. Copy file vào thư mục cmd/ của U-Boot
cp /home/thinh/Obsidian/UBoot_BeagleBone/code_examples/02_uboot_custom_cmd_and_porting/cmd_bbb_hwinfo.c ~/u-boot/cmd/bbb_hwinfo.c

# 2. Đăng ký vào cuối file cmd/Makefile
echo "obj-y += bbb_hwinfo.o" >> ~/u-boot/cmd/Makefile

# 3. Biên dịch lại U-Boot
cd ~/u-boot
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- am335x_evm_defconfig
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j12
```

### 3.3. Thử nghiệm trực tiếp trên cổng UART (Ngay cả khi chưa sửa code U-Boot!)

Ngay cả với bản U-Boot tiêu chuẩn có sẵn trên thẻ nhớ của bạn, bạn có thể thực hiện đúng thao tác đọc thanh ghi `SYSBOOT` và bật/tắt 4 đèn LED `USR0..3` bằng các lệnh `md.l` và `mw.l` tại dấu nhắc `=>` trên màn hình UART:

```text
# 1. Đọc thanh ghi DEVICE_ID (0x44E10600) và CONTROL_STATUS (0x44E10040)
=> md.l 0x44e10600 1
44e10600: 2b94402f                               /.+

=> md.l 0x44e10040 1
44e10040: 0040031c                               ..@.
# (2 chữ số cuối là 1c -> Nút S2 không nhấn; nếu là 18 -> Nút S2 đã được nhấn!)

# 2. Cấu hình GPIO1_21..24 làm Output và bật sáng cả 4 đèn LED USR0..3 ngay trong U-Boot!
=> mw.l 0x4804c134 0xfe1fffff
=> mw.l 0x4804c194 0x01e00000   <-- Nhìn xuống bo mạch: Cả 4 đèn USR0..3 lập tức sáng rực!
=> mw.l 0x4804c190 0x01e00000   <-- Cả 4 đèn USR0..3 lập tức tắt!
```

---

## 💾 4. QUY TRÌNH TẠO THẺ NHỚ MICROSD KHỞI ĐỘNG CHUẨN XÁC

Sử dụng kịch bản tự động [prepare_bbb_sdcard.sh](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/06_sdcard_flasher_and_uart_scripts/prepare_bbb_sdcard.sh) đã được chuẩn bị sẵn:

```bash
# Cấp quyền thực thi cho script
chmod +x /home/thinh/Obsidian/UBoot_BeagleBone/code_examples/06_sdcard_flasher_and_uart_scripts/prepare_bbb_sdcard.sh

# Nếu nạp file ảnh .wic từ Yocto (Thay /dev/sdX bằng tên thẻ nhớ của bạn, ví dụ /dev/sdb):
sudo /home/thinh/Obsidian/UBoot_BeagleBone/code_examples/06_sdcard_flasher_and_uart_scripts/prepare_bbb_sdcard.sh wic /dev/sdX core-image-minimal-beaglebone-yocto.rootfs.wic

# Nếu phân vùng thủ công và chép MLO, u-boot.img, zImage, dtb, uEnv.txt, rootfs:
sudo /home/thinh/Obsidian/UBoot_BeagleBone/code_examples/06_sdcard_flasher_and_uart_scripts/prepare_bbb_sdcard.sh manual /dev/sdX /duong/dan/thu/muc/chua/file
```
