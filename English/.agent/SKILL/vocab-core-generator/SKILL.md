---
name: vocab-core-generator
description: Tạo định nghĩa, ví dụ thực tế và collocations cho từ vựng.
---
# Skill: Xây dựng Nội dung Cốt lõi Từ vựng (Vocabulary Core Generator)

## Mục đích
Tạo ra phần cốt lõi của một thẻ từ vựng: Định nghĩa ngắn gọn dễ hiểu, các ví dụ bám sát đời thực và các cụm từ thường đi kèm (collocations).

## Đầu vào
Một từ vựng tiếng Anh và thông tin về ngữ cảnh của nó (nếu có từ bước trước).

## Hướng dẫn thực hiện
1. **Định nghĩa (Definition):** 
   - Cung cấp nghĩa tiếng Anh ngắn gọn, dễ hiểu.
   - Cung cấp nghĩa tiếng Việt tương ứng, sát với cách diễn đạt tự nhiên của người Việt.
2. **Ví dụ thực tế (Real-world Examples):** Tạo đúng 3 câu ví dụ có bối cảnh cụ thể để người học dễ tưởng tượng:
   - *Ví dụ 1 (Đời sống hàng ngày):* Một câu giao tiếp thông thường bạn có thể nói với bạn bè hoặc gia đình.
   - *Ví dụ 2 (Công sở / Học thuật):* Một câu dùng trong môi trường làm việc, viết email, hoặc viết luận.
   - *Ví dụ 3 (Văn hóa đại chúng):* Một câu giống như lời thoại trong phim, hoặc trích dẫn từ tin tức/bài báo.
   - (Bao gồm phần dịch tiếng Việt cho mỗi câu ví dụ).
3. **Collocations (Cụm từ đi kèm):** 
   - Liệt kê 3-5 collocations phổ biến nhất với từ này (ví dụ: động từ + danh từ, tính từ + danh từ).
   - Dịch nghĩa ngắn gọn cho mỗi collocation.

## Đầu ra
Trình bày dưới dạng Markdown:
```markdown
**Meaning:** 
- [EN]: ...
- [VN]: ...

**Collocations:**
- `[Collocation 1]`: [Nghĩa VN]
- `[Collocation 2]`: [Nghĩa VN]

**Examples:**
1. 💬 *Daily:* [Câu Tiếng Anh] -> *[Nghĩa Tiếng Việt]*
2. 💼 *Work/Academic:* [Câu Tiếng Anh] -> *[Nghĩa Tiếng Việt]*
3. 🎬 *Media/Movie:* [Câu Tiếng Anh] -> *[Nghĩa Tiếng Việt]*
```
