# Workflow Chuẩn: Tự động hóa Mở rộng Từ vựng (Bản Nâng cấp A1-C2)

Quy trình này quy định cách thức hoạt động của các Subagent khi được gọi để sinh từ vựng cho một chủ đề bất kỳ trong Obsidian Vault.

## 1. Yêu cầu Số lượng & Cấp độ
Mỗi khi khởi tạo một chủ đề, số lượng từ vựng cần sinh phải rơi vào khoảng **50 từ vựng**.
Quan trọng nhất: Phải bao phủ đủ mọi cấp độ từ cơ bản đến nâng cao:
- **A1-A2 (Basic):** Khoảng 15-20 từ phổ thông nhất.
- **B1-B2 (Intermediate):** Khoảng 15-20 từ trung cấp.
- **C1-C2 (Advanced/Proficiency):** Khoảng 10-15 từ học thuật, hiếm gặp.

## 2. Định dạng File Note Từ vựng
Các file `.md` được tạo ra phải tuân thủ nghiêm ngặt định dạng sau:

```markdown
# [Từ vựng]

*[Từ loại]*

- **[EN]:** Định nghĩa tiếng Anh
- **[VN]:** Định nghĩa tiếng Việt

**Level:** [A1/A2/B1/B2/C1/C2]

---
## Examples
1. *Ví dụ tiếng Anh 1*
   - Dịch nghĩa tiếng Việt 1
2. *Ví dụ tiếng Anh 2*
   - Dịch nghĩa tiếng Việt 2

---
## Memory Hack (Mẹo nhớ)
[Chèn phương pháp etymology, story, hoặc sound-alike để dễ nhớ]

---
## Word Family & Synonyms
**Word Family:**
- [Noun]: ...
- [Verb]: ...
- [Adj]: ...
- [Adv]: ...

**Synonyms:**
- [Từ đồng nghĩa 1], [Từ đồng nghĩa 2]
```

## 3. Quy chuẩn Bảng Mục lục (`0_{Topic}_Index.md`)
Sau khi sinh xong các file từ vựng, hệ thống (Master Agent hoặc Subagent) PHẢI cập nhật/tái cấu trúc file Index của thư mục đó bằng Python Script (tên file bắt đầu bằng `0_` để file Index luôn hiển thị ở trên cùng danh sách).
- Cấu trúc bảng bắt buộc: `| Từ vựng | Level | Loại từ | Nghĩa ngắn gọn | Word Family | Link Note |`
- Việc sắp xếp bảng bắt buộc phải ưu tiên theo cột **Level (A1 -> C2)**, sau đó mới đến Alphabet.

## 4. Cách triển khai (Execution)
Subagents nên viết một file Python script `.py` vào thư mục nháp (scratch) để tự động hóa việc tạo 50 file `.md` nhằm tránh bị giới hạn output token. Tuyệt đối không chỉnh sửa đè lên file Index bằng tay mà phải dùng script để duyệt và cập nhật file Index sau cùng.
