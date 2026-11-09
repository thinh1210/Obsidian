# Dự Án Mẫu: Remote Debugging C/C++ trên BeagleBone Black với VS Code

Thư mục này chứa toàn bộ mã nguồn, Makefile và cấu hình mẫu `.vscode` để bạn có thể mở trực tiếp trong VS Code trên máy tính máy chủ (Ubuntu/Host PC) và gỡ lỗi trực quan một ứng dụng C chạy trên bo mạch BeagleBone Black.

---

## 1. Cấu Trúc Thư Mục

```text
07_vscode_remote_debugging/
├── .vscode/
│   ├── launch.json              <-- Cấu hình Debugger F5 (1-Click Auto SSH Pipe, Manual TCP :2345, Kernel KGDB)
│   ├── tasks.json               <-- Cấu hình tác vụ tự động (Build ARM ELF, SCP sang BBB, dọn dẹp tiến trình)
│   └── c_cpp_properties.json    <-- Cấu hình IntelliSense (nhận diện include headers từ Yocto Sysroot)
├── src/
│   └── hello_debug.c            <-- Chương trình C thực nghiệm (biến, struct, vòng lặp, nhấp nháy LED USR3, malloc)
├── scripts/
│   ├── arm-gdb-wrapper.sh       <-- Script kích hoạt Yocto GDB 14.2 với đầy đủ thư viện phụ thuộc
│   └── arm-gcc-wrapper.sh       <-- Script kích hoạt Yocto GCC 13.5 kèm cờ tối ưu hóa Cortex-A8 & hard-float
├── Makefile                     <-- Biên dịch tự động, hỗ trợ "make deploy" nạp mã qua mạng LAN/USB RNDIS
└── README.md
```

---

## 2. Hướng Dẫn Sử Dụng Trong VS Code

### Bước 1: Mở Thư Mục Trong VS Code
Khởi chạy VS Code và mở thư mục này:
```bash
code /home/thinh/Obsidian/UBoot_BeagleBone/code_examples/07_vscode_remote_debugging
```
*Đảm bảo máy host đã cài extension **C/C++** (`ms-vscode.cpptools`).*

### Bước 2: Thiết Lập Kết Nối SSH Mạng (USB RNDIS hoặc LAN)
Kết nối BeagleBone Black với máy host qua cáp USB mini (giao diện mạng RNDIS `192.168.7.2`) hoặc cáp mạng LAN.
Kiểm tra SSH:
```bash
ssh root@192.168.7.2
```
*(Trên image `bbb-debug-image` đã cấu hình `debug-tweaks`, không cần mật khẩu).*

### Bước 3: Đặt Breakpoint và Bấm F5 (Chế độ 1-Click Auto)
1. Mở file [src/hello_debug.c](file:///home/thinh/Obsidian/UBoot_BeagleBone/code_examples/07_vscode_remote_debugging/src/hello_debug.c).
2. Click chuột vào lề trái cạnh dòng `89` (bên trong hàm `main`) để tạo một **chấm đỏ (Breakpoint)**.
3. Chuyển sang tab **Run & Debug** (phím tắt `Ctrl + Shift + D`).
4. Chọn cấu hình: **`1. [1-Click Auto] Debug C/C++ on BeagleBone (SSH Pipe)`**.
5. Nhấn **F5**:
   - VS Code tự động gọi `tasks.json` biên dịch file C thành mã máy ARM (`-g -O0`).
   - Tự động dùng `scp` đẩy file `hello_debug` sang bo BeagleBone.
   - Kích hoạt `gdbserver` qua SSH tunnel và kết nối GDB.
   - Con trỏ vàng dừng lại ngay tại dòng code bạn vừa đặt Breakpoint trên bo mạch thật!

### Bước 4: Thao Tác Gỡ Lỗi Trực Quan Trên Giao Diện VS Code
- **F10 (Step Over)**: Chạy qua từng dòng lệnh tiếp theo.
- **F11 (Step Into)**: Nhảy vào bên trong hàm con (ví dụ: `calculate_adjusted_temperature`).
- **Shift + F11 (Step Out)**: Thoát khỏi hàm con quay về hàm gọi.
- **Bảng Variables**: Xem trực tiếp giá trị biến `i`, struct `g_system_sensor`, các cờ logic.
- **Bảng Watch**: Thêm biểu thức muốn theo dõi như `g_system_sensor.temperature * 1.8 + 32`.
- **Bảng Call Stack**: Xem lịch sử các frame gọi hàm từ `main()` -> `process_sensor_buffer()`.
