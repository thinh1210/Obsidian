import os
import re

BASE_DIR = "/home/thinh/Obsidian/English/Writing"

# Clause breakdowns mapped by relative file path
clause_data = {
    "task2/agree_disagree/Sample_01_Overweight_Physical_Education.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Đọc và nắm bắt cấu trúc tầng bậc của các câu dài ngay sau bài viết mẫu để hiểu cách vận hành của các mệnh đề và tự áp dụng.

#### 📌 Câu dài 1 (Mở bài - Mệnh đề quan hệ + Bị động khách quan + Mệnh đề đối lập):
> *"Owing to the problems which a growing population of overweight people cause for the health care system, it is thought that the key to solving this issue is to have more sport and exercise in schools."*

- **1. Cụm giới từ chỉ nguyên nhân (Prepositional Phrase):**
  - `[Owing to the problems]` (Giới từ nguyên nhân: *Do bởi các vấn đề*).
- **2. Mệnh đề quan hệ xác định lồng ghép (Defining Relative Clause):**
  - `[which]` (Đại từ quan hệ làm tân ngữ thay cho *problems*) + `[a growing population of overweight people]` (Chủ ngữ S_rel) + `[cause for the health care system]` (Động từ & Giới từ V_rel).
  - *Ý nghĩa:* Làm rõ vấn đề này do ai gây ra và gây ra cho cơ quan nào.
- **3. Mệnh đề chính dùng chủ ngữ giả (Main Clause with Dummy Subject):**
  - `[it]` (Chủ ngữ giả) + `[is thought]` (Động từ to be & Phân từ bị động khách quan: *người ta cho rằng*).
- **4. Mệnh đề danh từ làm chủ ngữ thật (Noun Clause với 'that'):**
  - `[that]` (Liên từ) + `[the key to solving this issue]` (Chủ ngữ S_sub) + `[is]` (Động từ V_sub) + `[to have more sport and exercise in schools]` (Bổ ngữ nguyên mẫu).
- 💡 **Công thức ghép câu:** `Owing to [Noun] which S_rel + V_rel, it is thought that [Noun Clause: that S + is to V].`

---

#### 📌 Câu dài 2 (Thân bài 1 - Mệnh đề chính + Mệnh đề quan hệ lồng ghép kép):
> *"At the moment, the average child in the West does sport possibly twice a week, which is not enough to counteract their otherwise sedentary lifestyle that comes from many hours each day of sitting at a desk for their lessons."*

- **1. Mệnh đề độc lập chính (Main Clause):**
  - `[At the moment]` (Trạng ngữ thời gian) + `[the average child in the West]` (Chủ ngữ chính S_main) + `[does sport]` (Động từ & Tân ngữ V_main + O_main) + `[possibly twice a week]` (Trạng từ tần suất).
  - *Ý nghĩa:* Đưa ra con số thực tế về thời lượng vận động của trẻ em.
- **2. Mệnh đề quan hệ không xác định 1 (Non-defining Relative Clause):**
  - `[which]` (Đại từ quan hệ thay thế cho toàn bộ sự việc ở mệnh đề chính) + `[is not enough]` (Động từ to be & Tính từ) + `[to counteract their otherwise sedentary lifestyle]` (Cụm động từ nguyên mẫu chỉ mục đích).
  - *Ý nghĩa:* Bình luận rằng mức độ vận động đó là không đủ để bù đắp lối sống lười vận động.
- **3. Mệnh đề quan hệ xác định 2 (Defining Relative Clause lồng trong mệnh đề 1):**
  - `[that]` (Đại từ quan hệ thay thế cho *sedentary lifestyle*) + `[comes from]` (Động từ chỉ nguồn gốc) + `[many hours each day of sitting at a desk for their lessons]` (Cụm danh từ chỉ nguyên nhân).
  - *Ý nghĩa:* Giải thích căn nguyên của lối sống ngồi nhiều (do phải ngồi học liên tục).
- 💡 **Công thức ghép câu:** `S_main + V_main + O_main, which is not enough to + V_inf + Noun + that comes from + [Nguyên nhân].`""",

    "task2/discuss_both_views/Sample_01_University_vs_Work_Experience.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Phân tích cấu trúc câu đa tầng ngay dưới bài viết mẫu để nắm vững cách mở rộng ý và ghép mệnh đề song hành.

#### 📌 Câu dài 1 (Thân bài 1 - Cấu trúc Not only... but + Động từ nhấn mạnh + Mệnh đề quan hệ 'which'):
> *"Not only that, but academia does promote the development of useful skills, not just academic knowledge, for example analytical thinking, research skills and intellectual curiosity, which are valuable transferable skills."*

- **1. Thành phần nối chuyển tiếp (Transition):**
  - `[Not only that, but]` (Cụm liên từ kết hợp nhấn mạnh ý bổ sung).
- **2. Mệnh đề chính với trợ động từ 'does' nhấn mạnh (Main Clause with Emphatic 'does'):**
  - `[academia]` (Chủ ngữ chính S_main) + `[does promote]` (Trợ động từ *does* mang sắc thái khẳng định mạnh mẽ + Động từ nguyên mẫu) + `[the development of useful skills]` (Cụm danh từ tân ngữ O_main).
- **3. Cụm danh từ đối chiếu bổ trợ (Parenthetical Noun Phrase):**
  - `[not just academic knowledge, for example analytical thinking, research skills and intellectual curiosity]` (Cụm danh từ liệt kê cụ thể các kỹ năng).
- **4. Mệnh đề quan hệ không xác định (Non-defining Relative Clause):**
  - `[which]` (Đại từ quan hệ thay thế cho 3 kỹ năng được liệt kê) + `[are]` (Động từ liên kết) + `[valuable transferable skills]` (Bổ ngữ chỉ bản chất: *những kỹ năng chuyển đổi vô giá*).
- 💡 **Công thức ghép câu:** `Not only that, but S_main + does V_main + Noun_phrase, for example [A, B and C], which are [Tính từ + Danh từ].`

---

#### 📌 Câu dài 2 (Thân bài 2 - Chủ ngữ là V-ing song hành + So sánh hơn + Rút gọn thời gian):
> *"For instance, for a corporate management position, having experience of managing others, running projects, delegating tasks and strong emotional intelligence is of more importance than the theory of management with no real hands-on experience when fresh out of university."*

- **1. Cụm trạng ngữ bối cảnh (Adverbial Prepositional Phrases):**
  - `[For instance]` (Trạng từ liên kết ví dụ) + `[for a corporate management position]` (Giới từ chỉ vị trí công việc).
- **2. Mệnh đề chính với Chủ ngữ phức hợp danh động từ (Complex Gerund Subject):**
  - `[having experience of managing others, running projects, delegating tasks and strong emotional intelligence]` (Chủ ngữ chính dạng V-ing dài bao gồm 4 yếu tố thực chiến song hành).
  - `[is of more importance than]` (Cấu trúc vị ngữ trang trọng: *be of importance = be important* ở dạng so sánh hơn).
  - `[the theory of management with no real hands-on experience]` (Tân ngữ đối chiếu so sánh).
- **3. Mệnh đề trạng ngữ rút gọn chỉ thời gian (Elliptical Time Clause):**
  - `[when]` (Liên từ thời gian) + `[fresh out of university]` (Rút gọn từ *when they are fresh out of university* - khi mới chân ướt chân ráo ra trường).
- 💡 **Công thức ghép câu:** `For a [Position], having experience of [V-ing 1, V-ing 2, and Noun] is of more importance than [Đối tượng đối chiếu] when [Rút gọn tính từ].`""",

    "task2/problem_solution/Sample_01_Criminal_Reoffending.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách xây dựng mệnh đề bị động kép và mệnh đề trạng ngữ chỉ điều kiện hoàn cảnh.

#### 📌 Câu dài 1 (Thân bài 1 - Mệnh đề trạng ngữ rút gọn bị động + Ngoại động từ chỉ sự xô đẩy):
> *"When faced with the inability to earn a regular livelihood, former convicts frequently find themselves driven back into unlawful activities simply to survive."*

- **1. Mệnh đề trạng ngữ rút gọn dạng bị động (Elliptical Passive Adverbial Clause):**
  - `[When]` (Liên từ thời gian) + `[faced with the inability to earn a regular livelihood]` (Rút gọn từ *When they are faced with...* - Khi đối mặt với việc không có kế sinh nhai).
- **2. Mệnh đề độc lập chính (Main Clause):**
  - `[former convicts]` (Chủ ngữ chính S_main: *những người từng thụ án tù*).
  - `[frequently find themselves]` (Trạng từ tần suất + Động từ phản thân: *thường thấy chính mình...*).
  - `[driven back into unlawful activities]` (Phân từ quá khứ V-ed đóng vai trò bổ ngữ tân ngữ chỉ trạng thái bị xô đẩy trở lại con đường phạm pháp).
  - `[simply to survive]` (Cụm động từ nguyên mẫu chỉ mục đích tối hậu: *chỉ để sinh tồn*).
- 💡 **Công thức ghép câu:** `When faced with [Noun/Inability], S_main + find themselves + V-ed_passive + simply to + V_inf.`

---

#### 📌 Câu dài 2 (Thân bài 2 - Mệnh đề độc lập + Mệnh đề phụ mục đích + Mệnh đề thời gian):
> *"One way to tackle this is to ensure that all criminals entering prison are given the chance to retrain with useful skills which will hopefully ensure them a job after they have served their sentence."*

- **1. Mệnh đề chính (Main Clause):**
  - `[One way to tackle this]` (Cụm chủ ngữ chính S_main) + `[is]` (Động từ V_main) + `[to ensure]` (Bổ ngữ nguyên mẫu).
- **2. Mệnh đề danh từ làm tân ngữ (Noun Clause với 'that'):**
  - `[that]` (Liên từ) + `[all criminals entering prison]` (Chủ ngữ con với phân từ hiện tại *entering prison* rút gọn cho *who enter prison*) + `[are given the chance to retrain with useful skills]` (Vị ngữ bị động).
- **3. Mệnh đề quan hệ xác định (Defining Relative Clause):**
  - `[which]` (Đại từ quan hệ bổ nghĩa cho *useful skills*) + `[will hopefully ensure them a job]` (Vị ngữ tương lai đơn kèm tân ngữ trực tiếp và gián tiếp).
- **4. Mệnh đề trạng ngữ chỉ thời gian hoàn thành (Time Clause với 'after'):**
  - `[after]` (Liên từ thời gian) + `[they]` (S) + `[have served their sentence]` (Vị ngữ hiện tại hoàn thành: *sau khi đã hoàn thành thời gian thụ án*).
- 💡 **Công thức ghép câu:** `One way to tackle [Issue] is to ensure that S_sub + are given [Chance] which will V_inf after they have + V-ed.`""",

    "task2/advantages_disadvantages/Sample_01_One_Global_Language.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Phân tích cấu trúc câu điều kiện loại 2 giả định và câu chứa phân từ rút gọn loại trừ chi phí.

#### 📌 Câu dài 1 (Mở bài - Mệnh đề danh từ lồng mệnh đề quan hệ không xác định):
> *"It is thought by some people that English, which is now the most widely spoken language in the world, may one day predominate over all other languages and result in their eventual disappearance."*

- **1. Mệnh đề chính dùng chủ ngữ giả (Main Clause with Dummy Subject):**
  - `[It]` (Chủ ngữ giả) + `[is thought by some people]` (Động từ bị động kèm tác nhân).
- **2. Mệnh đề danh từ làm chủ ngữ thật (Noun Clause với 'that'):**
  - `[that]` (Liên từ) + `[English]` (Chủ ngữ của mệnh đề con S_sub).
- **3. Mệnh đề quan hệ không xác định chêm xen (Embedded Non-defining Relative Clause):**
  - `[which is now the most widely spoken language in the world]` (Bổ sung thông tin về vị thế của tiếng Anh mà không làm đứt đoạn câu).
- **4. Vị ngữ kép của mệnh đề danh từ (Compound Predicate of Noun Clause):**
  - `[may one day predominate over all other languages]` (Vị ngữ 1 với động từ khuyết thiếu *may*) + `[and]` (Liên từ đẳng lập) + `[result in their eventual disappearance]` (Vị ngữ 2 chỉ hệ quả sau cùng).
- 💡 **Công thức ghép câu:** `It is thought that [Subject], which is now [Fact], may one day V1 and result in [Noun Phrase].`

---

#### 📌 Câu dài 2 (Thân bài 1 - Giới từ nguyên nhân + Mệnh đề chính + Phân từ hiện tại rút gọn chỉ kết quả):
> *"With no language barriers, businesses could easily expand overseas and operate with far greater efficiency, completely eliminating the considerable financial expenditure previously allocated to translation and interpreting services."*

- **1. Cụm giới từ chỉ điều kiện tiền đề (Prepositional Phrase of Condition):**
  - `[With no language barriers]` (Với việc không còn rào cản ngôn ngữ).
- **2. Mệnh đề độc lập chính (Main Clause):**
  - `[businesses]` (Chủ ngữ chính S_main) + `[could easily expand overseas]` (Vị ngữ 1) + `[and]` + `[operate with far greater efficiency]` (Vị ngữ 2).
- **3. Mệnh đề phân từ hiện tại chỉ kết quả tự nhiên (Present Participle of Result):**
  - `[completely eliminating]` (Trạng từ + V-ing rút gọn từ *which completely eliminates*) + `[the considerable financial expenditure]` (Cụm tân ngữ chi phí tài chính đáng kể).
- **4. Cụm phân từ quá khứ rút gọn bổ nghĩa cho danh từ (Past Participle Phrase):**
  - `[previously allocated to translation and interpreting services]` (Rút gọn từ *which was previously allocated to...*).
- 💡 **Công thức ghép câu:** `With [Condition], S_main + could V1 and V2, completely V-ing + the Noun previously V-ed to [Field].`""",

    "task2/direct_questions/Sample_01_Money_and_Happiness.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Học cách viết mệnh đề nhượng bộ kép và liên từ phụ thuộc 'whether... or...' đan cài trong câu dài.

#### 📌 Câu dài 1 (Thân bài 2 - Mệnh đề danh động từ làm chủ ngữ + Mệnh đề nhượng bộ lồng ghép + Mệnh đề quan hệ):
> *"Finally, having a meaningful purpose in life, whether through engaging work, artistic hobbies, or altruistic contribution to society, brings an enduring feeling of fulfillment that wealth can never purchase."*

- **1. Chủ ngữ chính dạng Danh động từ (Gerund Phrase as Subject):**
  - `[Finally]` (Trạng từ liên kết chuyển ý) + `[having a meaningful purpose in life]` (Chủ ngữ chính S_main).
- **2. Cụm liên từ nhượng bộ lựa chọn chêm xen (Parenthetical Clause with 'whether... or...'):**
  - `[whether through engaging work, artistic hobbies, or altruistic contribution to society]` (Dù là thông qua công việc cuốn hút, sở thích nghệ thuật, hay sự cống hiến vị tha).
  - *Chức năng:* Bao quát toàn diện các khía cạnh tạo nên mục đích sống mà không làm câu bị gãy.
- **3. Vị ngữ chính (Main Predicate):**
  - `[brings]` (Động từ chia số ít theo gerund) + `[an enduring feeling of fulfillment]` (Cụm danh từ tân ngữ O_main: *cảm giác thỏa nguyện bền lâu*).
- **4. Mệnh đề quan hệ xác định (Defining Relative Clause):**
  - `[that]` (Đại từ quan hệ làm tân ngữ) + `[wealth]` (Chủ ngữ S_rel) + `[can never purchase]` (Động từ V_rel: *mà tiền của không bao giờ có thể mua được*).
- 💡 **Công thức ghép câu:** `Having [Quality/Goal], whether through [A, B, or C], brings [Positive State] that [Resource] can never [Verb].`""",

    "task1/bar_chart/Sample_01_Consumer_Goods_Spending.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Học cách so sánh đối chiếu giữa 2 quốc gia và sử dụng phân từ hiện tại tạo nhận xét số liệu đặc biệt trong Task 1.

#### 📌 Câu dài 1 (Overview - Cấu trúc đối chiếu song hành 'whereas' + So sánh hơn nhất):
> *"Both the British and the French spent most of their money on cars whereas the least amount of money was spent on perfume in the UK compared to cameras in France."*

- **1. Mệnh đề độc lập thứ nhất (First Independent Clause):**
  - `[Both the British and the French]` (Chủ ngữ kép S1) + `[spent]` (Động từ V1) + `[most of their money]` (Tân ngữ so sánh hơn nhất) + `[on cars]` (Cụm giới từ chỉ danh mục).
- **2. Liên từ chỉ sự tương phản (Subordinating Conjunction):**
  - `[whereas]` (Trong khi đó - tạo độ cân xứng tuyệt đối giữa 2 vế đối chiếu).
- **3. Mệnh đề độc lập thứ hai dạng bị động (Second Independent Clause in Passive Voice):**
  - `[the least amount of money]` (Chủ ngữ S2 chỉ số lượng ít nhất) + `[was spent]` (Động từ bị động V2) + `[on perfume in the UK compared to cameras in France]` (Cụm so sánh đối chứng 2 quốc gia).
- 💡 **Công thức ghép câu:** `Both [A and B] spent the most on [Item 1], whereas the least was spent on [Item 2 in A] compared to [Item 3 in B].`

---

#### 📌 Câu dài 2 (Thân bài 1 - Hai mệnh đề số liệu đối lập + Phân từ rút gọn chỉ nhận xét duy nhất):
> *"In the UK, expenditure on computers reached roughly £350,000, while the figure for France was slightly lower, at around £380,000, making it the only category where France spent more than the UK."*

- **1. Mệnh đề thứ nhất (Clause 1 - Báo cáo số liệu UK):**
  - `[In the UK]` (Trạng ngữ nơi chốn) + `[expenditure on computers]` (Chủ ngữ S1) + `[reached]` (Động từ) + `[roughly £350,000]` (Cụm số liệu xấp xỉ).
- **2. Mệnh đề phụ tương phản (Adverbial Clause với 'while' - Báo cáo số liệu Pháp):**
  - `[while]` (Liên từ tương phản) + `[the figure for France]` (Chủ ngữ S2 thay cho *expenditure*) + `[was slightly lower, at around £380,000]` (Vị ngữ số liệu).
- **3. Mệnh đề phân từ hiện tại chỉ nhận xét tổng kết (Present Participle of Comment):**
  - `[making it]` (Phân từ V-ing rút gọn cho *which made it*) + `[the only category]` (Tân ngữ bổ ngữ: *hạng mục duy nhất*) + `[where France spent more than the UK]` (Mệnh đề quan hệ nơi chốn bổ nghĩa cho *category*).
- 💡 **Công thức ghép câu:** `In [Country A], expenditure on [Item] reached [Số 1], while the figure for [Country B] was [Số 2], making it the only category where [B spent more than A].`""",

    "task1/line_graph/Sample_01_Spreads_Consumption.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách kết hợp mệnh đề xu hướng, điểm vượt mặt, mốc đạt đỉnh và phân từ kết thúc thời kỳ trong Line Graph.

#### 📌 Câu dài 1 (Thân bài 1 - Xu hướng vượt mặt + Phân từ đạt đỉnh + Phân từ khép lại thời kỳ):
> *"From that point onwards, margarine consumption surpassed that of butter and became the primary spread, peaking at over 100 grams in 1991, before witnessing a persistent downward trend to finish at roughly 40 grams in 2007."*

- **1. Mệnh đề chính với Vị ngữ kép (Main Clause with Compound Predicate):**
  - `[From that point onwards]` (Trạng từ thời gian: *Từ thời điểm đó trở đi*).
  - `[margarine consumption]` (Chủ ngữ S_main).
  - `[surpassed that of butter]` (Vị ngữ 1: *vượt qua mức tiêu thụ của bơ* - dùng *that of* tránh lặp từ).
  - `[and became the primary spread]` (Vị ngữ 2: *và trở thành loại bơ quết bánh chủ đạo*).
- **2. Mệnh đề phân từ hiện tại chỉ điểm cực đại (Participle Phrase of Peak):**
  - `[peaking at over 100 grams in 1991]` (Rút gọn từ *and it peaked at...*).
- **3. Cụm giới từ chỉ sự chuyển tiếp và kết thúc (Prepositional Time Phrase with 'before'):**
  - `[before witnessing a persistent downward trend]` (Trước khi chứng kiến một xu hướng giảm bền bỉ).
  - `[to finish at roughly 40 grams in 2007]` (Cụm động từ nguyên mẫu chỉ mốc số liệu kết thúc chu kỳ).
- 💡 **Công thức ghép câu:** `From [Year], S_main + surpassed that of [X] and became [Leader], peaking at [Peak Number] in [Year], before witnessing a downward trend to finish at [Final Number] in [Final Year].`""",

    "task1/pie_chart/Sample_01_Energy_Production_France.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Cách biểu đạt hai mệnh đề có xu hướng đối lập kịch liệt (plummeted vs saw its share swell) trong biểu đồ tròn.

#### 📌 Câu dài 1 (Thân bài 2 - Chuyển danh mục + Mệnh đề đẳng lập + Trạng từ đối lập mạnh mẽ):
> *"With regards to the remaining energy sources, petrol began as the second most prominent fuel at 29.27% in 1995, but plummeted significantly to 19.55% a decade later."*

- **1. Cụm từ dẫn dắt chuyển danh mục (Signposting Prepositional Phrase):**
  - `[With regards to the remaining energy sources]` (Xét đến các nguồn năng lượng còn lại).
- **2. Mệnh đề chính với 2 động từ tương phản nối bằng 'but' (Compound Main Clause):**
  - `[petrol]` (Chủ ngữ chính S_main).
  - `[began as the second most prominent fuel at 29.27% in 1995]` (Vị ngữ 1 nêu vị thế khởi đầu: *bắt đầu với tư cách là nguồn nhiên liệu nổi bật thứ hai*).
  - `[but]` (Liên từ nối tương phản).
  - `[plummeted significantly to 19.55% a decade later]` (Vị ngữ 2 với động từ mạnh *plummeted* chỉ sự tụt giảm nghiêm trọng sau 1 thập kỷ).
- 💡 **Công thức ghép câu:** `With regards to [Category], S_main + began as [Rank] at [Số 1] in [Year 1], but plummeted significantly to [Số 2] a decade later.`""",

    "task1/table/Sample_01_Consumer_Spending_Five_Countries.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Cách sử dụng câu chẻ nhấn mạnh (Cleft sentence) kết hợp đối chiếu địa lý bằng mệnh đề quan hệ nơi chốn 'where'.

#### 📌 Câu dài 1 (Thân bài 2 - Cấu trúc câu chẻ + Mệnh đề quan hệ 'which' + Cụm đối chiếu 'in contrast to' + Mệnh đề 'where'):
> *"Turning to the other two categories, Italy was the country which spent the highest proportion on clothing and footwear at 9.00%, in contrast to Sweden, where only 5.40% of expenditure was directed towards this category."*

- **1. Cụm phân từ chuyển tiếp (Signposting Transition Phrase):**
  - `[Turning to the other two categories]` (Chuyển sang 2 hạng mục còn lại).
- **2. Mệnh đề chính dùng cấu trúc Câu chẻ (Cleft Sentence Main Clause):**
  - `[Italy]` (Chủ ngữ được nhấn mạnh) + `[was the country]` (Vị ngữ to be) + `[which spent the highest proportion on clothing and footwear at 9.00%]` (Mệnh đề quan hệ xác định nhấn mạnh Ý là quốc gia chi nhiều nhất).
- **3. Cụm từ tương phản (Contrastive Prepositional Phrase):**
  - `[in contrast to Sweden]` (Trái ngược hoàn toàn với Thụy Điển).
- **4. Mệnh đề quan hệ nơi chốn không xác định (Non-defining Relative Clause với 'where'):**
  - `[where]` (Trạng từ quan hệ thay thế cho Thụy Điển) + `[only 5.40% of expenditure]` (Chủ ngữ S_rel) + `[was directed towards this category]` (Vị ngữ bị động: *được hướng về danh mục này*).
- 💡 **Công thức ghép câu:** `Turning to [Category], [Country A] was the country which spent the highest on [Item] at [Số 1], in contrast to [Country B], where only [Số 2] was directed towards this category.`""",

    "task1/map/Sample_01_Meadowside_Fonton_Development.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Nắm vững cấu trúc câu phức chỉ sự sáp nhập địa lý và phân từ hoàn tất biến đổi cảnh quan nông thôn thành đô thị.

#### 📌 Câu dài 1 (Overview - Hai chủ ngữ sáp nhập + Mệnh đề thời gian 'until' + Mệnh đề quan hệ 'at which point'):
> *"Overall, both Fonton and Meadowside village increased in size over the years until they eventually merged together, at which point Meadowside became a suburb."*

- **1. Mệnh đề chính (Main Clause):**
  - `[Overall]` (Trạng từ khái quát) + `[both Fonton and Meadowside village]` (Chủ ngữ kép S_main) + `[increased in size]` (Động từ & Cụm giới từ V_main) + `[over the years]` (Cụm trạng từ thời gian).
- **2. Mệnh đề trạng ngữ chỉ thời gian giới hạn (Adverbial Clause với 'until'):**
  - `[until]` (Liên từ: *cho đến khi*) + `[they]` (Chủ ngữ quy chiếu) + `[eventually merged together]` (Động từ sáp nhập).
- **3. Mệnh đề quan hệ chỉ mốc thời điểm hệ quả (Relative Clause với 'at which point'):**
  - `[at which point]` (Cụm đại từ quan hệ: *vào thời điểm đó thì...*) + `[Meadowside]` (Chủ ngữ) + `[became a suburb]` (Động từ và bổ ngữ: *trở thành khu ngoại ô*).
- 💡 **Công thức ghép câu:** `Overall, both [A and B] increased in size until they merged together, at which point [A] became a suburb.`

---

#### 📌 Câu dài 2 (Thân bài 2 - Chủ ngữ liệt kê 3 công trình + Bị động quá khứ + Phân từ biến đổi diện mạo):
> *"Additionally, a new shopping mall, an expansive leisure complex, and a large regional hospital were erected on former arable land, completely transforming the rural landscape into a modern suburban hub."*

- **1. Mệnh đề chính ở thể bị động với chủ ngữ bộ ba (Passive Main Clause with Triple Subjects):**
  - `[Additionally]` (Liên từ bổ sung) + `[a new shopping mall, an expansive leisure complex, and a large regional hospital]` (Cụm 3 danh từ chủ ngữ) + `[were erected]` (Động từ bị động: *được dựng lên*) + `[on former arable land]` (Cụm giới từ chỉ vị trí: *trên đất nông nghiệp cũ*).
- **2. Mệnh đề phân từ hiện tại chỉ kết quả biến đổi toàn diện (Present Participle of Complete Transformation):**
  - `[completely transforming]` (Trạng từ + V-ing rút gọn từ *which completely transformed*) + `[the rural landscape]` (Tân ngữ cảnh quan nông thôn) + `[into a modern suburban hub]` (Giới từ đích đến: *thành một trung tâm ngoại ô hiện đại*).
- 💡 **Công thức ghép câu:** `Additionally, [Facility 1, 2, and 3] were erected on [Land], completely transforming [Original State] into [New State].`""",

    "task1/process/Sample_01_Rainwater_Harvesting_Process.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Học cách kết nối các bước tuần tự trong quy trình bằng phân từ hoàn thành 'thereby V-ing' và mệnh đề thời gian 'once'.

#### 📌 Câu dài 1 (Thân bài 2 - Thể bị động kỹ thuật + Cụm chỉ mục đích + Phân từ 'thereby making'):
> *"At this critical stage of the operation, specific chemical compounds are introduced into the water to eliminate any remaining bacteria and contaminants, thereby making it completely safe and fit for human consumption."*

- **1. Cụm trạng ngữ thời điểm quy trình (Process Stage Adverbial Phrase):**
  - `[At this critical stage of the operation]` (Tại giai đoạn then chốt này của quy trình).
- **2. Mệnh đề độc lập chính dạng bị động kỹ thuật (Passive Technical Main Clause):**
  - `[specific chemical compounds]` (Chủ ngữ chính S_main: *các hợp chất hóa học đặc thù*) + `[are introduced into the water]` (Vị ngữ bị động: *được châm vào nước*) + `[to eliminate any remaining bacteria and contaminants]` (Cụm động từ nguyên mẫu chỉ mục đích: *nhằm tiêu diệt vi khuẩn và tạp chất còn sót lại*).
- **3. Mệnh đề phân từ hiện tại chỉ kết quả đạt chuẩn (Present Participle of Result với 'thereby'):**
  - `[thereby making it completely safe and fit for human consumption]` (Trạng từ *thereby* + V-ing: *bằng cách đó khiến nó hoàn toàn an toàn và đạt chuẩn tiêu dùng cho con người*).
- 💡 **Công thức ghép câu:** `At this stage, [Chemicals/Agents] are introduced to eliminate [Impurities], thereby making it completely [Adjectives: safe and fit for use].`""",

    "task1/mixed_chart/Sample_01_Glasgow_Education_Levels.md": """### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề Các Câu Dài & Khó Trong Bài (Clause Anatomy Breakdown)

> [!NOTE] Mục tiêu học tập
> Nắm vững cách đối chiếu số liệu đa chiều kết hợp mệnh đề quan hệ nơi chốn 'where' và phân từ 'resulting in' trong biểu đồ kết hợp.

#### 📌 Câu dài 1 (Thân bài 1 - Mệnh đề chính đảo ngược + Mệnh đề 'where' chứa 2 mốc tương phản):
> *"This trend was diametrically reversed among citizens with no qualifications, where the figure stood at a mere 9% for younger individuals but surged to 72% in the oldest cohort."*

- **1. Mệnh đề chính độc lập (Main Clause):**
  - `[This trend]` (Chủ ngữ S_main) + `[was diametrically reversed]` (Vị ngữ bị động: *hoàn toàn bị đảo ngược 180 độ*) + `[among citizens with no qualifications]` (Cụm giới từ chỉ nhóm đối tượng không bằng cấp).
- **2. Mệnh đề quan hệ trạng từ chỉ ngữ cảnh (Relative Clause với 'where'):**
  - `[where]` (Trạng từ quan hệ thay thế cho bối cảnh nhóm trên) + `[the figure]` (Chủ ngữ con S_rel).
  - `[stood at a mere 9% for younger individuals]` (Vị ngữ 1: *chỉ đứng ở mức vỏn vẹn 9% đối với người trẻ*).
  - `[but]` (Liên từ đẳng lập).
  - `[surged to 72% in the oldest cohort]` (Vị ngữ 2: *nhưng lại tăng vọt lên 72% ở thế hệ cao tuổi nhất*).
- 💡 **Công thức ghép câu:** `This trend was diametrically reversed among [Group], where the figure stood at a mere [Số 1] for [Nhóm trẻ] but surged to [Số 2] in [Nhóm già].`"""
}

def update_file(rel_path, breakdown_md):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # If the file already has the breakdown in section 4, clean that up if needed,
    # or place it directly under section 2 (right after the model essay text)
    # Target: Right before '--- \n\n## 3. 💎 Kho Từ Vựng'
    pattern = r"(## 2\. 📝 Bài Viết Mẫu Chuẩn.*?\n)(---\s*\n\s*## 3\. 💎 Kho Từ Vựng)"
    
    # Check if section already has clause breakdown
    if "### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề" in content:
        # Replace existing one
        content = re.sub(r"### 🔬 Mổ Xẻ Chi Tiết Mệnh Đề.*?(?=---\s*\n\s*## 3|\Z)", "", content, flags=re.DOTALL)

    # Insert breakdown right before ## 3
    replacement = f"\\1---\n\n{breakdown_md}\n\n\\2"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # If pattern didn't match (for instance if ## 2 has slightly different title)
    if new_content == content:
        # Fallback search for '## 3. 💎 Kho Từ Vựng'
        idx = content.find("## 3. 💎 Kho Từ Vựng")
        if idx != -1:
            new_content = content[:idx] + breakdown_md + "\n\n---\n\n" + content[idx:]

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {rel_path}")

def main():
    for rel_path, breakdown in clause_data.items():
        update_file(rel_path, breakdown)

if __name__ == "__main__":
    main()
