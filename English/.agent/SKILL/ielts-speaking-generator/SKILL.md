---
name: ielts-speaking-generator
description: Nhận plain text backbone (khung sườn văn bản thô) hoặc hình ảnh đề thi IELTS Speaking, tự động mở rộng và tạo bài note học toàn diện chuẩn Band 5.0 - 6.5 và Band 7.0+, kèm phân tích ngữ pháp, cầu thang từ vựng và câu trả lời mẫu song song.
---

# Skill: IELTS Speaking Master Note Generator (From Plain Text Backbone / Images)

## 🎯 Mục đích
Skill này tiếp nhận **Plain text backbone** (khung sườn văn bản thô gồm danh sách câu hỏi, từ khóa, gợi ý ý tưởng) hoặc **Hình ảnh đề bài** từ người dùng, sau đó tự động hoàn thiện và phát triển thành một bài học/ghi chú Speaking toàn diện theo định dạng Obsidian chuẩn mực.

Bài note được thiết kế theo cấu trúc chuẩn:
1. Nắm chắc cách trả lời đạt chuẩn **Band 5.0 - 6.5** (trôi chảy, đúng ngữ pháp, tự nhiên).
2. Học cách bứt phá lên **Band 7.0 - 8.0+** thông qua phân tích so sánh song song, cầu thang từ vựng và các mẫu câu phức tạp.

---

## 📥 Đầu vào (Inputs)
Người dùng cung cấp **Plain Text Backbone** (khung sườn văn bản thô) chứa:
- **Chủ đề (Topic Name):** Ví dụ: *Accommodation, Daily Routine, Work and Studies, Travel, Hobbies, Technology...*
- **Sub-themes / Gợi ý có sẵn:** Các từ khóa hoặc khía cạnh nhỏ người dùng liệt kê (VD: *types of house, favorite room, noisy neighbors...*).
- **Danh sách câu hỏi:**
  - Part 1 questions
  - Part 2 cue cards (You should say...)
  - Part 3 discussion questions (nếu có)
- *(Tùy chọn)* Một số từ vựng thô mà người dùng muốn sử dụng hoặc mở rộng.

*(Lưu ý: Skill vẫn hỗ trợ nhận dạng từ hình ảnh chụp sách/bảng viết tay nếu người dùng gửi ảnh).*

---

## 🔄 Quy trình thực hiện (Step-by-Step Workflow)

### Bước 1: Tiếp nhận & Phân tích Plain Text Backbone (Parsing)
1. Xác định rõ:
   - **Tên chủ đề chính** và tên file tương ứng (VD: `Accommodation.md`, `Work and Studies.md`).
   - Các **tiểu chủ đề (Sub-themes)** tiềm năng liên quan trực tiếp đến topic.
   - Các câu hỏi Part 1 & Part 2 cần giải quyết.
   - Các ý tưởng, từ vựng hoặc gợi ý mà người dùng đã phác thảo để giữ lại và phát triển lên tầm cao hơn.

---

### Bước 2: Xây dựng cấu trúc bài note chuẩn mực trong Obsidian
Mỗi bài Speaking Note hoàn chỉnh PHẢI tuân thủ cấu trúc 7 phần sau:

```markdown
# IELTS Speaking - Topic: [Tên Topic] (Từ Nền Tảng 5.0 - 6.5 Đến Nâng Cao 7.0 - 8.0+)

## 📌 I. Tiêu Chí Khác Biệt Giữa Band 5.0 - 6.5 và Band 7.0 - 8.0+
(Bảng so sánh 3 tiêu chí: Fluency, Lexical Resource, Grammatical Range)

## 🪜 II. Bảng Cầu Thang Từ Vựng (Lexical Ladder)
(Bảng đối chiếu từ vựng cơ bản Band 5.0-6.5 vs từ nâng cấp Band 7.0-8.0+, kèm IPA, nghĩa tiếng Việt, collocations và ví dụ câu)

## 🔍 III. Phân Tích Chuyên Sâu Các Từ Vựng Trọng Điểm
(Phân tích 5-6 từ đắt giá: sắc thái nghĩa, so sánh với từ đồng nghĩa thông thường, collocations, lỗi phát âm người Việt hay mắc phải)

## 🧠 IV. Phân Tích Cấu Trúc Câu Theo Các Theme Nhỏ (Sentence Pattern Analysis)
(Mỗi theme nhỏ có 1-2 mẫu câu phức cao cấp: Câu chẻ, Phân từ rút gọn, Đảo ngữ điều kiện, So sánh kép kèm Template + Phân tích ngữ pháp + Ví dụ cụ thể)

## 🗣️ V. Part 1: So Sánh Câu Trả Lời Giữa Band 5.0 - 6.5 và Band 7.0 - 8.0+
(Mỗi câu hỏi Part 1 có 2 phiên bản: Bản 5.0-6.5 và Bản 7.0-8.0+ kèm mục Upgrade Analysis & Paraphrasing Alternatives)

## 🎤 VI. Part 2: Cue Card, Full Model (Band 7.5) & Paraphrasing Bank
(Dàn ý 4 bước Mindmap + Bài mẫu 2 phút + Bảng hoán đổi từ vựng Band 6.0 vs Band 7.5+)

## 🎯 VII. Lộ Trình Luyện Tập Từng Bước (Action Plan)
```

