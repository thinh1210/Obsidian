# 🐧 Tài Liệu Học Tập & Tra Cứu Linux Kernel Architecture & Driver Development (Mastery Edition)

Bộ tài liệu này được nâng cấp, hệ thống hóa và mở rộng chuyên sâu từ khóa học **Linux Kernel and Driver Development** của **Bootlin** (446 slides). 

Tài liệu được viết bằng **Tiếng Việt**, bổ sung chi tiết nội dung slide, các bài thực hành **Practical Labs** (mô phỏng bo mạch BeagleBone Black / QEMU ARM64 / cảm biến Wii Nunchuk I2C / Serial UART), sơ đồ kiến trúc **Mermaid**, xử lý tình huống lỗi thực tế và bộ bài tập tự luyện tập hands-on.

---

## 🗺️ Danh Sách Các Chương Bài Học (Table of Contents & Practical Labs)

| Chương | Tên Chương | Nội dung chính & Bài Thực Hành (Practical Labs) |
| :--- | :--- | :--- |
| **01** | [Chương 1: Linux Kernel Introduction](./01_Linux_Kernel_Introduction.md) | Vai trò Kernel, Monolithic Architecture, User vs Kernel space, System Calls, Pseudo filesystems (`sysfs`, `procfs`). <br>🧪 **Lab 1**: Viết C Benchmark đo thời gian System Call Trap vs User Space; Khám phá `/proc` & `/sys`. |
| **02** | [Chương 2: Linux Kernel Sources](./02_Linux_Kernel_Sources.md) | Quy trình phát triển Mainline/LTS, Cấu trúc thư mục nguồn (`arch/`, `drivers/`, `fs/`), Giấy phép GPLv2. <br>🧪 **Lab 2**: Clone mã nguồn Kernel; Dùng `cscope`/`ctags` tra cứu `start_kernel()`; Kiểm tra mã nguồn với `checkpatch.pl`. |
| **03** | [Chương 3: Kernel Usage - Config, Build & Boot](./03_Linux_Kernel_Usage_Config_Build_Boot.md) | Cấu hình `Kconfig`/`menuconfig`, Biên dịch chéo (Cross-compilation), Bootloader (U-Boot) `bootargs`, Quản lý Modules (`modprobe`). <br>🧪 **Lab 3**: Biên dịch chéo Kernel ARM64; Khởi động mô phỏng hệ thống với QEMU. |
| **04** | [Chương 4: Developing Kernel Modules](./04_Developing_Kernel_Modules.md) | Cấu trúc Module (`module_init`/`module_exit`), Tham số module (`module_param`), Export symbols (`EXPORT_SYMBOL_GPL`), Kbuild Makefile. <br>🧪 **Lab 4**: Viết Out-of-tree Module nhận tham số mảng; Thay đổi tham số qua `/sys/module/`. |
| **05** | [Chương 5: Hardware Description & Device Tree](./05_Hardware_Description_Device_Tree.md) | Phân loại phần cứng, Cú pháp Device Tree (`.dts`, `.dtb`), Nodes/Properties (`compatible`, `reg`), Pin Muxing & Subsystem Pinctrl. <br>🧪 **Lab 5**: Viết nút Device Tree mô tả cảm biến I2C Nunchuk; Thực hành biên dịch & decompile với `dtc`. |
| **06** | [Chương 6: Linux Device & Driver Model](./06_Device_Driver_Model.md) | Kiến trúc Unified Device Model (`bus_type`, `device`, `driver`), Matching mechanism, Platform Drivers, I2C Subsystem. <br>🧪 **Lab 6**: Viết Driver I2C Nunchuk; Đọc 6 byte dữ liệu thô SMBus từ cảm biến. |
| **07** | [Chương 7: Kernel Frameworks & Char Drivers](./07_Kernel_Frameworks_Char_Drivers.md) | Major/Minor numbers, Character Drivers (`cdev`, `file_operations`), Trao đổi an toàn `copy_to_user`, Input Subsystem, Managed APIs (`devm_*`). <br>🧪 **Lab 7**: Tích hợp Nunchuk vào Input Subsystem; Kiểm thử sự kiện nút bấm & Joystick bằng `evtest`. |
| **08** | [Chương 8: Memory Management & I/O Memory](./08_Memory_Management_IO_Memory.md) | Virtual Memory, Allocators (Buddy, SLUB), API (`kmalloc` vs `vmalloc`), MMIO (`ioremap`, `readl`/`writel`), Memory Barriers. <br>🧪 **Lab 8**: Ánh xạ MMIO thanh ghi GPIO; Đọc/ghi thanh ghi để bật/tắt đèn LED phần cứng. |
| **09** | [Chương 9: Clock, Power & Misc Subsystem](./09_Clock_Power_Misc_Subsystem.md) | Common Clock Framework (`clk_*`), Reset Controllers, Power Management (Suspend/Resume, Runtime PM), Subsystem `miscdevice`. <br>🧪 **Lab 9**: Viết Driver Serial UART dùng `miscdevice` & CCF Clock API; Gửi ký tự qua `/dev/feserial`. |
| **10** | [Chương 10: Processes, Scheduling, Interrupts & Locking](./10_Processes_Scheduling_Interrupts_Concurrency.md) | Process Context vs Interrupt Context, Wait Queues, Top-half ISR vs Threaded IRQ/Workqueues, Concurrency, Spinlocks vs Mutexes. <br>🧪 **Lab 10**: Đăng ký Ngắt nút bấm GPIO Threaded IRQ; Dùng `spin_lock_irqsave` & `wait_event_interruptible`. |
| **11** | [Chương 11: Direct Memory Access (DMA)](./11_Direct_Memory_Access_DMA.md) | Nguyên lý DMA, Giải quyết bất đồng bộ CPU Cache (Coherent vs Streaming mappings), Slave DMA Engine Framework. <br>🧪 **Lab 11**: Lập trình cấp phát Coherent DMA Memory (`dma_alloc_coherent`); Cấu hình DMA mask 32-bit. |
| **12** | [Chương 12: Kernel Debugging & Advanced APIs](./12_Kernel_Debugging_Useful_APIs.md) | Log levels (`printk`, `dev_dbg`), Dynamic Debug, Debugfs, Kernel Oops analysis, Macro `container_of`, Circular Linked Lists, `mmap`. <br>🧪 **Lab 12**: Tạo giao diện `debugfs`; Đọc/ghi biến tinh chỉnh động trong `/sys/kernel/debug/`. |

---

## 💡 Cấu Trúc Đặt Ra Cho Mỗi File Chương
Mỗi file chương Markdown được tổ chức theo tiêu chuẩn 5 tầng học tập:
1. 📌 **Phân tích lý thuyết slide chuyên sâu** (Kèm sơ đồ Mermaid).
2. 🛠️ **Hướng dẫn bài thực hành Practical Lab chi tiết** (Mã nguồn C + Makefile + Lệnh terminal).
3. 💡 **Tình huống lỗi thực tế & Cách Debug** (Edge Cases & Debugging Tips).
4. 📝 **Bài tập thực hành Hands-on tự giải & Câu hỏi trắc nghiệm ôn tập**.
