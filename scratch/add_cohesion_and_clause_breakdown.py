import os
import re

BASE_DIR = "/home/thinh/Obsidian/English/Writing"

clause_cohesion_data = {
    "task2/agree_disagree/Sample_01_Overweight_Physical_Education.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cấu trúc mệnh đề bên trong câu (Intra-sentence) VÀ cách câu này móc xích nhịp nhàng với câu đứng trước (Inter-sentence Cohesion) để đạt điểm tối đa tiêu chí Coherence & Cohesion.

---

#### 📌 Câu dài 1 (Mở bài - Câu ghép đa tầng nhượng bộ & nhân quả):
> *"Owing to the problems which a growing population of overweight people cause for the health care system, it is thought that the key to solving this issue is to have more sport and exercise in schools."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm giới từ chỉ nguyên nhân:** `[Owing to the problems]` (Giới từ chỉ nguyên nhân trang trọng thay cho *Because of*).
  - **Mệnh đề quan hệ xác định lồng ghép:** `[which]` (Đại từ quan hệ làm tân ngữ thay cho *problems*) + `[a growing population of overweight people]` (Chủ ngữ S_rel) + `[cause for the health care system]` (Vị ngữ V_rel).
  - **Mệnh đề chính dùng chủ ngữ giả (Main Clause):** `[it]` (Chủ ngữ giả) + `[is thought]` (Động từ to be & Phân từ bị động khách quan).
  - **Mệnh đề danh từ làm chủ ngữ thật (Noun Clause):** `[that]` (Liên từ) + `[the key to solving this issue]` (Chủ ngữ S_sub) + `[is]` (Động từ V_sub) + `[to have more sport and exercise in schools]` (Bổ ngữ nguyên mẫu).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Móc xích nhân quả mở đầu (Causal Hook & Background Framing).**
  - *Mối nối ngữ nghĩa:* Đây là câu mở đầu bài viết, kết nối trực tiếp với Đề thi (Exam prompt). Tác giả dùng cụm danh từ trừu tượng `[the problems]` kết hợp với `[this issue]` (Shell Noun) để tóm tắt trọn vẹn hiện tượng béo phì gây quá tải y tế từ đề bài làm bệ phóng giới thiệu giải pháp thể thao học đường.
  - *Kỹ thuật liên kết:* Dùng Shell Noun (`this issue`) và cấu trúc khách quan (`it is thought that`) tránh xưng hô ngôi thứ nhất ở câu mở đầu.
- 💡 **Công thức ghép câu:** `Owing to [Noun] which S_rel + V_rel, it is thought that the key to [V-ing / Noun] is to + V_inf.`

---

#### 📌 Câu dài 2 (Thân bài 1 - Câu phức đối chiếu thực trạng vs kỳ vọng):
> *"At the moment, the average child in the West does sport possibly twice a week, which is not enough to counteract their otherwise sedentary lifestyle that comes from many hours each day of sitting at a desk for their lessons."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Mệnh đề chính độc lập:** `[At the moment]` (Trạng ngữ thời gian) + `[the average child in the West]` (Chủ ngữ chính S_main) + `[does sport]` (Động từ & Tân ngữ V_main + O_main) + `[possibly twice a week]` (Trạng từ tần suất).
  - **Mệnh đề quan hệ không xác định 1:** `[which]` (Đại từ quan hệ thay thế cho toàn bộ sự việc ở mệnh đề chính) + `[is not enough to counteract their otherwise sedentary lifestyle]` (Vị ngữ nhận xét mục đích).
  - **Mệnh đề quan hệ xác định 2 lồng ghép:** `[that]` (Đại từ quan hệ bổ nghĩa cho *sedentary lifestyle*) + `[comes from many hours each day of sitting at a desk for their lessons]` (Vị ngữ chỉ nguồn gốc nguyên nhân).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Tương phản thời gian & Dẫn chứng thực tế làm rõ (Temporal Contrast & Factual Elaboration).**
  - *Mối nối với câu trước:* Câu trước khẳng định *"This method will encourage a new generation to develop vital habits... and maintain a reasonable weight"* (Kỳ vọng tương lai). Câu này móc xích bằng trạng ngữ `[At the moment]` (Thời điểm hiện tại) để đối chiếu: *Tương lai thì tốt, nhưng hiện tại chỉ tập 2 buổi/tuần là không đủ*.
  - *Kỹ thuật liên kết từ vựng (Lexical Chain):* Cụm `[their lessons]` liên kết trực tiếp với từ khóa `[schools]` ở câu trước đó; đại từ `[their]` quy chiếu chính xác về `[the average child]`.
- 💡 **Công thức ghép câu:** `At the moment, S_main + V_main + O_main, which is not enough to counteract [Noun Phrase] that comes from [Nguyên nhân].`

---

#### 📌 Câu dài 3 (Đầu Thân bài 2 - Câu phức đảo chiều luận điểm):
> *"However, targeting physical exercise in school children to reduce the current issue of obesity in the wider population is not effective enough on its own."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Liên từ tương phản:** `[However]` (Đứng đầu câu báo hiệu chuyển đoạn).
  - **Mệnh đề chính với Chủ ngữ là Cụm danh động từ phức hợp (Complex Gerund Subject):**
    - Chủ ngữ dài: `[targeting physical exercise in school children to reduce the current issue of obesity in the wider population]` (Toàn bộ hành động tập trung vào thể dục trường học).
    - Vị ngữ: `[is not effective enough on its own]` (Không đủ hiệu quả nếu chỉ thực hiện một mình).
- **2. 🔗 Phân tích Liên kết với câu/đoạn trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Chuyển hướng phản biện liên đoạn (Inter-paragraph Counter-argument / Contrast).**
  - *Mối nối với đoạn trước:* Thân bài 1 vừa ca ngợi hết lời lợi ích của thể dục học đường. Đầu Thân bài 2 lập tức dùng `[However]` để "bẻ lái" sang mặt hạn chế.
  - *Kỹ thuật đỉnh cao (Given-New Principle):* Tác giả không chỉ viết *"However, it is not enough"*, mà dùng toàn bộ cụm V-ing `[targeting physical exercise in school children...]` để **tóm tắt toàn bộ nội dung của Thân bài 1**, biến nó thành thông tin đã biết (Given information), rồi gắn vị ngữ mới `[is not effective enough on its own]` làm bệ đỡ đưa ra luận điểm về Dinh dưỡng (New information).
- 💡 **Công thức ghép câu:** `However, V-ing + [Tóm tắt ý đoạn 1] is not effective enough on its own, as [Ý mới].`""",

    "task2/discuss_both_views/Sample_01_University_vs_Work_Experience.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững kỹ thuật dùng liên từ bổ sung tầng cao (Additive transition) và kỹ thuật đưa ví dụ cụ thể hóa luận điểm trừu tượng.

---

#### 📌 Câu dài 1 (Thân bài 1 - Cấu trúc Not only... but + Động từ nhấn mạnh + Mệnh đề quan hệ):
> *"Not only that, but academia does promote the development of useful skills, not just academic knowledge, for example analytical thinking, research skills and intellectual curiosity, which are valuable transferable skills."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Thành phần nối lũy tiến:** `[Not only that, but]` (Không chỉ có vậy, mà còn...).
  - **Mệnh đề chính với trợ động từ nhấn mạnh (Emphatic Main Clause):** `[academia]` (Chủ ngữ chính S_main) + `[does promote]` (Trợ động từ khẳng định mạnh + Động từ) + `[the development of useful skills]` (Tân ngữ).
  - **Thành phần chêm xen liệt kê (Parenthetical Exemplification):** `[not just academic knowledge, for example analytical thinking, research skills and intellectual curiosity]`.
  - **Mệnh đề quan hệ không xác định (Non-defining Relative Clause):** `[which]` (Thay thế cho 3 kỹ năng trên) + `[are valuable transferable skills]` (Vị ngữ bổ nghĩa chỉ bản chất).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Bổ sung tầng bậc lũy tiến (Climactic Additive Cohesion).**
  - *Mối nối với câu trước:* Câu liền trước nêu luận điểm 1: Bằng đại học là điều kiện bắt buộc cho các ngành nghề chuyên môn (Bác sĩ, Luật sư). Câu này dùng `[Not only that, but]` để bắc cầu sang luận điểm 2 quan trọng hơn: Đại học không chỉ dạy kiến thức nghề, mà còn dạy kỹ năng tư duy phản biện.
  - *Kỹ thuật liên kết đại từ (Anaphoric Reference):* Từ `[that]` trong `Not only that` quy chiếu trực tiếp về toàn bộ việc bằng cấp mở ra cơ hội làm bác sĩ/luật sư ở câu trước.
- 💡 **Công thức ghép câu:** `Not only that, but S_main + does V_main + Noun, for example [A, B and C], which are [Adjective + Noun].`

---

#### 📌 Câu dài 2 (Thân bài 2 - Chủ ngữ V-ing phức hợp + Cấu trúc so sánh hơn + Rút gọn thời gian):
> *"For instance, for a corporate management position, having experience of managing others, running projects, delegating tasks and strong emotional intelligence is of more importance than the theory of management with no real hands-on experience when fresh out of university."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm trạng ngữ định vị:** `[For instance]` + `[for a corporate management position]`.
  - **Mệnh đề chính với Chủ ngữ Danh động từ đa thành phần:** `[having experience of managing others, running projects, delegating tasks and strong emotional intelligence]` (Chủ ngữ chính S_main) + `[is of more importance than]` (Vị ngữ so sánh hơn) + `[the theory of management with no real hands-on experience]` (Tân ngữ đối chiếu).
  - **Mệnh đề trạng ngữ rút gọn chỉ thời gian:** `[when]` + `[fresh out of university]` (Rút gọn từ *when they are fresh out of university*).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Minh họa cụ thể hóa luận điểm (Exemplification & Concrete Proof).**
  - *Mối nối với câu trước:* Câu trước nêu luận điểm khái quát: *"having relevant work experience and soft skills can throw the balance in favour of the job applicant for certain hands-on types of work"* (khái niệm trừu tượng: công việc thực hành). Câu này lập tức dùng `[For instance]` gắn vào một vị trí công việc cụ thể: `[a corporate management position]` để chứng minh tính đúng đắn.
  - *Kỹ thuật lặp từ vựng đối chiếu (Lexical Contrast):* Từ `[theory of management]` ở câu này tạo ra sự tương phản đối lập trực tiếp với `[hands-on experience]` ở câu trước.
- 💡 **Công thức ghép câu:** `For instance, for [Role], having experience of [V-ing 1, 2, and Noun] is of more importance than [Theory] when [Adjective phrase].`""",

    "task2/problem_solution/Sample_01_Criminal_Reoffending.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ diễn giải 'In other words' và mệnh đề trạng ngữ nhân quả để móc nối các mắt xích logic.

---

#### 📌 Câu dài 1 (Thân bài 1 - Câu giải thích bản chất với 'In other words'):
> *"In other words, offenders are not given a chance to retrain and learn new skills for their future or develop a deeper understanding of correct moral behaviour and how their actions affect other people."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Trạng từ nối diễn giải:** `[In other words]` (Nói cách khác...).
  - **Mệnh đề chính dạng bị động kép:** `[offenders]` (Chủ ngữ S_main) + `[are not given a chance]` (Vị ngữ bị động) + `[to retrain and learn new skills for their future]` (Động từ nguyên mẫu 1) + `[or develop a deeper understanding of correct moral behaviour]` (Động từ nguyên mẫu 2).
  - **Mệnh đề danh từ lồng ghép làm tân ngữ cho giới từ 'of':** `[and how their actions affect other people]` (Cấu trúc Wh-clause: *Cách mà hành vi của họ gây ảnh hưởng đến người khác*).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Diễn giải & Mở rộng chi tiết (Explanatory Paraphrase / Elaboration).**
  - *Mối nối với câu trước:* Câu liền trước nêu nguyên nhân vắn tắt: *"due to the lack of rehabilitation whilst in prison"*. Câu này dùng `[In other words]` để bóc tách xem cụ thể "thiếu cải tạo" nghĩa là gì: không được học nghề mới + không được giáo dục đạo đức để hiểu nỗi đau của nạn nhân.
  - *Kỹ thuật liên kết từ vựng:* Cụm từ `[offenders]` và `[their future]` quy chiếu trực tiếp về danh từ `[first-time offenders]` ở câu trước.
- 💡 **Công thức ghép câu:** `In other words, S_main + are not given [Opportunity] to V1 or V2 and [Wh-clause: how S + V].`

---

#### 📌 Câu dài 2 (Thân bài 1 - Câu điều kiện hoàn cảnh đưa đến hệ quả bắt buộc):
> *"When faced with the inability to earn a regular livelihood, former convicts frequently find themselves driven back into unlawful activities simply to survive."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Mệnh đề trạng ngữ rút gọn bị động:** `[When faced with the inability to earn a regular livelihood]` (Rút gọn từ *When they are faced with...*).
  - **Mệnh đề chính:** `[former convicts]` (Chủ ngữ chính S_main) + `[frequently find themselves]` (Vị ngữ phản thân) + `[driven back into unlawful activities]` (Phân từ quá khứ V-ed chỉ sự ép buộc) + `[simply to survive]` (Cụm động từ nguyên mẫu chỉ mục đích cùng đường).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Nhân quả dồn dập (Direct Cause & Effect Progression).**
  - *Mối nối với câu trước:* Câu trước nêu thực trạng: *"having a criminal record which makes it exceedingly difficult to find a job"*. Câu này móc xích bằng cụm danh từ tóm tắt `[the inability to earn a regular livelihood]` để chỉ ra hệ quả đường cùng: khi không có việc làm $\rightarrow$ buộc phải đi trộm cướp để sinh tồn.
  - *Kỹ thuật liên kết từ vựng (Synonym Chain):* Tác giả thay thế cụm từ `[criminals]` ở các câu trước bằng từ vựng học thuật đồng nghĩa `[former convicts]` (cựu tù nhân) để tránh lỗi lặp từ (Lexical Resource).
- 💡 **Công thức ghép câu:** `When faced with [Obstacle/Inability], S_main + find themselves driven into [Action] simply to + V_inf.`""",

    "task2/advantages_disadvantages/Sample_01_One_Global_Language.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ 'On the other hand' để chuyển hướng toàn bài và mệnh đề phân từ loại trừ chi phí.

---

#### 📌 Câu dài 1 (Thân bài 1 - Tiền đề thuận lợi + Mệnh đề kép + Phân từ rút gọn triệt tiêu chi phí):
> *"With no language barriers, businesses could easily expand overseas and operate with far greater efficiency, completely eliminating the considerable financial expenditure previously allocated to translation and interpreting services."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm giới từ chỉ tiền đề thuận lợi:** `[With no language barriers]` (Với việc không còn rào cản ngôn ngữ).
  - **Mệnh đề chính với Vị ngữ kép:** `[businesses]` (Chủ ngữ S_main) + `[could easily expand overseas]` (Vị ngữ 1) + `[and operate with far greater efficiency]` (Vị ngữ 2).
  - **Mệnh đề phân từ hiện tại chỉ kết quả tự nhiên (Resulting Participle):** `[completely eliminating the considerable financial expenditure]` (Rút gọn từ *which would completely eliminate...*).
  - **Cụm phân từ quá khứ bổ nghĩa cho danh từ:** `[previously allocated to translation and interpreting services]`.
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Phát triển luận điểm từ tiền đề (Logical Consequence / Elaboration).**
  - *Mối nối với câu trước:* Câu trước nêu lợi ích: *"Another positive aspect would be the promotion of trade"* (Thúc đẩy thương mại). Câu này giải thích cơ chế thúc đẩy thương mại diễn ra như thế nào: bằng cách xóa bỏ rào cản ngôn ngữ $\rightarrow$ mở rộng thị trường và loại bỏ chi phí dịch thuật.
  - *Kỹ thuật liên kết:* Cụm `[With no language barriers]` kế thừa và cụ thể hóa ý "everyone spoke one language" đã nêu ở phần đầu đoạn văn.
- 💡 **Công thức ghép câu:** `With [Advantage/No Barrier], S_main + could V1 and V2, completely V-ing + the Noun previously V-ed to [Sector].`

---

#### 📌 Câu dài 2 (Đầu Thân bài 2 - Câu thông báo chuyển hướng sang mặt đối lập):
> *"On the other hand, there are obvious downsides to having only one global language."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Liên từ tương phản liên đoạn:** `[On the other hand]` (Mặt khác...).
  - **Mệnh đề tồn tại (Existential Clause):** `[there are]` + `[obvious downsides]` (Chủ ngữ thật S_real) + `[to having only one global language]` (Cụm giới từ hạn định).
- **2. 🔗 Phân tích Liên kết với đoạn trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Báo hiệu chuyển dịch lập trường (Macro-level Contrast / Topic Shift).**
  - *Mối nối với đoạn trước:* Thân bài 1 khép lại toàn bộ các ưu điểm (lợi ích giao tiếp, thương mại). Câu này đóng vai trò Topic Sentence của Thân bài 2, dùng cặp liên từ chuẩn mực `[On the other hand]` kết hợp với danh từ đối lập `[downsides]` để chuyển sang phân tích các mặt tiêu cực.
  - *Kỹ thuật liên kết:* Lặp lại cụm từ khóa của đề bài `[having only one global language]` để đảm bảo người đọc và giám khảo luôn thấy bài viết bám sát 100% Task Response.
- 💡 **Công thức ghép câu:** `On the other hand, there are obvious downsides / pitfalls to [V-ing / Noun Phrase].`""",

    "task2/direct_questions/Sample_01_Money_and_Happiness.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững kỹ thuật dùng số đếm liên kết ý (Firstly, Secondly, Finally) kết hợp chêm xen mệnh đề lựa chọn 'whether... or...'.

---

#### 📌 Câu dài 1 (Thân bài 2 - Mệnh đề danh động từ + Mệnh đề lựa chọn chêm xen + Mệnh đề quan hệ):
> *"Finally, having a meaningful purpose in life, whether through engaging work, artistic hobbies, or altruistic contribution to society, brings an enduring feeling of fulfillment that wealth can never purchase."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Trạng từ chỉ thứ tự cuối cùng:** `[Finally]` (Cuối cùng nhưng không kém phần quan trọng).
  - **Chủ ngữ Danh động từ chính:** `[having a meaningful purpose in life]` (Chủ ngữ S_main).
  - **Mệnh đề nhượng bộ lựa chọn chêm xen (Parenthetical Clause):** `[whether through engaging work, artistic hobbies, or altruistic contribution to society]`.
  - **Vị ngữ chính:** `[brings an enduring feeling of fulfillment]` (Mang lại cảm giác thỏa nguyện bền lâu).
  - **Mệnh đề quan hệ xác định làm tân ngữ:** `[that wealth can never purchase]` (Mà của cải không bao giờ có thể mua được).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Liên kết thứ tự chuỗi luận cứ (Sequential Enumeration / Final Argument Hook).**
  - *Mối nối với câu trước:* Thân bài 2 trả lời câu hỏi *"Những yếu tố nào khác tạo nên hạnh phúc?"*. Tác giả xây dựng chuỗi liên kết: *First among these is health* $\rightarrow$ *Another crucial element is fulfilling relationships* $\rightarrow$ và chốt hạ bằng `[Finally]` (Ý thứ ba: Mục đích sống).
  - *Kỹ thuật liên kết đối chiếu (Thematic Resonance):* Cụm từ cuối câu `[that wealth can never purchase]` khéo léo kéo người đọc quay trở lại chủ đề trọng tâm của đề bài là *money vs happiness*, tạo sự kết nối chặt chẽ từ đầu đến cuối bài.
- 💡 **Công thức ghép câu:** `Finally, having [Noun/Trait], whether through [A, B, or C], brings [Emotion] that [Material Thing] can never [Verb].`""",

    "task1/bar_chart/Sample_01_Consumer_Goods_Spending.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ 'Similarly' để liên kết 2 đối tượng có cùng xu hướng và 'Furthermore' để bổ sung nhận xét Overview.

---

#### 📌 Câu dài 1 (Thân bài 1 - Câu liên kết tương đồng số liệu giữa 2 quốc gia):
> *"Similarly, the British outlay on books was higher than the French, at roughly £400,000 and £300,000 respectively."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Trạng từ liên kết tương đồng:** `[Similarly]` (Tương tự như vậy...).
  - **Mệnh đề độc lập chính:** `[the British outlay on books]` (Chủ ngữ S_main) + `[was higher than]` (Động từ & Cấu trúc so sánh hơn) + `[the French]` (Tân ngữ quy chiếu thay cho *the French outlay*).
  - **Cụm trạng ngữ số liệu đối chiếu kèm 'respectively':** `[at roughly £400,000 and £300,000 respectively]` (Lần lượt ở mức 400 nghìn và 300 nghìn bảng).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Liên kết quy luật tương đồng (Comparative Analogy / Pattern Matching).**
  - *Mối nối với câu trước:* Câu liền trước phân tích xe hơi (cars): người Anh chi 450 nghìn bảng so với 400 nghìn bảng của Pháp (Anh cao hơn Pháp). Câu này dùng `[Similarly]` để báo hiệu rằng mặt hàng sách (books) cũng tuân theo đúng quy luật này (Anh tiếp tục chi cao hơn Pháp).
  - *Kỹ thuật tránh lặp từ (Lexical Variation):* Thay vì lặp lại từ *expenditure* ở câu trước, tác giả đổi sang danh từ đồng nghĩa `[outlay]`.
- 💡 **Công thức ghép câu:** `Similarly, the [Country A] outlay on [Item] was higher than the [Country B], at [Số A] and [Số B] respectively.`""",

    "task1/line_graph/Sample_01_Spreads_Consumption.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng cụm trạng từ thời gian bước ngoặt 'From that point onwards' và liên từ tương phản liên đoạn 'In contrast'.

---

#### 📌 Câu dài 1 (Thân bài 1 - Câu mô tả bước ngoặt giao cắt và đỉnh điểm):
> *"From that point onwards, margarine consumption surpassed that of butter and became the primary spread, peaking at over 100 grams in 1991, before witnessing a persistent downward trend to finish at roughly 40 grams in 2007."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm trạng từ mốc thời gian:** `[From that point onwards]` (Kể từ thời điểm đó trở đi).
  - **Mệnh đề chính với Vị ngữ kép:** `[margarine consumption]` (Chủ ngữ S_main) + `[surpassed that of butter]` (Vị ngữ 1) + `[and became the primary spread]` (Vị ngữ 2).
  - **Mệnh đề phân từ hiện tại chỉ đỉnh:** `[peaking at over 100 grams in 1991]`.
  - **Cụm giới từ chuyển tiếp kết thúc chu kỳ:** `[before witnessing a persistent downward trend to finish at roughly 40 grams in 2007]`.
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Móc xích điểm ngoặt thời gian (Turning-point Chronological Hook).**
  - *Mối nối với câu trước:* Câu liền trước mô tả giai đoạn 1981 - 1986 khi butter giảm mạnh còn margarine tăng nhẹ lên 100g (tiến sát nhau). Câu này dùng `[From that point onwards]` để bắt nhịp ngay tại mốc năm 1986 đó, dẫn dắt người đọc chứng kiến khoảnh khắc margarine chính thức vượt mặt butter.
  - *Kỹ thuật thay thế đại từ (Pronoun Substitution):* Cụm từ `[that of butter]` thay thế cho *consumption of butter*, giúp câu thanh thoát và không bị lặp từ.
- 💡 **Công thức ghép câu:** `From that point onwards, [Subject A] surpassed that of [Subject B] and became [Rank], peaking at [Peak] in [Year], before V-ing to finish at [Final Number].`

---

#### 📌 Câu dài 2 (Đầu Thân bài 2 - Câu tương phản giữa hai nhóm đường):
> *"In contrast, low fat and reduced spreads were only introduced in 1996 at around 10 grams."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Liên từ tương phản liên đoạn:** `[In contrast]` (Trái lại...).
  - **Mệnh đề độc lập chính ở thể bị động:** `[low fat and reduced spreads]` (Chủ ngữ S_main) + `[were only introduced]` (Động từ bị động kèm phó từ nhấn mạnh *only*) + `[in 1996]` (Trạng từ thời gian) + `[at around 10 grams]` (Trạng từ số liệu).
- **2. 🔗 Phân tích Liên kết với đoạn trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Tương phản phân đoạn biểu đồ (Macro-level Contrast between Lines).**
  - *Mối nối với đoạn trước:* Thân bài 1 dành trọn vẹn mô tả 2 loại bơ có mặt từ năm 1981 và có xu hướng giảm chung (butter & margarine). Mở đầu Thân bài 2 dùng `[In contrast]` để tạo sự cách biệt rõ ràng với loại bơ thứ 3: xuất hiện muộn hơn hẳn (năm 1996) và có xu hướng tăng ngược lại hoàn toàn.
- 💡 **Công thức ghép câu:** `In contrast, [Category] was only introduced in [Year] at around [Number].`""",

    "task1/pie_chart/Sample_01_Energy_Production_France.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ 'Likewise' kết nối 2 số liệu tăng nhẹ và 'In sharp contrast' để đối chiếu sự tăng - giảm giữa các lát cắt.

---

#### 📌 Câu dài 1 (Thân bài 1 - Câu đối chiếu tương đồng giữa than đá và khí đốt):
> *"Likewise, gas generated 29.63% in 1995, after which it experienced a negligible increase of around 1% to reach 30.31% in 2005."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Trạng từ liên kết tương đồng:** `[Likewise]` (Cũng tương tự như thế...).
  - **Mệnh đề độc lập 1:** `[gas]` (Chủ ngữ S1) + `[generated 29.63% in 1995]` (Động từ & Tỷ lệ mốc 1).
  - **Mệnh đề quan hệ thời gian nối tiếp:** `[after which]` (Sau thời điểm đó thì...) + `[it experienced a negligible increase of around 1%]` (Vị ngữ chỉ mức tăng không đáng kể) + `[to reach 30.31% in 2005]` (Cụm động từ nguyên mẫu chỉ mốc số liệu đạt được).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Liên kết xu hướng tương đồng (Parallel Trend Hook).**
  - *Mối nối với câu trước:* Câu trước phân tích than đá (coal): chiếm 29.80% năm 1995 và tăng nhẹ lên 30.93% năm 2005. Câu này dùng `[Likewise]` để kéo sang khí đốt (gas), cho thấy hai loại nhiên liệu hóa thạch này có hành vi và tỷ trọng gần như y hệt nhau.
  - *Kỹ thuật nối mệnh đề (Relative Connector):* Dùng `[after which]` thay vì chấm câu rồi viết *After that, it experienced...* giúp câu văn trở nên mượt mà, đạt điểm cao về Grammatical Range.
- 💡 **Công thức ghép câu:** `Likewise, [Category] generated [X]% in [Year 1], after which it experienced [Adjective + change] to reach [Y]% in [Year 2].`""",

    "task1/table/Sample_01_Consumer_Spending_Five_Countries.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Cách dùng cụm phân từ 'Turning to' để đổi danh mục khảo sát và mệnh đề quan hệ nơi chốn 'where' đối chiếu hai cực đối lập.

---

#### 📌 Câu dài 1 (Thân bài 2 - Câu chẻ kết hợp cụm chuyển đổi danh mục và đối chiếu nơi chốn):
> *"Turning to the other two categories, Italy was the country which spent the highest proportion on clothing and footwear at 9.00%, in contrast to Sweden, where only 5.40% of expenditure was directed towards this category."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm phân từ chuyển dịch danh mục:** `[Turning to the other two categories]` (Chuyển sang 2 hạng mục còn lại).
  - **Mệnh đề chính dùng cấu trúc Câu chẻ (Cleft Sentence):** `[Italy was the country]` + `[which spent the highest proportion on clothing and footwear at 9.00%]`.
  - **Cụm giới từ đối lập:** `[in contrast to Sweden]` (Trái ngược với Thụy Điển).
  - **Mệnh đề quan hệ nơi chốn:** `[where]` (Tại đó) + `[only 5.40% of expenditure was directed towards this category]` (Chỉ 5.40% chi tiêu được dành cho nhóm này).
- **2. 🔗 Phân tích Liên kết với đoạn trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Chuyển dịch phạm vi phân tích (Topic/Category Transition).**
  - *Mối nối với đoạn trước:* Thân bài 1 đã giải quyết xong hạng mục lớn nhất là Thực phẩm & Thuốc lá. Mở đầu Thân bài 2 dùng `[Turning to the other two categories]` để thông báo cho người đọc biết tác giả đang chuyển sang phân tích 2 cột số liệu còn lại của bảng.
  - *Kỹ thuật tạo cực đối lập:* Ghép nước chi nhiều nhất (Italy - 9%) với nước chi ít nhất (Sweden - 5.4%) vào chung một câu bằng cụm liên kết `[in contrast to... where...]` giúp tạo sự tương phản cực kỳ sắc nét.
- 💡 **Công thức ghép câu:** `Turning to [Remaining Categories], [Country A] was the country which spent the highest on [Item], in contrast to [Country B], where only [Number] was recorded.`""",

    "task1/map/Sample_01_Meadowside_Fonton_Development.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ mốc thời gian 'From... to...' nối tiếp câu chuyện quy hoạch và đại từ liên kết 'at which point'.

---

#### 📌 Câu dài 1 (Overview - Hai thực thể mở rộng + Mệnh đề thời gian 'until' + Mệnh đề hệ quả 'at which point'):
> *"Overall, both Fonton and Meadowside village increased in size over the years until they eventually merged together, at which point Meadowside became a suburb."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Mệnh đề chính:** `[Overall, both Fonton and Meadowside village increased in size over the years]`.
  - **Mệnh đề trạng ngữ chỉ thời gian giới hạn:** `[until they eventually merged together]` (Cho đến khi chúng sáp nhập làm một).
  - **Mệnh đề quan hệ chỉ thời điểm hệ quả:** `[at which point]` (Vào thời điểm đó thì...) + `[Meadowside became a suburb]`.
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Tổng hợp khái quát từ câu mở bài (Intro-to-Overview Logical Synthesis).**
  - *Mối nối với câu trước:* Câu mở đầu (Introduction) chỉ mới giới thiệu tên 2 địa danh và các mốc thời gian từ 1962 đến nay. Câu Overview này lập tức dùng `[Overall]` để tóm lược toàn bộ bức tranh: sự tăng trưởng kích thước $\rightarrow$ dẫn đến sự sáp nhập.
  - *Kỹ thuật liên kết thời gian:* Dùng cụm liên kết `[at which point]` nối liền khoảnh khắc sáp nhập với việc thay đổi chức năng hành chính (trở thành khu ngoại ô).
- 💡 **Công thức ghép câu:** `Overall, both [Entity A and B] increased in size until they merged together, at which point [Entity A] became a [New Status].`""",

    "task1/process/Sample_01_Rainwater_Harvesting_Process.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững kỹ thuật dùng mệnh đề phân từ 'Once filtered' và cụm quy chiếu anaphoric 'From this storage facility' để kết nối các công đoạn xử lý nước.

---

#### 📌 Câu dài 1 (Thân bài 1 - Mệnh đề phân từ nối bước + Mệnh đề thời gian 'until' + Mệnh đề 'where'):
> *"Once filtered, the water continues along underground pipes until it reaches a secure storage tank, where it is held prior to further refinement."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Mệnh đề phân từ hoàn thành rút gọn:** `[Once filtered]` (Rút gọn từ *Once the water has been filtered*).
  - **Mệnh đề chính:** `[the water]` (Chủ ngữ S_main) + `[continues along underground pipes]` (Vị ngữ V_main).
  - **Mệnh đề trạng ngữ chỉ điểm đến thời gian:** `[until it reaches a secure storage tank]`.
  - **Mệnh đề quan hệ nơi chốn:** `[where it is held prior to further refinement]` (Nơi nó được lưu giữ trước khi tiếp tục tinh chế).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Móc xích công đoạn tuần tự (Step-by-step Sequential Linkage).**
  - *Mối nối với câu trước:* Câu trước mô tả nước chảy qua bộ lọc nước: *"The runoff first passes through a specialized water filter designed to remove large debris"*. Câu này lập tức móc xích bằng cụm phân từ `[Once filtered]` (Một khi đã được lọc xong) để kích hoạt ngay công đoạn dẫn nước vào đường ống ngầm.
  - *Kỹ thuật liên kết đỉnh cao:* Chuyển đổi một động từ ở câu trước (*filter*) thành phân từ ở đầu câu sau (*Once filtered*) là kỹ thuật kết nối câu mượt mà nhất trong IELTS Task 1 Process.
- 💡 **Công thức ghép câu:** `Once [V-ed_passive], the [Material] continues along [Route] until it reaches [Destination], where it is [Action performed].`

---

#### 📌 Câu dài 2 (Thân bài 2 - Cụm quy chiếu nơi chốn + Bị động kỹ thuật):
> *"From this storage facility, the water is piped into an adjacent water treatment unit."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm giới từ chỉ xuất phát điểm:** `[From this storage facility]` (Từ bể chứa này...).
  - **Mệnh đề chính ở thể bị động:** `[the water]` (Chủ ngữ S_main) + `[is piped into]` (Động từ bị động: *được bơm qua đường ống vào*) + `[an adjacent water treatment unit]` (Tân ngữ nơi đến).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Quy chiếu đại từ chỉ định (Anaphoric Demonstrative Reference).**
  - *Mối nối với câu trước:* Câu trước kết thúc tại bồn chứa nước (*storage tank*). Câu này mở đầu ngay bằng cụm `[From this storage facility]`, sử dụng đại từ chỉ định `[this]` để nhắc lại bồn chứa ở câu trước, tạo thành một chiếc "cầu nối" đưa dòng chảy của nước sang trạm xử lý tiếp theo.
- 💡 **Công thức ghép câu:** `From this [Facility/Container], the [Substance] is piped / transferred into an adjacent [Next Unit].`""",

    "task1/mixed_chart/Sample_01_Glasgow_Education_Levels.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề & Kỹ Thuật Liên Kết Câu (Sentence Anatomy & Cohesion)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách dùng liên từ 'Meanwhile' đối chiếu nội bộ nhóm tuổi và cụm 'Turning to the pie charts' để đổi góc nhìn từ biểu đồ cột sang biểu đồ tròn.

---

#### 📌 Câu dài 1 (Thân bài 1 - Câu đối chiếu xu hướng bằng 'Meanwhile' + Phân từ sụt giảm mạnh):
> *"Meanwhile, the proportion of individuals with school-level education remained relatively constant at around 20% across most brackets, but plunged to as low as 3% in the over-75 demographic."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Trạng từ liên kết diễn tiến song song:** `[Meanwhile]` (Trong khi đó...).
  - **Mệnh đề độc lập chính với Vị ngữ kép đối lập:**
    - `[the proportion of individuals with school-level education]` (Chủ ngữ S_main).
    - `[remained relatively constant at around 20% across most brackets]` (Vị ngữ 1 chỉ sự ổn định).
    - `[but]` (Liên từ tương phản đẳng lập).
    - `[plunged to as low as 3% in the over-75 demographic]` (Vị ngữ 2 với động từ mạnh *plunged* chỉ sự sụt giảm chạm đáy).
- **2. 🔗 Phân tích Liên kết với câu trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Chuyển dịch đối tượng khảo sát nội bộ (Internal Category Shift / Co-occurrence).**
  - *Mối nối với câu trước:* Hai câu trước đã phân tích 2 nhóm học vấn cực đoan (nhóm có bằng đại học và nhóm không có bằng cấp). Tác giả dùng `[Meanwhile]` để kéo sự chú ý sang nhóm học vấn thứ ba còn lại (nhóm có bằng phổ thông).
  - *Kỹ thuật liên kết từ vựng:* Cụm từ `[over-75 demographic]` đồng nghĩa và móc xích chặt chẽ với cụm `[oldest cohort]` ở câu liền trước.
- 💡 **Công thức ghép câu:** `Meanwhile, the proportion of [Group] remained relatively constant at [X]%, but plunged to as low as [Y]% in [Specific Segment].`

---

#### 📌 Câu dài 2 (Đầu Thân bài 2 - Chuyển sang biểu đồ tròn):
> *"Turning to the pie charts, the distribution between genders was exceptionally balanced."*

- **1. Phân tích các Mệnh đề trong câu (Intra-sentence Clauses):**
  - **Cụm phân từ chuyển tiếp biểu đồ:** `[Turning to the pie charts]` (Chuyển sang các biểu đồ tròn...).
  - **Mệnh đề chính:** `[the distribution between genders]` (Chủ ngữ S_main) + `[was]` (Động từ to be) + `[exceptionally balanced]` (Bổ ngữ tính từ chỉ sự cân bằng vượt bậc).
- **2. 🔗 Phân tích Liên kết với đoạn trước (Inter-sentence Cohesion):**
  - *Kiểu liên kết:* **Chuyển giao biểu đồ vĩ mô (Macro Chart Transition).**
  - *Mối nối với đoạn trước:* Thân bài 1 đã hoàn thành trọn vẹn việc phân tích Biểu đồ cột (Bar chart theo độ tuổi). Mở đầu Thân bài 2 dùng công thức kinh điển `[Turning to the pie charts]` để thông báo dứt khoát rằng tác giả chuyển sang khai thác dữ liệu giới tính của Biểu đồ tròn.
- 💡 **Công thức ghép câu:** `Turning to [Second Chart], the [Aspect/Distribution] was exceptionally [Adjective: balanced / uniform / disparate].`"""
}

def update_file(rel_path, new_analysis):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern: Replace the existing '### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề...' block with the new enriched one
    pattern = r"### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề.*?(?=---\s*\n\s*## 3\. 💎 Kho Từ Vựng|\Z)"
    
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, new_analysis + "\n\n", content, flags=re.DOTALL)
    else:
        # If not found, insert right before ## 3
        idx = content.find("## 3. 💎 Kho Từ Vựng")
        if idx != -1:
            new_content = content[:idx] + new_analysis + "\n\n---\n\n" + content[idx:]
        else:
            new_content = content + "\n\n" + new_analysis

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated with Cohesion: {rel_path}")

def main():
    for rel_path, analysis in clause_cohesion_data.items():
        update_file(rel_path, analysis)

if __name__ == "__main__":
    main()
