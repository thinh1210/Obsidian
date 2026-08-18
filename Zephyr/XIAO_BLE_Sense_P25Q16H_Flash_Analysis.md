# Phân tích nguyên lý nạp và lỗi Flash ngoại vi (P25Q16H) trên XIAO BLE Sense

## 1. Nguyên lý nạp Firmware của XIAO BLE Sense
* **Bộ điều khiển chính (nRF52840)**: Chứa **1MB Internal Flash**. Mã nguồn chạy thực tế của bạn (như code Zephyr đọc IMU) bắt buộc phải được nạp và chạy trên Internal Flash này (tại địa chỉ `0x27000`).
* **Chip nhớ ngoài (Puya P25Q16H)**: Là chip QSPI Flash ngoại vi **2MB**. 
* **Quá trình nạp qua USB (Bootloader mode)**: 
  1. Khi bạn vào Bootloader mode (bằng cách double-tap nút reset), MCU nRF52840 sẽ giả lập một ổ đĩa ảo định dạng FAT có tên `XIAO-SENSE`. Bộ nhớ FAT ảo này được lưu trữ vật lý trên chip Flash ngoại vi **P25Q16H**.
  2. Khi bạn copy file `.uf2` vào ổ đĩa ảo, dữ liệu thực chất đang được ghi xuống chip `P25Q16H` qua giao tiếp QSPI.
  3. Bootloader (chạy trên nRF52840) sẽ tự động đọc các khối dữ liệu `.uf2` này từ `P25Q16H`, tiến hành giải mã và ghi đè trực tiếp vào **Internal Flash** của nRF52840 tại địa chỉ `0x27000`. 
  4. Sau khi hoàn tất, chip tự động Reset để khởi chạy ứng dụng mới.

---

## 2. Tại sao có thể không nạp được code liên quan đến P25Q16H?
Dựa theo datasheet của **P25Q16H**, có 2 lý do phần cứng phổ biến khiến việc nạp (copy UF2) có vẻ thành công nhưng code không chạy:

### Lý do 1: Chế độ bảo vệ ghi (Write Protection) trên P25Q16H bị khóa
* Theo datasheet (phần Status Register), chip P25Q16H có các bit bảo vệ khối (`BP0` đến `BP4`) và chân bảo vệ phần cứng `WP#` (chân số 3).
* Nếu các bit này vô tình bị khóa (có thể do firmware cũ ghi nhầm cấu hình, hoặc do nhiễu vật lý trên chân `WP#`), chip Flash ngoại vi `P25Q16H` sẽ chuyển sang chế độ **Read-Only (Chỉ đọc)**.
* **Hậu quả:** Hệ điều hành Linux của bạn báo copy file thành công (do HĐH sử dụng bộ nhớ đệm cache để ghi), nhưng thực tế chip `P25Q16H` từ chối ghi dữ liệu vật lý. Do đó, Bootloader không nhận được file `.uf2` thật, nó bỏ qua việc nạp và board vẫn chạy code cũ (như blinky cũ).

### Lý do 2: Lỗi nhận diện JEDEC ID (Lỗi tương thích Bootloader cũ)
* Các lô hàng mới của Seeed Studio chuyển sang dùng chip flash Puya `P25Q16H` có mã định danh JEDEC ID là: `[0x85, 0x60, 0x15]` thay cho dòng chip GD25Q16 cũ.
* Nếu board của bạn đang chạy phiên bản Bootloader cũ (phiên bản trước khi có bản cập nhật hỗ trợ Puya), Bootloader sẽ không nhận dạng được JEDEC ID này. Dẫn tới hệ thống không thể giao tiếp ghi chép dữ liệu lên đĩa ảo bị lỗi.

---

## 🛠️ Giải pháp khắc phục triệt để
Nếu gặp phải tình trạng này, giải pháp mạnh nhất là bạn cần thực hiện **Mass Erase** (xóa toàn bộ chip bao gồm cả việc reset các bit khóa bảo vệ thanh ghi trạng thái của `P25Q16H`) và nạp lại phiên bản Bootloader mới nhất.

* **Cách thực hiện**: Cần sử dụng cổng nạp phần cứng **SWD** ở mặt sau của board thông qua một mạch nạp ngoài (ví dụ: J-Link, DAPLink hoặc sử dụng Raspberry Pi chạy OpenOCD).
