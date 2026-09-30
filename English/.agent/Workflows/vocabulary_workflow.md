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
> /[Phiên âm IPA]/

![[[tên_từ_chuẩn_hóa].mp3]]

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
Sau khi sinh xong các file từ vựng, hệ thống (Master Agent hoặc Subagent) PHẢI cập nhật/tái cấu trúc file Index của thư mục đó theo **Kiến trúc Phân loại Ngữ nghĩa Trực quan (Semantic Clustering)**:
- Tên file bắt đầu bằng `0_` để file Index luôn hiển thị ở trên cùng danh sách (VD: `0_CITY_Index.md`).
- **Sơ đồ liên kết chủ đề (Semantic Map):** Nằm ngay đầu trang (`## 🗺️ Sơ đồ liên kết chủ đề (Semantic Map)`), liệt kê các nhánh phân nhóm kèm các wikilinks `[[Từ vựng]]` để người học dễ dàng nắm bắt bức tranh tổng quan.
- **Phân chia nhóm ngữ nghĩa (Semantic Sub-groups):** Mỗi chủ đề được chia thành 3 - 4 phân nhóm ngữ nghĩa trực quan (VD: với `CITY` là Cơ sở vật chất, Giao thông mặt đất, Khu vực quy hoạch, Nhịp sống thành thị).
- **Cấu trúc bảng cho từng nhóm:** Mỗi nhóm có tiêu đề `### [Icon] [STT]. [Tên nhóm Tiếng Việt] ([English Title])`, một đoạn mô tả ngắn ngữ cảnh, và một bảng 7 cột chuẩn:
  `| Từ vựng | Phát âm | Level | Loại từ | Nghĩa ngắn gọn | Word Family | Link Note |`
- Cột **Phát âm** chứa cả phiên âm IPA lẫn biểu tượng phát âm gắn link âm thanh: `/<ipa>/ [[<filename>.mp3\|🔊]]` (LƯU Ý: Phải dùng ký tự thoát `\|` để tránh làm vỡ cột của bảng Markdown).
- Việc sắp xếp bảng bắt buộc phải ưu tiên theo cột **Level (A1 -> C2)**, sau đó mới đến Alphabet.
- **Đồng bộ Note con:** Từng note con tương ứng trong chủ đề cần được cập nhật dòng metadata: `| **Phân nhóm:** <Tên nhóm>`.
- **Đoạn văn thực tế (Contextual Story):** Phần câu chuyện ngữ cảnh song ngữ Anh - Việt ở cuối trang Index PHẢI được bảo tồn nguyên vẹn 100%.

## 4. Quản lý File Âm thanh (Audio Assets)
- Toàn bộ file âm thanh định dạng `.mp3` được lưu tập trung tại `/home/thinh/Obsidian/English/audio/`.
- Tên file âm thanh được chuẩn hóa theo định dạng chữ thường, thay khoảng trắng và dấu gạch nối bằng dấu gạch dưới (VD: `sold_out.mp3`, `look_after.mp3`).
- Script tải tự động: `download_audio.py` tại thư mục gốc của Vault hoặc trong `English/audio/`.

## 5. Cách triển khai (Execution)
Subagents nên viết một file Python script `.py` vào thư mục nháp (scratch) để tự động hóa việc tạo 50 file `.md` nhằm tránh bị giới hạn output token. Tuyệt đối không chỉnh sửa đè lên file Index bằng tay mà phải dùng script để duyệt và cập nhật file Index sau cùng.
