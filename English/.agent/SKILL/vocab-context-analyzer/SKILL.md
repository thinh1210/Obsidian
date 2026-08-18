---
name: vocab-context-analyzer
description: Phân tích ngữ cảnh, cấp độ và chủ đề của một từ vựng tiếng Anh.
---
# Skill: Phân tích Ngữ cảnh Từ vựng (Vocabulary Context Analyzer)

## Mục đích
Khi người dùng cung cấp một từ vựng tiếng Anh, hãy phân tích để xác định các đặc tính cơ bản của nó. Điều này giúp định hướng cách học và sử dụng từ chính xác trong thực tế.

## Đầu vào
Một từ vựng tiếng Anh (kèm theo cụm từ hoặc idiom nếu có).

## Hướng dẫn thực hiện
1. **Phân tích Cấp độ (CEFR Level):** Xác định từ này thường thuộc cấp độ nào (A1, A2, B1, B2, C1, hay C2). Nếu thường xuất hiện trong IELTS/TOEIC, hãy ghi chú thêm.
2. **Ngữ cảnh sử dụng (Register/Tone):** Xác định từ này mang sắc thái gì: 
   - Formal (Trang trọng)
   - Informal (Thân mật)
   - Slang (Lóng)
   - Academic (Học thuật)
   - Khác (Old-fashioned, Poetic, etc.)
3. **Chủ đề (Topic/Domain):** Từ vựng này thường được sử dụng trong chủ đề hoặc lĩnh vực nào (ví dụ: Kinh doanh, Khoa học, Giao tiếp hàng ngày, Y tế).

## Đầu ra
Trình bày kết quả dưới dạng Markdown ngắn gọn:
```markdown
**Level:** [CEFR Level] (Note: IELTS/TOEIC nếu có)
**Ngữ cảnh:** [Formal/Informal/Academic...]
**Chủ đề:** [Topic]
```
