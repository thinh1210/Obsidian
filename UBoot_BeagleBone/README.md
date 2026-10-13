# 🦴 Giáo Trình Nghiên Cứu Chuyên Sâu: U-Boot & Bootloader Architecture Trên BeagleBone Black (TI AM335x)

Bộ tài liệu này được biên soạn và hệ thống hóa chuyên sâu dành riêng cho việc **học tập, nghiên cứu và phát triển hệ thống nhúng Linux** xoay quanh bootloader **Das U-Boot** và vi xử lý **Texas Instruments AM335x** (Cortex-A8) trên bo mạch **BeagleBone Black**.

Tài liệu được thiết kế tương thích hoàn hảo với cơ chế liên kết ghi chú của **Obsidian**, tích hợp sơ đồ tuần tự **Mermaid**, giải phẫu mã nguồn C/Device Tree và các bài thực hành **Hands-on Lab**.

---

## 🗺️ LỘ TRÌNH HỌC TẬP & DANH SÁCH CÁC CHƯƠNG (CURRICULUM ROADMAP)

```mermaid
graph LR
    Ch1["Chương 1: Kiến Trúc Boot Flow<br>(ROM -> SPL -> U-Boot -> Kernel)"] --> Ch2["Chương 2: Giải Phẫu Mã Nguồn<br>(C Code, EEPROM, PMIC, DDR3)"]
    Ch2 --> Ch3["Chương 3: Thực Hành Build & Flash<br>(Cross-compile, MBR, FAT32, Raw)"]
    Ch3 --> Ch4["Chương 4: uEnv.txt & U-Boot CLI<br>(Từ điển lệnh, Memory Debugging)"]
    Ch4 --> Ch5["Chương 5: Nâng Cao & Gỡ Lỗi<br>(Capes Overlays, UUID, Troubleshooting)"]
```

---

| Chương | Tên Chuyên Đề | Nội dung chính & Kỹ năng đạt được |
| :---: | :--- | :--- |
| **01** | [Chương 1: Tổng Quan Kiến Trúc Boot Flow AM335x](./docs/01_Tong_Quan_Kien_Truc_Boot_Flow_AM335x.md) | Phân tầng 4 giai đoạn khởi động; Giải mã chi tiết tại sao cần SPL/MLO; Giới hạn 109 KB Internal SRAM; Chân `SYSBOOT[15:0]`, nút S2, Cold vs Warm Reset; Bản đồ bộ nhớ 512MB DDR3. |
| **02** | [Chương 2: Giải Phẫu Mã Nguồn U-Boot Cho BeagleBone](./docs/02_Giai_Phau_Ma_Nguon_UBoot_Cho_BeagleBone.md) | Phân tích `am335x_evm_defconfig`; Thư mục `board/ti/am335x/` (`board.c`, `board.h`, `mux.c`); Đọc EEPROM ID `A335BNLT`; Kỹ thuật port U-Boot cho Custom Board; Nâng áp PMIC TPS65217C lên 1.325V; Cấu hình DDR3 timing; Phân tích `am335x_evm.h` và Device Tree trong U-Boot (`u-boot,dm-spl`). |
| **03** | [Chương 3: Thực Hành Build U-Boot & Tạo Thẻ Nhớ Boot](./docs/03_Thuc_Hanh_Build_UBoot_Va_Tao_The_Nho_Boot.md) | Cài đặt Toolchain ARM `gcc-arm-linux-gnueabihf`; Clone mã nguồn Denx U-Boot; Biên dịch ra `MLO` và `u-boot.img`; Kiểm tra GP Header bằng `hexdump`; Phân vùng MBR bằng `parted`; Quy tắc sao chép `MLO` vào FAT32; Phương pháp Raw Flashing vào eMMC (`seek=1 bs=128k`). |
| **04** | [Chương 4: Cấu Hình uEnv.txt & Từ Điển Lệnh U-Boot CLI](./docs/04_Cau_Hinh_uEnv_Va_Tap_Lenh_UBoot_CLI.md) | Cơ chế `env import`; File cấu hình `uEnv.txt` mẫu hoàn chỉnh giải thích từng biến (`console`, `loadaddr`, `fdtaddr`, `bootargs`, `uenvcmd`); Từ điển tra cứu toàn diện các lệnh U-Boot CLI: quản lý MMC (`mmc`), hệ thống file (`fatload`, `ext4load`, `load`), biến môi trường (`setenv`, `saveenv`), khởi động (`bootz`), can thiệp RAM & thanh ghi (`md`, `mw`, `mm`), Device Tree (`fdt`). |
| **05** | [Chương 5: Kỹ Thuật Nâng Cao, Repo Mẫu & Gỡ Lỗi](./docs/05_Cac_Ky_Thuat_Nang_Cao_Va_Phan_Tich_Repo_Mau.md) | Phân tích kỹ thuật từ `RobertCNelson/boot-scripts`: Cape Manager (Device Tree Overlays trong U-Boot), UUID tự động cho RootFS; Hướng dẫn thực hành nạp Kernel thủ công từng lệnh qua UART Console; Cẩm nang chẩn đoán 4 sự cố kinh điển: UART im lặng, chuỗi "CCCC...", treo ở SPL, treo sau "Starting kernel...". |

---

## 🔗 LIÊN KẾT HỆ SINH THÁI GHI CHÚ TRONG VAULT (CROSS-REFERENCES)

Bộ tài liệu này kết nối trực tiếp với chuỗi tài liệu **Linux Kernel Architecture** trong cùng Vault Obsidian của bạn:

- 📄 **Cấu hình Bootloader truyền `bootargs` vào Kernel**: Xem chi tiết tại [Chương 3: Linux Kernel Usage - Config, Build & Boot](../Linux_Bootlin/docs/03_Linux_Kernel_Usage_Config_Build_Boot.md).
- 📄 **Cú pháp Device Tree và cơ chế Pinctrl**: Xem chi tiết tại [Chương 5: Hardware Description & Device Tree](../Linux_Bootlin/docs/05_Hardware_Description_Device_Tree.md).
- 📄 **Lập trình Memory-Mapped I/O (MMIO)**: Xem chi tiết tại [Chương 8: Memory Management & I/O Memory](../Linux_Bootlin/docs/08_Memory_Management_IO_Memory.md).

---

## 📚 TÀI NGUYÊN & GITHUB REPOSITORIES THAM KHẢO

1. **Denx Das U-Boot Mainline**: [https://github.com/u-boot/u-boot](https://github.com/u-boot/u-boot)
2. **BeagleBoard.org U-Boot Mirror**: [https://github.com/beagleboard/u-boot](https://github.com/beagleboard/u-boot)
3. **Robert C. Nelson Boot Scripts**: [https://github.com/RobertCNelson/boot-scripts](https://github.com/RobertCNelson/boot-scripts)
4. **Robert C. Nelson Kernel & U-Boot Builder**: [https://github.com/RobertCNelson/bb-kernel](https://github.com/RobertCNelson/bb-kernel)
5. **Texas Instruments AM335x Technical Reference Manual (TRM)**: Document mã hiệu **SPRUH73** (Chương 26: *Initialization*).