---

## 📋 Hướng Dẫn Chi Tiết Từng Phần

### 1. Bảng Cầu Thang Từ Vựng (Lexical Ladder)
Bắt buộc có các cột:
- **Khía cạnh biểu đạt** (Ý nghĩa cơ bản muốn diễn đạt).
- **Band 5.0 - 6.5** (Từ vựng thông dụng, quen thuộc).
- **Band 7.0 - 8.0+** (Collocation, Idiomatic phrase, Academic/Sophisticated word).
- **Phiên âm IPA** của từ nâng cao.
- **Ý nghĩa & Sắc thái sử dụng** (ngữ cảnh phù hợp, tránh lạm dụng sai sắc thái).

### 2. Phân Tích Chuyên Sâu Từ Trọng Điểm (Word Analysis)
Chọn 5-6 từ then chốt thường bị dùng sai sắc thái hoặc phát âm sai:
- **Định nghĩa & Sắc thái:** Tại sao từ này đắt giá hơn từ cơ bản.
- **Phân biệt từ dễ nhầm lẫn:** Chỉ ra ranh giới giữa từ học thuật và từ thông dụng.
- **Collocations đi kèm:** Các cụm từ tự nhiên người bản xứ hay dùng.
- **Lưu ý phát âm (Pronunciation & Stress):** Nhấn trọng âm âm mấy, bật âm đuôi nào.

### 3. Phân Tích Mẫu Câu Theo Các Theme Nhỏ (Sentence Pattern Analysis)
Chia topic thành 4 - 6 chủ đề nhỏ (Sub-themes). Mỗi sub-theme cung cấp:
- **Tên cấu trúc ngữ pháp:** (Ví dụ: *Cleft sentence with 'What'*, *Past Participle Clause*, *Inversion Conditional*, *Double Comparative*).
- **Cấu trúc khung (Template):** Công thức có chỗ trống để người học tự ráp thông tin.
- **Phân tích ngữ pháp (Grammar Breakdown):** Giải thích tại sao cấu trúc này ăn điểm GRA 7.0+.
- **Ví dụ mẫu hoàn chỉnh:** Áp dụng thực tế vào chính sub-theme đó.

### 4. Thiết Kế Câu Trả Lời Part 1 Song Song 2 Cấp Độ
Với mỗi câu hỏi trong backbone:
- 🟢 **Bản 5.0 - 6.5:** Trả lời trực tiếp, rõ ý theo công thức A.R.E (Answer - Reason - Example), dùng từ chuẩn mực nhưng không quá phức tạp, dễ nói trơn tru.
- 🔵 **Bản 7.0 - 8.0+:** Dùng collocations đắt giá, cấu trúc câu phức, tư duy có chiều sâu hoặc đối chiếu tương phản.
- 🔍 **Upgrade Analysis:** Gạch đầu dòng chỉ rõ:
  - *Từ cơ bản* ➡️ *Từ nâng cấp*
  - Điểm cải thiện về mặt ngữ pháp.
- 🔄 **Paraphrasing Alternatives:** Cung cấp thêm 2-3 cách diễn đạt đồng nghĩa cho từ/cụm từ chính trong câu kèm IPA.

### 5. Part 2 Cue Card & Paraphrasing Bank
- **Dàn ý tư duy (Mindmap 4 bước):** Định hướng ý trả lời trong 1 phút chuẩn bị.
- **Bài mẫu hoàn chỉnh 2 phút (Band 7.5+):** Chia đoạn rõ ràng, lồng ghép các idioms và collocations tự nhiên.
- **Kho từ vựng hoán đổi (Paraphrasing Bank):** Bảng so sánh cụm từ thường gặp ở Band 6.0 và cụm tương đương ở Band 7.5 - 8.0+.

---

## 💾 Lưu file và định dạng Obsidian
- Đường dẫn lưu mặc định: `/home/thinh/Obsidian/English/IELTS Note/Speaking/[Tên Topic].md`
- Dùng Markdown chuẩn của Obsidian:
  - Bảng (`| Col 1 | Col 2 |`) rõ ràng, thẳng hàng.
  - Callout alerts: `> [!TIP]`, `> [!WARNING]`, `> [!NOTE]`.
  - In đậm (**bold**) các từ vựng và collocations trọng điểm.
  - Phiên âm kẹp trong dấu backtick (ví dụ: `/ˌpɪk.tʃəˈresk/`).
