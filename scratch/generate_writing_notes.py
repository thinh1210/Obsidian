import os
import sys

BASE_DIR = "/home/thinh/Obsidian/English/Writing"

essays = [
    # =========================================================================
    # TASK 2 ESSAYS
    # =========================================================================
    {
        "task": "task2",
        "type_folder": "agree_disagree",
        "filename": "Sample_01_Overweight_Physical_Education.md",
        "title": "Tackle Obesity: Physical Education vs Diet",
        "meta": {
            "task": "Task 2",
            "type": "Opinion (Agree or Disagree)",
            "topic": "Health & Lifestyle",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-agree-disagree-essay-sample-answer/",
            "tags": ["ielts/writing", "task2/agree_disagree", "topic/health", "band/9"]
        },
        "prompt": "The growing number of overweight people is putting a strain on the health care system in an effort to deal with the health issues involved. Some people think that the best way to deal with this problem is to introduce more physical education lessons in the school curriculum. To what extent do you agree or disagree?",
        "outline": """- **Dạng bài:** Opinion (Agree or Disagree) - Hướng tiếp cận: **Balanced / Partial Agreement** (Đồng ý thể dục học đường là giải pháp tốt, nhưng khẳng định cần kết hợp chế độ ăn uống & can thiệp thị trường).
- **Thesis Statement:** Thể dục học đường là một phương án khả thi để giải quyết vấn đề về lâu dài, nhưng chế độ dinh dưỡng (diet) cũng bắt buộc phải được xem xét.
- **Thân bài 1 (Ủng hộ Thể dục học đường - Physical Education):**
  - *Topic Sentence:* Tăng cường thể thao/vận động trong trường học giúp giải quyết tận gốc thói quen lười vận động về lâu dài.
  - *Giải thích:* Lối sống hiện đại khiến trẻ em ngồi bàn học nhiều giờ mỗi ngày (sedentary lifestyle), 2 buổi thể dục/tuần là không đủ.
  - *Hệ quả:* Thêm giờ thể dục và hoạt động ngoại khóa giúp trẻ rèn luyện thói quen vận động bền vững cho tới khi trưởng thành.
- **Thân bài 2 (Lý do cần thêm Chế độ ăn uống & Quản lý thực phẩm):**
  - *Topic Sentence:* Chỉ tập thể dục thôi là chưa đủ để đẩy lùi nạn béo phì trong toàn xã hội.
  - *Luận điểm phụ 1:* Trẻ em cần được giáo dục về dinh dưỡng hợp lý (clean eating) để biết thực phẩm nào tốt/xấu.
  - *Luận điểm phụ 2:* Cần biện pháp can thiệp trực tiếp từ chính phủ: đánh thuế thực phẩm siêu chế biến (Ultra-processed foods - UPFs) và trợ giá rau củ quả tươi.
- **Kết luận:** Khẳng định giải pháp tối ưu phải là sự phối hợp song hành giữa rèn luyện thể chất và kiểm soát chế độ dinh dưỡng thông qua giáo dục và chính sách giá cả.""",
        "model_essay": """Owing to the problems which a growing population of overweight people cause for the health care system, it is thought that the key to solving this issue is to have more sport and exercise in schools. I agree that this is one way to tackle the problem, but diet must also be taken into consideration.

Increasing sport or regular exercise in schools is a useful way to tackle weight problems in the long run in the general population. This method will encourage a new generation to develop vital habits which support overall health and also help them maintain a reasonable weight. At the moment, the average child in the West does sport possibly twice a week, which is not enough to counteract their otherwise sedentary lifestyle that comes from many hours each day of sitting at a desk for their lessons. By incorporating more exercise time and possibly extracurricular physical activities, they will undoubtedly become fitter and more active, and continue living that way after leaving schools.

However, targeting physical exercise in school children to reduce the current issue of obesity in the wider population is not effective enough on its own. Firstly, children in schools need to also be educated about what constitutes healthy foods and why in order to ensure a new generation of people who understand clean eating. Secondly, for a more immediate impact, it is important to look at reducing the number of Ultra processed foods (UPFs) on the market which too many people gravitate towards. For example, the government could impose a tax on UPFs to increase the price, and also reduce the cost of healthy foods, such as vegetables, to encourage a better diet.

In conclusion, I believe the best approach to tackling weight issues in the population starts with diet and exercise in schools but must also include encouraging a healthier diet through price changes targeting specific foods on the market.""",
        "vocab": [
            ("put a strain on", "/pʊt ə streɪn ɒn/", "C1", "Collocation", "Đặt gánh nặng / áp lực lên cái gì", "The growing number of overweight people is putting a strain on the health care system."),
            ("sedentary lifestyle", "/ˈsedntri ˈlaɪfstaɪl/", "C1", "Noun Phrase", "Lối sống thụ động, ngồi nhiều ít vận động", "Counteract their otherwise sedentary lifestyle that comes from hours of sitting at a desk."),
            ("extracurricular physical activities", "/ˌekstrəkəˈrɪkjələ ˈfɪzɪkl ækˈtɪvətiz/", "B2/C1", "Noun Phrase", "Các hoạt động thể chất ngoại khóa", "By incorporating more exercise time and possibly extracurricular physical activities..."),
            ("counteract", "/ˌkaʊntərˈækt/", "C1", "Verb", "Triệt tiêu, chống lại tác hại của cái gì", "Sport is not enough to counteract their otherwise sedentary lifestyle."),
            ("clean eating", "/kliːn ˈiːtɪŋ/", "B2", "Noun", "Ăn uống lành mạnh, thực phẩm tự nhiên", "...to ensure a new generation of people who understand clean eating."),
            ("ultra-processed foods (UPFs)", "/ˈʌltrə ˈprəʊsest fuːdz/", "C1", "Noun Phrase", "Thực phẩm siêu chế biến (nhiều phụ gia, dầu mỡ)", "Reducing the number of Ultra processed foods (UPFs) on the market."),
            ("gravitate towards", "/ˈɡrævɪteɪt təˈwɔːdz/", "C2", "Phrasal Verb", "Có xu hướng bị thu hút, ngả về phía...", "...which too many people gravitate towards."),
            ("impose a tax on", "/ɪmˈpəʊz ə tæks ɒn/", "B2/C1", "Collocation", "Áp thuế lên mặt hàng gì", "The government could impose a tax on UPFs to increase the price.")
        ],
        "grammar": [
            ("**Mệnh đề phân từ / Giới từ mở đầu câu (Participle / Prepositional phrase):** `Owing to the problems which...` thay cho *Because of*, tăng tính trang trọng và mạch lạc.", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md"),
            ("**Cấu trúc đối lập tinh tế (Balanced Thesis):** `I agree that this is one way to tackle..., but... must also be taken into consideration.`", "Grammar & Cohesion/4. Advanced Grammar Topics/4.1. Passive Voice (Câu bị động).md"),
            ("**Đảo cấu trúc trạng từ chỉ kết quả:** `...counteract their otherwise sedentary lifestyle that comes from...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md")
        ],
        "guide": """- **Chiến lược mở bài:** Paraphrase bối cảnh (vấn đề quá cân gây áp lực lên y tế) -> Nêu rõ mức độ đồng ý một phần (Agree in part: thể thao tốt nhưng dinh dưỡng là yếu tố quyết định không kém).
- **Chiến lược Thân bài 1 (Thừa nhận mặt đúng của đề bài):**
  - Mở đầu bằng Topic Sentence: *Increasing sport in schools is a useful way to tackle... in the long run.*
  - Chỉ ra thực trạng hiện tại: chỉ tập 2 lần/tuần vs ngồi cả ngày.
  - Đưa giải pháp: bổ sung giờ học + hoạt động ngoại khóa -> tạo lập thói quen suốt đời.
- **Chiến lược Thân bài 2 (Mở rộng góc nhìn / Luận điểm bổ trợ):**
  - Dùng liên từ chuyển tiếp tạo độ tương phản: *However, targeting... is not effective enough on its own.*
  - Triển khai 2 ý mạch lạc: (1) Giáo dục ăn uống lành mạnh trong trường; (2) Can thiệp vĩ mô (thuế UPFs, giảm giá thực phẩm sạch).
- **Chiến lược Kết bài:** Khẳng định phương pháp toàn diện = Giáo dục thể chất & Dinh dưỡng + Chính sách tài khóa can thiệp giá."""
    },

    {
        "task": "task2",
        "type_folder": "discuss_both_views",
        "filename": "Sample_01_University_vs_Work_Experience.md",
        "title": "University Education vs Experience & Soft Skills",
        "meta": {
            "task": "Task 2",
            "type": "Discussion (Discuss Both Views & Give Opinion)",
            "topic": "Work & Education",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-discussion-essay-model-answer/",
            "tags": ["ielts/writing", "task2/discuss_both_views", "topic/work", "band/9"]
        },
        "prompt": "Completing university education is thought by some to be the best way to get a good job. On the other hand, other people think that getting experience and developing soft skills is more important. Discuss both sides and give your opinion.",
        "outline": """- **Dạng bài:** Discussion (Discuss both views and give your opinion).
- **Thesis Statement & Quan điểm cá nhân:** Bằng đại học là điều kiện tiên quyết cho các ngành học thuật/chuyên môn sâu, trong khi kinh nghiệm và kỹ năng mềm lại chiếm ưu thế tuyệt đối trong kinh doanh và các ngành ứng dụng thực tế.
- **Thân bài 1 (Quan điểm 1: Bằng đại học - University Degree):**
  - *Topic Sentence:* Bằng đại học giúp ứng viên nổi trội và là tiêu chí tuyển chọn tiên quyết.
  - *Luận cứ 1:* Một số nghề bắt buộc phải có đào tạo chính quy (Bác sĩ, Luật sư, Giảng viên).
  - *Luận cứ 2:* Đại học không chỉ dạy kiến thức mà còn rèn tư duy phản biện (analytical thinking), nghiên cứu (research skills) và sự tò mò học thuật (intellectual curiosity).
- **Thân bài 2 (Quan điểm 2: Kinh nghiệm & Kỹ năng mềm - Soft Skills):**
  - *Topic Sentence:* Kinh nghiệm thực chiến và kỹ năng mềm tạo lợi thế quyết định trong các công việc thực hành.
  - *Ví dụ:* Quản lý doanh nghiệp cần trí tuệ cảm xúc (emotional intelligence), kỹ năng ủy quyền (delegating tasks) hơn là lý thuyết quản trị suông.
  - *Dẫn chứng thêm:* Ngành dịch vụ khách hàng, bán hàng, khách sạn đòi hỏi kỹ năng giao tiếp (interpersonal skills) chỉ có thể trau dồi qua cọ xát thực tế.
- **Kết luận:** Thành công khi xin việc phụ thuộc vào đặc thù từng ngành nghề (nghề chuyên môn cần bằng cấp, nghề kinh doanh/dịch vụ cần kỹ năng & kinh nghiệm).""",
        "model_essay": """Some people think that being a university graduate is the key to securing a good job, while others think experience and soft skills are better. In my opinion, I believe that the former is essential for academic jobs, while the latter are more useful in business and related industries.

On the one hand, many people think it is easy find good employment with an undergrad degree or above because it puts people one step ahead of other applicants, and can be the deciding factor between applicants. Furthermore, certain career paths are not open to those without a higher level of education, such as jobs requiring academic or specialist knowledge, namely teachers, lecturers, doctors and lawyers. Not only that, but academia does promote the development of useful skills, not just academic knowledge, for example analytical thinking, research skills and intellectual curiosity, which are valuable transferable skills. For this reason, tertiary education offers an advantage for those aiming for a professional or academic career.

On the other hand, having relevant work experience and soft skills can throw the balance in favour of the job applicant for certain hands-on types of work. For instance, for a corporate management position, having experience of managing others, running projects, delegating tasks and strong emotional intelligence is of more importance than the theory of management with no real hands-on experience when fresh out of university. Also, certain industries require interpersonal skills which can only be developed through extensive experience with people, such as in customer service, hospitality and sales. Consequently, it can be seen that tertiary education is no advantage at all in some areas.

In conclusion, I think that securing a good job requires a relevant background specific to the career or job the applicant is applying for. Some positions will require an academic background, whilst others benefit more from experience and skills.""",
        "vocab": [
            ("the former ... the latter", "/ðə ˈfɔːmə ... ðə ˈlætə/", "B2/C1", "Cohesive Pair", "Cái trước ... cái sau (dùng đối chiếu)", "The former is essential for academic jobs, while the latter are more useful in business."),
            ("securing a good job", "/sɪˈkjʊərɪŋ ə ɡʊd dʒɒb/", "B2/C1", "Collocation", "Giành được / đảm bảo được một công việc tốt", "Being a university graduate is the key to securing a good job."),
            ("one step ahead of", "/wʌn step əˈhed ɒv/", "C1", "Idiom/Phrase", "Đi trước một bước, có lợi thế hơn", "It puts people one step ahead of other applicants."),
            ("transferable skills", "/trænsˈfɜːrəbl skɪlz/", "C1", "Noun Phrase", "Kỹ năng mềm có thể chuyển đổi linh hoạt giữa các ngành", "...analytical thinking, research skills, which are valuable transferable skills."),
            ("throw the balance in favour of", "/θrəʊ ðə ˈbæləns ɪn ˈfeɪvər ɒv/", "C2", "Idiom", "Làm cán cân nghiêng về phía ai đó (tạo lợi thế)", "Can throw the balance in favour of the job applicant."),
            ("hands-on types of work", "/hændz ɒn taɪps ɒv wɜːk/", "C1", "Noun Phrase", "Công việc mang tính thực hành/thực chiến", "...throw the balance in favour of the job applicant for certain hands-on types of work."),
            ("emotional intelligence (EQ)", "/ɪˈməʊʃənl ɪnˈtelɪdʒəns/", "C1", "Noun Phrase", "Trí tuệ cảm xúc", "Having strong emotional intelligence is of more importance than theory."),
            ("interpersonal skills", "/ˌɪntəˈpɜːsənl skɪlz/", "C1", "Noun Phrase", "Kỹ năng giao tiếp và ứng xử giữa người với người", "Certain industries require interpersonal skills developed through extensive experience.")
        ],
        "grammar": [
            ("**Cấu trúc Not only... but (Đảo ngữ nhấn mạnh):** `Not only that, but academia does promote the development of...` (Trợ động từ *does* nhấn mạnh động từ *promote*).", "Grammar & Cohesion/4. Advanced Grammar Topics/4.4. Inversion (Đảo ngữ).md"),
            ("**Rút gọn mệnh đề phân từ thời gian:** `...when fresh out of university.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.2. Connecting Clauses with Prepositions.md"),
            ("**Cặp liên từ song song thể hiện hai mặt:** `On the one hand,... / On the other hand,...` phối hợp nhịp nhàng với `Consequently, it can be seen that...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md")
        ],
        "guide": """- **Chiến lược mở bài:** Paraphrase 2 luồng quan điểm -> Đưa ra lập trường phân loại (the former for X, the latter for Y).
- **Body 1 (Bàn về Bằng đại học):**
  - Khẳng định giá trị của bằng đại học trong các ngành đặc thù (Luật, Y, Giáo dục).
  - Khai thác giá trị vô hình của môi trường học thuật: *analytical thinking*, *intellectual curiosity*.
- **Body 2 (Bàn về Kinh nghiệm & Kỹ năng mềm):**
  - Đối chiếu với môi trường doanh nghiệp: lý thuyết quản trị không thay thế được khả năng quản trị con người và giao tiếp.
  - Đưa ví dụ sắc bén về Hospitality, Sales, Corporate Management.
- **Kết luận:** Tóm tắt sự phụ thuộc vào từng ngành nghề cụ thể."""
    },

    {
        "task": "task2",
        "type_folder": "problem_solution",
        "filename": "Sample_01_Criminal_Reoffending.md",
        "title": "Criminal Reoffending: Causes & Solutions",
        "meta": {
            "task": "Task 2",
            "type": "Cause & Solution (Problems & Measures)",
            "topic": "Crime & Law",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-solution-essay-band-9-model-answer/",
            "tags": ["ielts/writing", "task2/problem_solution", "topic/crime", "band/9"]
        },
        "prompt": "Many offenders commit more crimes after serving their first punishment. Why is this happening, and what measures can be taken to tackle this problem?",
        "outline": """- **Dạng bài:** Two-Question (Cause and Solution).
- **Thesis Statement:** Nguyên nhân chính dẫn đến tái phạm là thiếu cải tạo hoàn lương (rehabilitation) và khó khăn tìm việc sau khi ra tù. Giải pháp trọng tâm là đào tạo nghề trong trại giam và theo dõi/hỗ trợ tái hòa nhập cộng đồng.
- **Thân bài 1 (Nguyên nhân - Causes):**
  - *Cause 1:* Thiếu chương trình cải tạo (lack of rehabilitation): Tù nhân không được học nghề mới, không hiểu được hậu quả hành vi đối với nạn nhân.
  - *Cause 2:* Định kiến xã hội và hồ sơ tiền án cản trở tìm việc: Không có thu nhập hợp pháp khiến họ cùng đường và quay lại con đường phạm pháp.
- **Thân bài 2 (Giải pháp - Solutions tương ứng):**
  - *Solution 1:* Cung cấp chương trình đào tạo nghề thực tế ngay trong thời gian thụ án (retrain with useful skills) -> mở ra cơ hội việc làm sau mãn hạn.
  - *Solution 2:* Thiết lập hệ thống giám sát và tư vấn sau khi thả tự do (closer observation and mentoring) -> phát hiện nguy cơ sớm và hỗ trợ tâm lý tái hòa nhập.
- **Kết luận:** Tóm tắt lại cả hai nhóm biện pháp: cải tạo dạy nghề từ bên trong và nâng đỡ giám sát từ bên ngoài.""",
        "model_essay": """A large number of criminals who serve their first prison sentence, leave prison only to reoffend. This is mainly because of the lack of rehabilitation and difficulty finding regular employment once released. There are a number of solutions which should be implemented to deal with criminals who reoffend.

Firstly, the reason for most first-time offenders committing crimes again, once they have been released from prison, is due to the lack of rehabilitation whilst in prison. In other words, offenders are not given a chance to retrain and learn new skills for their future or develop a deeper understanding of correct moral behaviour and how their actions affect other people. Furthermore, another factor is having a criminal record which makes it exceedingly difficult to find a job after release from prison. When faced with the inability to earn a regular livelihood, former convicts frequently find themselves driven back into unlawful activities simply to survive.

There are two effective solutions to the problem of repeat offenders. One way to tackle this is to ensure that all criminals entering prison are given the chance to retrain with useful skills which will hopefully ensure them a job after they have served their sentence. By doing this, it will help them integrate back into society. Another way of dealing with this issue is for the police or probation officers to keep a closer eye on ex-prisoners once they have been released. This will assist in monitoring their actions and seeing if they are having difficulty coping in the community so that timely interventions can be made.

In conclusion, regardless of the reasons for reoffending, having skills training and education in prison as well as closer observation for newly released offenders can be effective in preventing criminals from committing crimes again.""",
        "vocab": [
            ("reoffend / repeat offender", "/riːəˈfend/ - /rɪˈpiːt əˈfendər/", "C1", "Verb / Noun", "Tái phạm tội / Tội phạm tái phạm", "A large number of criminals leave prison only to reoffend."),
            ("rehabilitation", "/ˌriːəˌbɪlɪˈteɪʃn/", "C1", "Noun", "Sự cải tạo, phục hồi nhân phẩm", "This is mainly because of the lack of rehabilitation whilst in prison."),
            ("regular livelihood", "/ˈreɡjələ ˈlaɪvlihʊd/", "C1", "Noun Phrase", "Kế sinh nhai, nguồn thu nhập ổn định", "When faced with the inability to earn a regular livelihood..."),
            ("former convicts / ex-prisoners", "/ˈfɔːmə ˈkɒnvɪkts/", "C1", "Noun Phrase", "Người từng thụ án tù, cựu tù nhân", "Former convicts frequently find themselves driven back into unlawful activities."),
            ("integrate back into society", "/ˈɪntɪɡreɪt bæk ˈɪntuː səˈsaɪəti/", "C1", "Collocation", "Tái hòa nhập vào đời sống xã hội", "By doing this, it will help them integrate back into society."),
            ("probation officer", "/prəˈbeɪʃn ˈɒfɪsər/", "C2", "Noun", "Cán bộ quản chế, giám sát người hưởng án treo", "Another way is for probation officers to keep a closer eye on ex-prisoners."),
            ("keep a close eye on", "/kiːp ə kləʊs aɪ ɒn/", "B2/C1", "Idiom", "Theo dõi sát sao, giám sát chặt chẽ", "...keep a closer eye on ex-prisoners once released."),
            ("timely intervention", "/ˈtaɪmli ˌɪntəˈvenʃn/", "C1", "Noun Phrase", "Sự can thiệp kịp thời", "...so that timely interventions can be made.")
        ],
        "grammar": [
            ("**Cấu trúc nguyên nhân - hệ quả đa tầng:** `This is mainly because of [Noun Phrase] and [Noun Phrase] once released.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.2. Connecting Clauses with Prepositions.md"),
            ("**Bị động kép & phân từ rút gọn:** `When faced with the inability to..., former convicts find themselves driven back into...`", "Grammar & Cohesion/4. Advanced Grammar Topics/4.1. Passive Voice (Câu bị động).md"),
            ("**Cụm từ liên kết điều kiện độc lập:** `In conclusion, regardless of the reasons for..., having [V-ing] as well as [Noun] can be effective in...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md")
        ],
        "guide": """- **Chiến lược phân bổ đoạn:**
  - Body 1 dành trọn vẹn giải thích **2 nguyên nhân cốt lõi** (1 nguyên nhân chủ quan trong tù: thiếu cải tạo, 1 nguyên nhân khách quan ngoài đời: tiền án khó xin việc).
  - Body 2 đưa ra **2 giải pháp đối ứng trực tiếp** (Đào tạo nghề để giải quyết việc làm; Cán bộ quản chế để giải quyết việc tái hòa nhập).
- **Liên kết nguyên nhân & giải pháp:** Đảm bảo giải pháp 1 giải quyết đúng nguyên nhân 1, giải pháp 2 giải quyết đúng nguyên nhân 2 để đạt điểm tối đa Coherence & Cohesion."""
    },

    {
        "task": "task2",
        "type_folder": "advantages_disadvantages",
        "filename": "Sample_01_One_Global_Language.md",
        "title": "A Single Global Language: Pros and Cons",
        "meta": {
            "task": "Task 2",
            "type": "Advantages & Disadvantages",
            "topic": "Language & Globalization",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-advantage-disadvantage-model-essay/",
            "tags": ["ielts/writing", "task2/advantages_disadvantages", "topic/language", "band/9"]
        },
        "prompt": "The development of tourism contributed to English becoming the most prominent language in the world. Some people think this will lead to English becoming the only language to be spoken globally. What are the advantages and disadvantages to having one language in the world?",
        "outline": """- **Dạng bài:** Advantages and Disadvantages (Phân tích cả hai mặt lợi và hại).
- **Thesis Statement:** Việc toàn cầu chỉ dùng một ngôn ngữ duy nhất sẽ thúc đẩy sự hiểu biết quốc tế và phát triển kinh tế, nhưng lại mang đến tổn thất khổng lồ về mặt bản sắc văn hóa và di sản nhân loại.
- **Thân bài 1 (Ưu điểm - Advantages):**
  - *Lợi ích 1:* Thấu hiểu xuyên biên giới (enable greater understanding between countries) -> xóa bỏ rào cản ngôn ngữ.
  - *Lợi ích 2:* Tăng tốc dòng chảy tri thức, thương mại và hợp tác quốc tế (free flow of information and technological sharing).
  - *Lợi ích 3:* Giảm thiểu chi phí và thời gian cho công tác biên phiên dịch trong ngoại giao và kinh doanh.
- **Thân bài 2 (Nhược điểm - Disadvantages):**
  - *Bất lợi 1:* Nguy cơ tuyệt chủng của hàng ngàn bản địa ngữ kéo theo sự biến mất của các nền văn hóa độc bản.
  - *Bất lợi 2:* Mất đi sự đa dạng góc nhìn thế giới (linguistic diversity reflects unique human perspectives).
  - *Bất lợi 3:* Xói mòn bản sắc cá nhân và di sản cha ông trao truyền qua các thế hệ.
- **Kết luận:** Dù lợi ích kinh tế và giao tiếp là rõ ràng, nhưng cái giá phải trả về mặt văn hóa là quá lớn. Cần ưu tiên bảo tồn ngôn ngữ địa phương.""",
        "model_essay": """It is thought by some people that English, which is now the most widely spoken language in the world, may one day predominate over all other languages and result in their eventual disappearance. Having one language would certainly aid understanding and economic growth but there will also be some drawbacks.

One evident benefit to having one global language is that it would enable greater understanding between countries. In other words, if everyone spoke one language, there would be complete understanding between not only countries but all people throughout the world which would promote learning, the flow of information and ideas. Another positive aspect would be the promotion of trade. With no language barriers, businesses could easily expand overseas and operate with far greater efficiency, completely eliminating the considerable financial expenditure previously allocated to translation and interpreting services.

On the other hand, there are obvious downsides to having only one global language. Firstly, it would mean that all other languages would eventually disappear and, along with them, their cultures. The diversity of cultures is one of the joys this world has to offer. Each culture is unique with its own way of life and its own perspective of the world which is reflected through its language. If the language were to vanish, an indispensable part of human heritage would be lost forever. Furthermore, people would feel a loss of identity because their native tongue connects them intimately with their ancestors and geographical roots.

In conclusion, while there are plus points to having one global language, too much would be lost as a result. Maintaining local languages and cultures should be prioritised to ensure a rich world heritage for future generations.""",
        "vocab": [
            ("predominate over", "/prɪˈdɒmɪneɪt ˈəʊvər/", "C2", "Verb", "Chiếm ưu thế tuyệt đối, áp đảo hoàn toàn", "...may one day predominate over all other languages."),
            ("eventual disappearance", "/ɪˈventʃuəl ˌdɪsəˈpɪərəns/", "C1", "Noun Phrase", "Sự biến mất sau cùng, sự tuyệt chủng dần dần", "...and result in their eventual disappearance."),
            ("language barriers", "/ˈlæŋɡwɪdʒ ˈbæriəz/", "B2/C1", "Noun Phrase", "Rào cản ngôn ngữ", "With no language barriers, businesses could easily expand overseas."),
            ("financial expenditure", "/faɪˈnænʃl ɪkˈspendɪtʃər/", "C1", "Noun Phrase", "Chi phí tài chính", "Eliminating the considerable financial expenditure allocated to translation."),
            ("indispensable part", "/ˌɪndɪˈspensəbl pɑːt/", "C1", "Collocation", "Phần không thể thiếu, cốt yếu", "An indispensable part of human heritage would be lost forever."),
            ("loss of identity", "/lɒs ɒv aɪˈdentəti/", "C1", "Noun Phrase", "Sự đánh mất bản sắc", "People would feel a loss of identity because their native tongue connects them..."),
            ("native tongue", "/ˈneɪtɪv tʌŋ/", "B2/C1", "Noun Phrase", "Tiếng mẹ đẻ", "Their native tongue connects them intimately with their ancestors."),
            ("world heritage", "/wɜːld ˈherɪtɪdʒ/", "B2/C1", "Noun Phrase", "Di sản thế giới", "...to ensure a rich world heritage for future generations.")
        ],
        "grammar": [
            ("**Mệnh đề quan hệ không xác định mở rộng:** `English, which is now the most widely spoken language in the world, may one day...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Câu điều kiện loại 2 giả định:** `In other words, if everyone spoke one language, there would be complete understanding...`", "Grammar & Cohesion/4. Advanced Grammar Topics/4.5. Conditionals & Wish (Câu điều kiện & Ước).md"),
            ("**Cấu trúc thức giả định với 'were to':** `If the language were to vanish, an indispensable part... would be lost forever.`", "Grammar & Cohesion/4. Advanced Grammar Topics/4.6. Subjunctive Mood (Thức giả định).md")
        ],
        "guide": """- **Lưu ý quan trọng cho dạng Advantages & Disadvantages:**
  - Cần chia 1 đoạn riêng cho **Ưu điểm** và 1 đoạn riêng cho **Nhược điểm**.
  - Dùng các từ đồng nghĩa thay thế linh hoạt: *Benefits / Positive points / Gains* thay cho *Advantages*; *Downsides / Drawbacks / Negative points* thay cho *Disadvantages*.
- **Cách cân đối:** Thể hiện rõ sự thấu đáo trong việc cân nhắc giá trị kinh tế vs giá trị văn hóa tinh thần."""
    },

    {
        "task": "task2",
        "type_folder": "direct_questions",
        "filename": "Sample_01_Money_and_Happiness.md",
        "title": "Money & Happiness: What Truly Matters?",
        "meta": {
            "task": "Task 2",
            "type": "Direct Questions (Two-Part Questions)",
            "topic": "Society & Philosophy of Life",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-model-essay-score-9/",
            "tags": ["ielts/writing", "task2/direct_questions", "topic/society", "band/9"]
        },
        "prompt": "Some people think that money is one of the most essential factors in promoting happiness. Do you think people can be happy without much money? What other factors contribute towards happiness?",
        "outline": """- **Dạng bài:** Direct Questions (Trả lời 2 câu hỏi trực tiếp).
  - *Câu hỏi 1:* Con người có thể hạnh phúc khi không có nhiều tiền không?
  - *Câu hỏi 2:* Những yếu tố nào khác đóng góp vào niềm hạnh phúc?
- **Thesis Statement:** Hoàn toàn có thể hạnh phúc mà không cần nhiều của cải nếu đáp ứng được các nhu cầu cơ bản; các yếu tố như sức khỏe, quan hệ gia đình/xã hội và mục đích sống đóng vai trò cốt lõi hơn tiền bạc.
- **Thân bài 1 (Trả lời Câu hỏi 1 - Hạnh phúc không cần nhiều tiền):**
  - Khẳng định: Tiền mang lại tiện nghi tức thời, nhưng không bảo đảm hạnh phúc (đặc biệt khi đối mặt bệnh tật, mất mát).
  - Điều kiện: Miễn là con người có đủ tài chính cho các nhu cầu thiết yếu (necessities: thức ăn, nơi ở, y tế cơ bản), việc thiếu các món đồ xa xỉ không làm giảm đi sự thanh thản và niềm vui cuộc sống.
- **Thân bài 2 (Trả lời Câu hỏi 2 - Các yếu tố khác tạo nên hạnh phúc):**
  - *Yếu tố 1: Sức khỏe (Health):* Cơ thể tráng kiện là nền tảng tận hưởng cuộc sống (a healthy body enables one to appreciate daily living).
  - *Yếu tố 2: Mối quan hệ gắn kết (Meaningful relationships):* Tình cảm gia đình, bạn bè bè bạn mang lại sự an ủi và chỗ dựa tinh thần (emotional support).
  - *Yếu tố 3: Mục đích sống & Sự cống hiến (Sense of purpose):* Làm công việc yêu thích hoặc giúp đỡ cộng đồng mang lại cảm giác thỏa nguyện sâu sắc.
- **Kết luận:** Tóm tắt trả lời gãy gọn cả 2 câu hỏi trong một kết luận cô đọng.""",
        "model_essay": """Money is considered by many people to be one of the most important contributing factors towards happiness. In my opinion, it is possible for people to be happy even if they have little money and other aspects of life can play a more vital role in creating happiness than wealth alone.

Although money allows people to afford luxuries and treats, which certainly do bring temporary enjoyment and satisfaction, a substantial number of people are happy without money. Firstly, money is no guarantee of happiness, particularly if disease or disaster feature largely in someone’s life. Secondly, as long as people have the money to cover their necessities, doing without luxury items does not negatively affect the pleasures that a good life can bring. For example, simple pleasures such as spending quality time outdoors or sharing laughter with loved ones cost virtually nothing yet cultivate profound contentment.

Other factors play an equally or even more significant role in contributing to a person's happiness. First among these is health; good physical and mental well-being allows people to enjoy everyday moments and participate fully in activities they cherish. Another crucial element is fulfilling relationships with family, friends, and the broader community, which offer mutual trust, unconditional emotional support, and a sense of belonging. Finally, having a meaningful purpose in life, whether through engaging work, artistic hobbies, or altruistic contribution to society, brings an enduring feeling of fulfillment that wealth can never purchase.

In conclusion, I firmly believe that true happiness does not hinge entirely on financial abundance. As long as basic survival needs are met, vibrant health, affectionate social bonds, and a meaningful purpose represent the true cornerstones of human joy.""",
        "vocab": [
            ("temporary enjoyment", "/ˈtemprəri ɪnˈdʒɔɪmənt/", "B2", "Collocation", "Niềm vui thích tạm thời", "Money allows people to afford treats, which bring temporary enjoyment."),
            ("profound contentment", "/prəˈfaʊnd kənˈtentmənt/", "C2", "Noun Phrase", "Sự bằng lòng, thanh thản sâu sắc từ tâm can", "...cost virtually nothing yet cultivate profound contentment."),
            ("fulfilling relationships", "/fʊlˈfɪlɪŋ rɪˈleɪʃnʃɪps/", "C1", "Noun Phrase", "Các mối quan hệ mang lại cảm giác trọn vẹn, thỏa nguyện", "Another crucial element is fulfilling relationships with family and friends."),
            ("unconditional emotional support", "/ˌʌnkənˈdɪʃənl ɪˈməʊʃənl səˈpɔːt/", "C1", "Noun Phrase", "Sự hỗ trợ tinh thần vô điều kiện", "...which offer mutual trust and unconditional emotional support."),
            ("sense of belonging", "/sens ɒv bɪˈlɒŋɪŋ/", "C1", "Collocation", "Cảm giác thuộc về một cộng đồng/tập thể", "...unconditional emotional support and a sense of belonging."),
            ("altruistic contribution", "/ˌæltruˈɪstɪk ˌkɒntrɪˈbjuːʃn/", "C2", "Noun Phrase", "Sự đóng góp vị tha, không màng vụ lợi", "...whether through engaging work or altruistic contribution to society."),
            ("hinge on", "/hɪndʒ ɒn/", "C1", "Phrasal Verb", "Phụ thuộc hoàn toàn vào điều gì", "True happiness does not hinge entirely on financial abundance."),
            ("cornerstones of human joy", "/ˈkɔːnəstəʊnz ɒv ˈhjuːmən dʒɔɪ/", "C2", "Metaphor", "Nền móng / viên đá tảng tạo nên niềm vui con người", "...represent the true cornerstones of human joy.")
        ],
        "grammar": [
            ("**Mệnh đề nhượng bộ 'Although':** `Although money allows people to afford..., which certainly do bring..., a substantial number of people are happy...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Trợ động từ 'do' mang sắc thái khẳng định mạnh mẽ:** `...which certainly do bring temporary enjoyment...`", "Grammar & Cohesion/1. Tenses & Core Grammar/1.1. Present Tenses.md"),
            ("**Mệnh đề danh từ làm tân ngữ sau giới từ:** `...does not negatively affect [what a good life can bring].`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md")
        ],
        "guide": """- **Cấu trúc 4 đoạn chuẩn xác cho Direct Questions:**
  - **Mở bài:** 2 câu (Câu 1 dẫn dắt vấn đề tiền bạc & hạnh phúc; Câu 2 trực tiếp trả lời vắn tắt 2 câu hỏi).
  - **Thân bài 1:** Dành riêng giải quyết câu hỏi 1 (Vì sao không cần nhiều tiền vẫn hạnh phúc: tiền không ngăn được bệnh tật, chỉ cần nhu cầu cơ bản).
  - **Thân bài 2:** Dành riêng giải quyết câu hỏi 2 (Liệt kê 3 yếu tố quan trọng hơn: Sức khỏe -> Mối quan hệ -> Mục đích sống).
  - **Kết bài:** Khẳng định lại câu trả lời một cách trang trọng, đúc kết triết lý sống."""
    },

    # =========================================================================
    # TASK 1 REPORTS
    # =========================================================================
    {
        "task": "task1",
        "type_folder": "bar_chart",
        "filename": "Sample_01_Consumer_Goods_Spending.md",
        "title": "Consumer Goods Spending in France and the UK (2010)",
        "meta": {
            "task": "Task 1",
            "type": "Bar Chart",
            "topic": "Economy & Consumer Spending",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-model-bar-chart-band-score-9/",
            "tags": ["ielts/writing", "task1/bar_chart", "topic/economy", "band/9"]
        },
        "prompt": "The chart illustrates the amount of money spent on five consumer goods (cars, computers, books, perfume and cameras) in France and the UK in 2010. Units are measured in pounds sterling. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2015/01/Bar-Chart-Model-300x179.jpg",
        "outline": """- **Loại biểu đồ:** Bar Chart (Biểu đồ cột so sánh tĩnh tại một năm 2010).
- **Đơn vị đo lường:** Bảng Anh (Pounds sterling - £).
- **Phân tích tổng quan (Overview):**
  1. Người Anh (UK) chi tiêu cho cả 5 mặt hàng tiêu dùng nhiều hơn người Pháp (France).
  2. Ở cả hai quốc gia, **xe hơi (cars)** là mặt hàng được chi tiêu nhiều nhất.
  3. Mặt hàng có mức chi tiêu chênh lệch rõ rệt nhất giữa hai nước là **máy ảnh (cameras)**.
- **Phân đoạn Thân bài (Grouping Strategy):**
  - **Body 1 (Các mặt hàng chi tiêu cao: Cars, Books, Computers):** So sánh số liệu cụ thể giữa UK và France ở nhóm sản phẩm chủ lực.
  - **Body 2 (Các mặt hàng chi tiêu thấp hơn & Chênh lệch lớn: Cameras, Perfume):** Nêu bật sự cách biệt về máy ảnh và nước hoa.""",
        "model_essay": """The chart illustrates the amount of money spent on five consumer goods (cars, computers, books, perfume and cameras) in France and the UK in 2010. Units are measured in pounds sterling.

Overall, the UK spent more money on consumer goods than France in the period given. Both the British and the French spent most of their money on cars whereas the least amount of money was spent on perfume in the UK compared to cameras in France. Furthermore, the most significant difference in expenditure between the two countries was on cameras.

In terms of cars, people in the UK spent approximately £450,000 on this as opposed to around £400,000 in France. Similarly, the British outlay on books was higher than the French, at roughly £400,000 and £300,000 respectively. In the UK, expenditure on computers reached roughly £350,000, while the figure for France was slightly lower, at around £380,000, making it the only category where France spent more than the UK.

Turning to the remaining categories, the UK spent significantly more on cameras than France, with figures standing at over £350,000 compared to under £150,000 respectively. Finally, perfume saw the lowest expenditure in the UK at around £140,000, which was slightly below the French expenditure of approximately £200,000.""",
        "vocab": [
            ("illustrates / portrays / depicts", "/ˈɪləstreɪts/", "B2/C1", "Verb", "Minh họa, mô tả số liệu", "The chart illustrates the amount of money spent..."),
            ("pounds sterling", "/paʊndz ˈstɜːlɪŋ/", "B2", "Noun", "Đơn vị tiền tệ Bảng Anh", "Units are measured in pounds sterling."),
            ("expenditure on / outlay on", "/ɪkˈspendɪtʃər ɒn/ - /ˈaʊtleɪ/", "C1", "Noun Collocation", "Mức chi tiêu / kinh phí bỏ ra cho việc gì", "The most significant difference in expenditure between the two countries was on cameras."),
            ("as opposed to", "/æz əˈpəʊzd tuː/", "C1", "Phrase", "Trái ngược với, thay vì so với...", "People in the UK spent £450,000 as opposed to around £400,000 in France."),
            ("respectively", "/rɪˈspektɪvli/", "B2/C1", "Adverb", "Lần lượt theo thứ tự đã nêu", "At roughly £400,000 and £300,000 respectively."),
            ("the figure for [X]", "/ðə ˈfɪɡər fɔː/", "B2/C1", "Phrase", "Số liệu dành cho đối tượng X", "While the figure for France was slightly lower..."),
            ("turning to the remaining categories", "/ˈtɜːnɪŋ tuː/", "C1", "Signposting Phrase", "Chuyển sang các danh mục còn lại (từ nối mạch lạc)", "Turning to the remaining categories, the UK spent significantly more..."),
            ("stood at / saw the lowest expenditure", "/stʊd æt/", "B2/C1", "Verb Collocation", "Đứng ở mức / ghi nhận mức chi thấp nhất", "Figures standing at over £350,000 compared to under £150,000.")
        ],
        "grammar": [
            ("**Cấu trúc đối chiếu song hành:** `Both the British and the French spent most of their money on..., whereas the least amount was spent on...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md"),
            ("**Mệnh đề phân từ tạo nhận xét:** `..., making it the only category where France spent more than the UK.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**So sánh hơn và tính từ bậc cao:** `...spent significantly more on cameras than France, with figures standing at... compared to...`", "Grammar & Cohesion/1. Tenses & Core Grammar/1.2. Past Tenses.md")
        ],
        "guide": """- **Quy tắc vàng của Task 1 Bar Chart:**
  - Không bao giờ đưa ý kiến cá nhân (No personal opinions).
  - Phải có câu **Overview** rõ ràng (nhìn ra 2 đặc điểm nổi bật nhất: ai cao nhất, chênh lệch nào lớn nhất).
  - Sử dụng linh hoạt các cụm từ xấp xỉ (*approximately, roughly, around, slightly over, just under*) vì đây là biểu đồ cột không có bảng số liệu tuyệt đối.
  - Gom nhóm thông tin logic: nhóm mặt hàng đắt tiền/chủ lực vào một đoạn, nhóm còn lại vào đoạn thứ hai."""
    },

    {
        "task": "task1",
        "type_folder": "line_graph",
        "filename": "Sample_01_Spreads_Consumption.md",
        "title": "Consumption of Three Spreads (1981 - 2007)",
        "meta": {
            "task": "Task 1",
            "type": "Line Graph",
            "topic": "Food & Nutrition Trends",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-writing-task-1-line-graph-model-score-9/",
            "tags": ["ielts/writing", "task1/line_graph", "topic/food", "band/9"]
        },
        "prompt": "The line graph illustrates the amount of three kinds of spreads (margarine, butter, and low fat and reduced spreads) which were consumed from 1981 to 2007. Units are measured in grams. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2014/11/consumption-of-spreads-line-graph.jpg",
        "outline": """- **Loại biểu đồ:** Line Graph (Biểu đồ xu hướng thay đổi qua thời gian từ 1981 đến 2007).
- **Các đối tượng:** 3 loại bơ quết bánh (Margarine, Butter, Low fat spreads). Đơn vị: Grams.
- **Phân tích tổng quan (Overview):**
  1. Mức tiêu thụ của margarine và butter có xu hướng giảm chung qua cả thời kỳ, trong khi low fat spreads tăng lên rõ rệt.
  2. Bơ truyền thống (butter) bắt đầu ở vị trí quán quân, margarine vươn lên dẫn đầu ở giữa kỳ, nhưng về sau cùng thì low fat spreads trở thành loại phổ biến nhất.
- **Phân chia đoạn thân bài:**
  - **Body 1 (Butter & Margarine - Hai đường giảm):** Bắt đầu từ 1981 (butter 140g, margarine 90g), biến động qua các năm và cùng tụt dốc vào năm 2007.
  - **Body 2 (Low fat & Reduced spreads - Đường tăng):** Xuất hiện từ năm 1996 ở mức chỉ khoảng 10g, sau đó tăng vọt đạt đỉnh khoảng 80g và kết thúc ở vị trí dẫn đầu.""",
        "model_essay": """The line graph illustrates the amount of three kinds of spreads (margarine, butter, and low fat and reduced spreads) which were consumed from 1981 to 2007. Units are measured in grams.

Overall, the consumption of margarine and butter decreased over the period given, while for low fat and reduced spreads, it rose. At the start of the period, butter was the most popular spread. Margarine was the most widely consumed in the middle of the period but, by the end, low fat and reduced spreads was most popular.

In 1981, butter was the most popular spread, with consumption standing at around 140 grams. This was followed by margarine at about 90 grams. Over the next five years, the figure for butter fell sharply to just below 120 grams in 1986, while margarine experienced a slight increase to around 100 grams. From that point onwards, margarine consumption surpassed that of butter and became the primary spread, peaking at over 100 grams in 1991, before witnessing a persistent downward trend to finish at roughly 40 grams in 2007. Butter consumption continued to decline steadily, closing the period at about 50 grams.

In contrast, low fat and reduced spreads were only introduced in 1996 at around 10 grams. However, this category experienced a steep climb over the next five years, peaking at approximately 80 grams in 2001. Although its consumption dipped slightly towards the end of the timeline, it remained the most widely consumed spread in 2007, standing at about 70 grams.""",
        "vocab": [
            ("consumption of", "/kənˈsʌmpʃn ɒv/", "B2/C1", "Noun Phrase", "Mức tiêu thụ của cái gì", "The consumption of margarine and butter decreased over the period."),
            ("surpassed", "/səˈpɑːst/", "C1", "Verb", "Vượt qua, qua mặt", "Margarine consumption surpassed that of butter..."),
            ("peaked at", "/piːkt æt/", "B2/C1", "Verb Collocation", "Đạt đỉnh điểm tại mức nào", "...peaking at over 100 grams in 1991."),
            ("witnessed a persistent downward trend", "/ˈwɪtnɪst ə pəˈsɪstənt ˈdaʊnwəd trend/", "C1/C2", "Phrase", "Ghi nhận một xu hướng giảm dai dẳng, liên tục", "...before witnessing a persistent downward trend to finish at roughly 40 grams."),
            ("steep climb", "/stiːp klaɪm/", "C1", "Noun Phrase", "Sự tăng vọt dốc đứng", "Experienced a steep climb over the next five years."),
            ("dipped slightly", "/dɪpt ˈslaɪtli/", "B2/C1", "Verb Phrase", "Giảm nhẹ một chút rồi chững lại", "Although its consumption dipped slightly towards the end..."),
            ("stood at / closing at", "/stʊd æt/", "B2/C1", "Verb", "Dừng ở mức / khép lại thời kỳ ở mức", "...standing at about 70 grams."),
            ("over the period given / timeline", "/ˈtaɪmlaɪn/", "B2", "Prepositional Phrase", "Trong suốt giai đoạn được đưa ra", "Over the period given...")
        ],
        "grammar": [
            ("**Cụm phân từ diễn tả kết quả cuối kỳ:** `...before witnessing a persistent downward trend to finish at roughly 40 grams in 2007.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.2. Connecting Clauses with Prepositions.md"),
            ("**Thay thế danh từ tránh lặp bằng 'that of':** `...margarine consumption surpassed [that of butter]...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Sử dụng liên từ nhượng bộ trong câu tóm tắt số liệu:** `Although its consumption dipped slightly..., it remained the most widely consumed spread...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md")
        ],
        "guide": """- **Bí quyết mô tả Line Graph:**
  - Tuyệt đối không mô tả từng năm một cách máy móc (Không được viết: năm 1981 là X, năm 1982 là Y, năm 1983 là Z).
  - Phải chỉ ra được điểm bắt đầu, xu hướng chung (tăng, giảm, ổn định, dao động), các điểm giao cắt (intersection/surpassing), điểm đạt đỉnh (peak) và điểm kết thúc.
  - Gom các đường có cùng xu hướng vào chung một đoạn (ở đây gom Butter & Margarine vào đoạn 1 vì cùng giảm; Low-fat tách riêng đoạn 2 vì là đường tăng cá biệt)."""
    },

    {
        "task": "task1",
        "type_folder": "pie_chart",
        "filename": "Sample_01_Energy_Production_France.md",
        "title": "Energy Production in France (1995 vs 2005)",
        "meta": {
            "task": "Task 1",
            "type": "Pie Chart",
            "topic": "Energy & Environment",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-pie-chart-task-1-model-score-9/",
            "tags": ["ielts/writing", "task1/pie_chart", "topic/energy", "band/9"]
        },
        "prompt": "The two pie charts illustrate the proportion of five sources of energy production (coal, gas, nuclear, petrol and other sources) in France in two years (1995 and 2005). Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2014/11/ielts-pie-chart-comparison-300x181.png",
        "outline": """- **Loại biểu đồ:** Multiple Pie Charts (So sánh cơ cấu sản xuất năng lượng Pháp năm 1995 và 2005).
- **Đơn vị:** Phần trăm (%).
- **Phân tích tổng quan (Overview):**
  1. Trong cả 2 năm, Than đá (Coal) và Khí đốt (Gas) chiếm hơn một nửa tổng sản lượng năng lượng.
  2. Nguồn năng lượng hạt nhân (Nuclear) và nguồn khác tăng gần gấp đôi tỷ trọng.
  3. Dầu mỏ (Petrol) là nguồn năng lượng duy nhất sụt giảm trong giai đoạn này.
- **Cách chia đoạn:**
  - **Body 1 (Các nguồn chiếm tỷ trọng áp đảo: Coal & Gas):** Năm 1995 than đá 29.80%, khí đốt 29.63%. Sang 2005 cùng tăng nhẹ lên lần lượt 30.93% và 30.31%.
  - **Body 2 (Các nguồn còn lại: Nuclear, Other, Petrol):** Nuclear tăng từ 6.40% lên 10.10%; Other tăng từ 4.90% lên 9.10%. Trái lại, Petrol giảm từ 29.27% xuống 19.55%.""",
        "model_essay": """The two pie charts illustrate the proportion of five sources of energy production (coal, gas, nuclear, petrol and other sources) in France in two years (1995 and 2005).

Overall, in both years coal and gas accounted for over half of all energy production, while the least was other energy sources. There was only a very minimal increase in production from gas and coal, whereas nuclear and other sources almost doubled. Petrol was the only energy source to decrease over the period.

In 1995, energy produced by coal comprised 29.80% of the total energy production and this showed a marginal rise to 30.93% in 2005. Likewise, gas generated 29.63% in 1995, after which it experienced a negligible increase of around 1% to reach 30.31% in 2005. Together, these two fossil fuels continually represented approximately three-fifths of all power generated in France.

With regards to the remaining energy sources, petrol began as the second most prominent fuel at 29.27% in 1995, but plummeted significantly to 19.55% a decade later. In sharp contrast, nuclear energy saw its share swell from 6.40% to 10.10% over the ten-year timeframe. Similarly, other unspecified sources of power generation almost doubled, climbing from 4.90% to 9.10% by 2005.""",
        "vocab": [
            ("accounted for / comprised / generated", "/əˈkaʊntɪd fɔː/", "B2/C1", "Verb Collocation", "Chiếm tỉ lệ bao nhiêu phần trăm", "Coal and gas accounted for over half of all energy production."),
            ("marginal rise / negligible increase", "/ˈmɑːdʒɪnl raɪz/", "C1", "Noun Phrase", "Sự gia tăng rất nhỏ, không đáng kể", "...showed a marginal rise to 30.93%."),
            ("three-fifths of", "/θriː fɪfθs ɒv/", "B2/C1", "Fraction Paraphrase", "3/5 tổng số (tương đương 60%)", "...continually represented approximately three-fifths of all power."),
            ("with regards to", "/wɪð rɪˈɡɑːdz tuː/", "B2/C1", "Linking Phrase", "Xét về khía cạnh, đối với...", "With regards to the remaining energy sources..."),
            ("plummeted significantly", "/ˈplʌmɪtɪd sɪɡˈnɪfɪkəntli/", "C1", "Verb Phrase", "Lao dốc mạnh, giảm tụt dốc", "...but plummeted significantly to 19.55% a decade later."),
            ("in sharp contrast", "/ɪn ʃɑːp ˈkɒntrɑːst/", "C1", "Signpost", "Trái ngược hoàn toàn (tạo tính mạch lạc)", "In sharp contrast, nuclear energy saw its share swell..."),
            ("share swell from ... to ...", "/ʃeə swel/", "C2", "Phrase", "Thị phần / tỷ trọng phình to, tăng vọt từ... lên...", "...nuclear energy saw its share swell from 6.40% to 10.10%."),
            ("timeframe / a decade later", "/ˈtaɪmfreɪm/", "B2/C1", "Noun", "Khung thời gian / một thập kỷ sau đó", "...over the ten-year timeframe.")
        ],
        "grammar": [
            ("**Mệnh đề trạng ngữ chỉ sự tương phản 'whereas':** `There was only a very minimal increase..., whereas nuclear and other sources almost doubled.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md"),
            ("**Biến đổi phần trăm thành phân số tương đương (Fractions):** `...represented approximately three-fifths of all power...` (Tránh lặp đi lặp lại ký hiệu %).", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Mệnh đề phân từ hiện tại chỉ hệ quả:** `...almost doubled, climbing from 4.90% to 9.10% by 2005.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md")
        ],
        "guide": """- **Quy tắc xử lý Pie Chart:**
  - Đa dạng hóa cách diễn đạt tỷ lệ phần trăm: *accounted for X%, made up X%, comprised X%, represented X%, the proportion of X stood at Y%*.
  - Chuyển đổi linh hoạt giữa tỷ lệ % và phân số/tỷ lệ ước lượng: 50% = *a half*, 60% = *three-fifths*, 25% = *a quarter*, 75% = *three-quarters*.
  - So sánh trực diện sự tăng/giảm giữa 2 mốc năm cho từng nhóm chứ không nên liệt kê rời rạc năm 1995 xong mới liệt kê năm 2005."""
    },

    {
        "task": "task1",
        "type_folder": "table",
        "filename": "Sample_01_Consumer_Spending_Five_Countries.md",
        "title": "Consumer Spending in Five European Countries (2002)",
        "meta": {
            "task": "Task 1",
            "type": "Table",
            "topic": "Consumer Expenditure",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-table-band-9-model-answer/",
            "tags": ["ielts/writing", "task1/table", "topic/economy", "band/9"]
        },
        "prompt": "The table illustrates the proportion of consumer expenditure in Ireland, Italy, Spain, Sweden and Turkey on three types of consumer goods in 2002. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2014/11/cambridge-ielts-table.jpg",
        "outline": """- **Loại biểu đồ:** Bảng số liệu (Table) - So sánh chi tiêu của 5 quốc gia (Ireland, Italy, Spain, Sweden, Turkey) cho 3 nhóm mặt hàng (Food/Drinks/Tobacco, Clothing/Footwear, Leisure/Education) năm 2002.
- **Phân tích tổng quan (Overview):**
  1. Tất cả 5 quốc gia đều chi tiêu nhiều nhất cho hạng mục Thực phẩm, Đồ uống & Thuốc lá (Food, drinks and tobacco), gấp gần 3 lần các hạng mục khác.
  2. Ngược lại, chi tiêu cho Giải trí & Giáo dục (Leisure/Education) luôn ở mức thấp nhất ở cả 5 nước.
  3. Thổ Nhĩ Kỳ (Turkey) có tổng mức chi tiêu cho các nhóm hàng nhìn chung cao hơn 4 quốc gia còn lại.
- **Chiến lược chia đoạn:**
  - **Body 1 (Hạng mục lớn nhất - Food, Drinks & Tobacco):** Thổ Nhĩ Kỳ dẫn đầu (32.14%), theo sau là Ireland (28.91%), Tây Ban Nha và Ý (~16-18%), Thụy Điển thấp nhất (15.77%).
  - **Body 2 (Hai hạng mục còn lại - Clothing/Footwear & Leisure/Education):** Ý chi nhiều nhất cho Quần áo/Giày dép (9.00%), Thổ Nhĩ Kỳ cao nhất cho Giải trí/Giáo dục (4.35%), trong khi Thụy Điển thấp nhất cho quần áo (5.40%).""",
        "model_essay": """The table illustrates the proportion of consumer expenditure in Ireland, Italy, Spain, Sweden and Turkey on three types of consumer goods in 2002.

Overall, the category of consumer goods that all countries spent most on was food, drinks and tobacco, which was three times higher than on the other types of goods. The lowest spending could be seen in the category of leisure and education in all five countries. The outlay of Turkey was generally higher than the other four countries.

In terms of food, drinks and tobacco, Turkey had the highest proportion of expenditure with 32.14%, closely followed by Ireland at 28.91%. Spain and Italy allocated 18.80% and 16.36% of their spending to this sector respectively, while Sweden spent the lowest percentage of all, at only 15.77%.

Turning to the other two categories, Italy was the country which spent the highest proportion on clothing and footwear at 9.00%, in contrast to Sweden, where only 5.40% of expenditure was directed towards this category. Finally, Turkey recorded the highest percentage of consumer outlay on leisure and education at 4.35%, whereas the remaining nations spent between approximately 2% and 3.2% on this sector.""",
        "vocab": [
            ("consumer expenditure / outlay", "/kənˈsjuːmər ɪkˈspendɪtʃər/", "C1", "Noun", "Mức chi tiêu tiêu dùng của người dân", "The table illustrates the proportion of consumer expenditure..."),
            ("three times higher than", "/θriː taɪmz ˈhaɪər ðæn/", "B2/C1", "Comparative Structure", "Cao gấp 3 lần so với...", "...which was three times higher than on the other types of goods."),
            ("allocated ... to this sector", "/ˈæləkeɪtɪd/", "C1", "Verb Collocation", "Phân bổ bao nhiêu phần trăm chi tiêu cho ngành/nhóm hàng này", "Spain and Italy allocated 18.80% and 16.36% of their spending to this sector."),
            ("directed towards this category", "/dəˈrektɪd təˈwɔːdz/", "C1", "Passive Collocation", "Được hướng vào / dành cho nhóm này", "...only 5.40% of expenditure was directed towards this category."),
            ("in terms of", "/ɪn tɜːmz ɒv/", "B2", "Signpost", "Xét về khía cạnh nào đó", "In terms of food, drinks and tobacco..."),
            ("closely followed by", "/ˈkləʊsli ˈfɒləʊd baɪ/", "B2/C1", "Phrase", "Bám sát ngay phía sau bởi đối tượng nào", "Turkey had the highest proportion, closely followed by Ireland."),
            ("recorded the highest percentage", "/rɪˈkɔːdɪd/", "B2/C1", "Verb Collocation", "Ghi nhận tỷ lệ phần trăm cao nhất", "Turkey recorded the highest percentage of consumer outlay..."),
            ("the remaining nations", "/ðə rɪˈmeɪnɪŋ ˈneɪʃnz/", "B2/C1", "Noun Phrase", "Các quốc gia còn lại", "...whereas the remaining nations spent between 2% and 3.2%.")
        ],
        "grammar": [
            ("**Mệnh đề quan hệ không xác định so sánh:** `...food, drinks and tobacco, which was three times higher than on the other types of goods.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Cấu trúc câu chẻ nhấn mạnh (Cleft sentence):** `Italy was the country which spent the highest proportion on clothing...`", "Grammar & Cohesion/4. Advanced Grammar Topics/4.7. Cleft Sentences (Câu chẻ nhấn mạnh).md"),
            ("**Mệnh đề quan hệ với 'where':** `...in contrast to Sweden, where only 5.40% of expenditure was directed towards this category.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md")
        ],
        "guide": """- **Kỹ năng phân tích bảng số liệu (Table):**
  - Không đọc số theo từng hàng hoặc từng cột một cách đơn điệu! Phải tìm ra điểm cao nhất (highest) và thấp nhất (lowest) ở từng hạng mục.
  - Gom các số liệu tương đồng: Đặt nhóm hàng lớn nhất (Food & Tobacco) ở Body 1; 2 nhóm hàng nhỏ hơn ở Body 2.
  - Dùng các liên từ chuyển ý: *In terms of, Turning to, Finally, In contrast to* để kết nối mượt mà."""
    },

    {
        "task": "task1",
        "type_folder": "map",
        "filename": "Sample_01_Meadowside_Fonton_Development.md",
        "title": "Development of Meadowside and Fonton (1962 to Present)",
        "meta": {
            "task": "Task 1",
            "type": "Map Comparison",
            "topic": "Urban Development & Infrastructure",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-map-model-answer/",
            "tags": ["ielts/writing", "task1/map", "topic/urban_development", "band/9"]
        },
        "prompt": "The maps below show the changes that have taken place in Meadowside village and Fonton, a neighbouring town, since 1962. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2014/11/ielts-map-comparison-3-maps-201x300.jpg",
        "outline": """- **Loại biểu đồ:** Map (Bản đồ so sánh qua 3 mốc thời gian: 1962, 1985 và Hiện tại).
- **Khu vực:** Làng Meadowside và thị trấn lân cận Fonton.
- **Phân tích tổng quan (Overview):**
  1. Cả Fonton và Meadowside đều mở rộng diện tích đáng kể qua các năm cho đến khi hợp nhất làm một, biến Meadowside thành khu ngoại ô của Fonton.
  2. Cơ sở hạ tầng, nhà ở và các tiện ích công cộng đã có sự thay đổi và hiện đại hóa ngoạn mục.
- **Chiến lược phân chia đoạn thân bài:**
  - **Body 1 (Giai đoạn 1962 - 1985):** Năm 1962 hai khu vực tách biệt bởi đất trống. Đến 1985, Fonton mở rộng về phía Đông và Meadowside mở rộng về phía Tây; xuất hiện tuyến đường sắt và ga xe lửa kết nối hai nơi.
  - **Body 2 (Giai đoạn từ 1985 đến Hiện tại):** Hai khu vực sáp nhập hoàn toàn; xây dựng thêm tuyến đường tránh (bypass), bệnh viện lớn, công viên giải trí và khu thương mại mới.""",
        "model_essay": """The three maps illustrate how Meadowside village and Fonton, which is a nearby town, have developed from 1962 to the present.

Overall, both Fonton and Meadowside village increased in size over the years until they eventually merged together, at which point Meadowside became a suburb. Furthermore, there have been significant changes to infrastructure, housing and facilities over the period given.

In 1962, both Fonton and Meadowside were completely separate entities separated by a vast expanse of green fields. At this time, Fonton had a modest population of under 10,000, while Meadowside accommodated fewer than 1,000 residents. By 1985, substantial housing estates had been constructed to the east of Fonton and to the west of Meadowside, narrowing the distance between them. Moreover, a railway line and a station were built, providing direct transportation links across the two settlements.

From 1985 to the present day, the expansion continued relentlessly until Fonton and Meadowside completely merged, resulting in a joint metropolitan area with a combined population exceeding 60,000. In terms of modern infrastructure, a ring road was built circumventing the entire town. Additionally, a new shopping mall, an expansive leisure complex, and a large regional hospital were erected on former arable land, completely transforming the rural landscape into a modern suburban hub.""",
        "vocab": [
            ("merged together", "/mɜːdʒd təˈɡeðər/", "B2/C1", "Verb Collocation", "Sáp nhập lại với nhau thành một thể thống nhất", "...until they eventually merged together."),
            ("at which point", "/æt wɪtʃ pɔɪnt/", "C1", "Relative Clause Linker", "Vào thời điểm đó thì...", "...until they merged, at which point Meadowside became a suburb."),
            ("separate entities", "/ˈseprət ˈentətiz/", "C1", "Noun Phrase", "Các thực thể riêng biệt, tách rời nhau", "Both were completely separate entities separated by green fields."),
            ("expanse of green fields", "/ɪkˈspæns ɒv ɡriːn fiːldz/", "C2", "Noun Phrase", "Một vùng đất đồng cỏ xanh bao la trải dài", "...separated by a vast expanse of green fields."),
            ("housing estates", "/ˈhaʊzɪŋ ɪˈsteɪts/", "B2/C1", "Noun Phrase", "Các khu đô thị / khu dân cư nhà ở mới xây", "Substantial housing estates had been constructed."),
            ("railway line and a station", "/ˈreɪlweɪ laɪn/", "B2", "Noun", "Tuyến đường sắt và nhà ga", "A railway line and a station were built."),
            ("circumventing the town / ring road", "/ˌsɜːkəmˈventɪŋ/", "C2", "Verb / Noun", "Bao quanh thị trấn / Tuyến đường vành đai", "A ring road was built circumventing the entire town."),
            ("erected on former arable land", "/ɪˈrektɪd ɒn ˈfɔːmər ˈærəbl lænd/", "C1/C2", "Collocation", "Được xây dựng dựng lên trên đất nông nghiệp cũ", "A hospital was erected on former arable land.")
        ],
        "grammar": [
            ("**Quá khứ hoàn thành bị động cho các công trình đã hoàn thành:** `...substantial housing estates had been constructed...`", "Grammar & Cohesion/1. Tenses & Core Grammar/1.2. Past Tenses.md"),
            ("**Mệnh đề phân từ chỉ hệ quả chuyển hóa:** `..., resulting in a joint metropolitan area with a combined population...` và `..., completely transforming the rural landscape into...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Cụm giới từ chỉ phương hướng trong không gian địa lý:** `...to the east of Fonton and to the west of Meadowside...`", "Grammar & Cohesion/3. Prepositions, Gerunds & Infinitives/3.1. Basic Prepositions (Giới từ cơ bản).md")
        ],
        "guide": """- **Từ vựng cốt tử cho dạng Map:**
  - *Phương hướng chính xác:* north, south, east, west, north-east, south-west, to the east of...
  - *Động từ miêu tả xây dựng & mở rộng:* was constructed, was erected, expanded, widened, extended, merged, was demolished, was replaced by.
  - *Biến đổi chức năng đất đai:* transformed into, gave way to, converted into.
- **Thì của động từ:** Chú ý mốc thời gian trong quá khứ dùng Past Simple hoặc Past Perfect; mốc hiện tại dùng Present Perfect hoặc Present Simple."""
    },

    {
        "task": "task1",
        "type_folder": "process",
        "filename": "Sample_01_Rainwater_Harvesting_Process.md",
        "title": "Rainwater Harvesting & Treatment Process",
        "meta": {
            "task": "Task 1",
            "type": "Process Diagram",
            "topic": "Environment & Engineering",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/ielts-diagram/",
            "tags": ["ielts/writing", "task1/process", "topic/environment", "band/9"]
        },
        "prompt": "The diagram illustrates how rainwater is collected and treated for human consumption in an Australian town. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2026/04/IELTS-Rainwater-Diagram-2026-1024x663.jpg",
        "outline": """- **Loại biểu đồ:** Quy trình nhân tạo (Man-made process - Thu gom và xử lý nước mưa thành nước uống).
- **Phân tích tổng quan (Overview):**
  1. Quy trình gồm nhiều giai đoạn tuần tự khép kín: thu gom từ mái nhà -> lọc thô loại bỏ cặn bẩn -> dẫn vào bể chứa -> khử trùng bằng hóa chất -> phân phối ngược lại cho các hộ gia đình.
  2. Nước mưa sau khi qua hệ thống xử lý sẽ đạt chuẩn uống trực tiếp (fit for human consumption).
- **Chiến lược chia đoạn:**
  - **Body 1 (Giai đoạn Thu gom & Lọc sơ cấp):** Nước mưa rơi xuống mái nhà, chảy qua máng xối (gutter) -> qua bộ lọc (water filter) để loại bỏ rác/cặn -> dẫn theo đường ống ngầm vào bồn chứa (storage tank).
  - **Body 2 (Giai đoạn Xử lý Hóa chất & Phân phối tiêu dùng):** Nước từ bồn chứa được bơm sang trạm xử lý nước (water treatment) -> thêm hóa chất làm sạch vi khuẩn -> bơm theo hệ thống ống dẫn ngược về vòi nước của các hộ gia đình.""",
        "model_essay": """The diagram illustrates the sequential process by which rainwater is harvested and treated for drinking purposes in an Australian town.

Overall, rainwater is collected from the roofs of residential houses and then passes through a multi-stage filtering and chemical treatment system before being pumped back into the municipal water supply for domestic consumption.

At the beginning of the procedure, rain falls onto the rooftops of houses and flows down drainage pipes through a guttering system. The runoff first passes through a specialized water filter designed to remove large debris and impurities. Once filtered, the water continues along underground pipes until it reaches a secure storage tank, where it is held prior to further refinement.

From this storage facility, the water is piped into an adjacent water treatment unit. At this critical stage of the operation, specific chemical compounds are introduced into the water to eliminate any remaining bacteria and contaminants, thereby making it completely safe and fit for human consumption. Once the purification process is concluded, the potable water travels along a network of distribution pipes directly back into households, supplying clean drinking water for the local residents.""",
        "vocab": [
            ("sequential process", "/sɪˈkwenʃl ˈprəʊses/", "C1", "Noun Phrase", "Quy trình diễn ra tuần tự theo các bước", "The diagram illustrates the sequential process by which..."),
            ("harvested and treated", "/ˈhɑːvɪstɪd ænd ˈtriːtɪd/", "B2/C1", "Passive Collocation", "Được thu gom và xử lý", "...rainwater is harvested and treated for drinking purposes."),
            ("fit for human consumption", "/fɪt fɔː ˈhjuːmən kənˈsʌmpʃn/", "C1", "Idiomatic Phrase", "Đạt chuẩn an toàn để con người sử dụng", "...thereby making it completely safe and fit for human consumption."),
            ("debris and impurities", "/ˈdebriː ænd ɪmˈpjʊərətiz/", "C1", "Noun Phrase", "Rác thải vụn và các tạp chất", "...designed to remove large debris and impurities."),
            ("drainage pipes / guttering system", "/ˈdreɪnɪdʒ paɪps/", "B2/C1", "Noun", "Đường ống thoát nước / Hệ thống máng xối mái nhà", "...flows down drainage pipes through a guttering system."),
            ("chemical compounds are introduced", "/ˈkemɪkl ˈkɒmpaʊndz/", "C1", "Passive Collocation", "Các hợp chất hóa học được đưa/châm vào", "Specific chemical compounds are introduced into the water."),
            ("purification process / potable water", "/ˌpjʊərɪfɪˈkeɪʃn/ - /ˈpəʊtəbl/", "C1/C2", "Noun", "Quy trình làm sạch tinh khiết / Nước uống an toàn", "Once the purification process is concluded, the potable water travels..."),
            ("distribution pipes", "/ˌdɪstrɪˈbjuːʃn paɪps/", "B2/C1", "Noun Phrase", "Mạng lưới đường ống phân phối", "...travels along a network of distribution pipes back into households.")
        ],
        "grammar": [
            ("**Sử dụng Thể bị động (Passive Voice) xuyên suốt quy trình:** `is collected, is filtered, is piped, are introduced, is concluded.` (Quy trình nhân tạo luôn ưu tiên Passive Voice vì đối tượng thực hiện không quan trọng).", "Grammar & Cohesion/4. Advanced Grammar Topics/4.1. Passive Voice (Câu bị động).md"),
            ("**Các từ nối chỉ thứ tự thời gian (Time linkers):** `At the beginning of..., Once filtered..., From this point..., At this critical stage..., Once concluded...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md"),
            ("**Cụm phân từ hiện tại chỉ mục đích và hệ quả:** `..., supplying clean drinking water for the local residents.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md")
        ],
        "guide": """- **Quy tắc vàng cho Process Diagram:**
  - Luôn sử dụng thì **Hiện tại đơn (Present Simple)** và dạng **Bị động (Passive Voice)** cho quy trình nhân tạo.
  - Sử dụng các từ chỉ thứ tự các bước: *Initially, In the initial stage, Subsequently, Following this, Concurrently, The final phase involves...*
  - Không được bỏ sót bất kỳ bước hay chi tiết quan trọng nào được thể hiện trên sơ đồ hình vẽ."""
    },

    {
        "task": "task1",
        "type_folder": "mixed_chart",
        "filename": "Sample_01_Glasgow_Education_Levels.md",
        "title": "Education Levels in Glasgow by Age and Gender (2010)",
        "meta": {
            "task": "Task 1",
            "type": "Mixed Chart (Bar & Pie Charts)",
            "topic": "Education & Demographics",
            "band_target": 9.0,
            "source": "IELTS Liz",
            "source_url": "https://ieltsliz.com/dec-2016-ielts-writing-task-1-sample-answer/",
            "tags": ["ielts/writing", "task1/mixed_chart", "topic/education", "band/9"]
        },
        "prompt": "The bar chart and pie charts illustrate the percentage of people in Glasgow having three levels of education (university, school and those with no qualifications) in 2010. Information is divided into five age groups in the bar chart and by gender in the pie charts. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
        "image_url": "https://ieltsliz.com/wp-content/uploads/2099/07/Multiple-Task-of-Two-Charts-IELTS-Writing-Task-1.png",
        "outline": """- **Loại biểu đồ:** Multiple / Mixed Charts:
  - 1 Bar chart: Phân bố 3 mức học vấn (University, School, No qualifications) theo 5 nhóm tuổi.
  - 2 Pie charts: Cơ cấu học vấn theo giới tính (Men vs Women).
- **Phân tích tổng quan (Overview):**
  1. Đại đa số người có bằng đại học thuộc các nhóm tuổi trẻ, trong khi ở nhóm tuổi cao nhất hầu hết không có bằng cấp.
  2. Tỷ lệ giữa nam và nữ có sự tương đồng rất lớn và chênh lệch không đáng kể ở mọi trình độ học vấn.
- **Chiến lược chia đoạn:**
  - **Body 1 (Phân tích Bar Chart - Nhóm tuổi):** Nêu bật xu hướng đối nghịch: tỷ lệ có bằng đại học cao ở nhóm trẻ (lên tới 76%), giảm dần về già (chỉ 25% ở nhóm trên 75 tuổi); ngược lại người không bằng cấp tăng mạnh từ 9% ở người trẻ lên 72% ở người già. Tỷ lệ có bằng phổ thông dao động quanh 20%.
  - **Body 2 (Phân tích Pie Charts - Giới tính):** Tỷ lệ phân bổ giữa nam và nữ ở 3 mức học vấn gần như ngang ngửa nhau, mỗi nhóm chiếm khoảng 1/3, độ chênh lệch tối đa giữa 2 giới chỉ là 3%.""",
        "model_essay": """The bar chart and pie charts illustrate the percentage of people in Glasgow having three levels of education (university, school and those with no qualifications) in 2010. Information is divided into five age groups in the bar chart and by gender in the pie charts.

Overall, the majority of people with university education were in younger age groups, while in the oldest age group most people did not have any qualifications. The proportions of men and women were remarkably similar and showed very little difference across all three educational levels.

Looking first at the bar chart, the percentage of people with university education was up to 76% in the younger three age groups, compared to only 50% in those aged 50 to 75 and just 25% in those over 75. This trend was diametrically reversed among citizens with no qualifications, where the figure stood at a mere 9% for younger individuals but surged to 72% in the oldest cohort. Meanwhile, the proportion of individuals with school-level education remained relatively constant at around 20% across most brackets, but plunged to as low as 3% in the over-75 demographic.

Turning to the pie charts, the distribution between genders was exceptionally balanced. Approximately one third of both men and women held a university qualification, with a negligible gap of only 3% (32% for women and 35% for men). A similarly minimal disparity was observed among those without qualifications, while the figures for school qualifications were virtually identical between the sexes.""",
        "vocab": [
            ("educational qualifications", "/ˌedʒuˈkeɪʃənl ˌkwɒlɪfɪˈkeɪʃnz/", "B2/C1", "Noun Phrase", "Bằng cấp / trình độ học vấn", "...having three levels of education or qualifications."),
            ("diametrically reversed", "/ˌdaɪəˈmetrɪkli rɪˈvɜːst/", "C2", "Collocation", "Hoàn toàn đảo ngược theo hướng đối lập", "This trend was diametrically reversed among citizens with no qualifications."),
            ("oldest cohort / demographic", "/ˈkəʊhɔːt/ - /ˌdeməˈɡræfɪk/", "C1", "Noun", "Nhóm nhân khẩu học / thế hệ cao tuổi nhất", "...surged to 72% in the oldest cohort."),
            ("remained relatively constant", "/rɪˈmeɪnd ˈrelətɪvli ˈkɒnstənt/", "B2/C1", "Collocation", "Giữ mức tương đối ổn định", "Remained relatively constant at around 20% across most brackets."),
            ("exceptionally balanced", "/ɪkˈsepʃənəli ˈbælənst/", "C1", "Collocation", "Cực kỳ cân bằng, đồng đều", "The distribution between genders was exceptionally balanced."),
            ("negligible gap / minimal disparity", "/ˈneɡlɪdʒəbl ɡæp/ - /dɪˈspærəti/", "C1/C2", "Noun Phrase", "Khoảng cách không đáng kể / sự chênh lệch tối thiểu", "With a negligible gap of only 3%... A similarly minimal disparity was observed."),
            ("virtually identical", "/ˈvɜːtʃuəli aɪˈdentɪkl/", "C1", "Collocation", "Gần như giống hệt nhau 100%", "...were virtually identical between the sexes."),
            ("age brackets", "/eɪdʒ ˈbrækɪts/", "B2/C1", "Noun", "Các nhóm khung độ tuổi", "...across most brackets.")
        ],
        "grammar": [
            ("**Cấu trúc đối chiếu nhiều chiều:** `...was up to 76% in younger groups, compared to only 50% in those aged 50 to 75 and just 25% in those over 75.`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md"),
            ("**Mệnh đề quan hệ rút gọn diễn tả sự đảo ngược:** `This trend was diametrically reversed among citizens with no qualifications, where the figure stood at a mere 9%... but surged to 72%...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.1. Sentence Elements & Types.md"),
            ("**Rút gọn chủ ngữ với 'Turning to':** `Turning to the pie charts, the distribution between genders was...`", "Grammar & Cohesion/2. Sentence Structures & Writing/2.3. Sentence Linkers & Paragraph Cohesion.md")
        ],
        "guide": """- **Kỹ thuật làm chủ dạng Mixed Chart (Biểu đồ kết hợp):**
  - Đừng bối rối khi thấy 2 loại biểu đồ khác nhau! Bí quyết là **chia để trị**:
    - **Body 1:** Dành trọn vẹn để phân tích Biểu đồ thứ nhất (Bar chart).
    - **Body 2:** Dành trọn vẹn để phân tích Biểu đồ thứ hai (Pie charts).
  - Phần **Overview** bắt buộc phải rút ra 1 đặc điểm nổi bật nhất của biểu đồ thứ nhất + 1 đặc điểm nổi bật nhất của biểu đồ thứ hai."""
    }
]

def generate():
    for item in essays:
        task_dir = os.path.join(BASE_DIR, item["task"], item["type_folder"])
        os.makedirs(task_dir, exist_ok=True)
        file_path = os.path.join(task_dir, item["filename"])

        # Format YAML
        tags_str = "\n".join([f"  - {t}" for t in item["meta"]["tags"]])
        yaml_header = f"""---
task: {item["meta"]["task"]}
type: {item["meta"]["type"]}
topic: {item["meta"]["topic"]}
band_target: {item["meta"]["band_target"]}
source: "{item["meta"]["source"]}"
source_url: "{item["meta"]["source_url"]}"
tags:
{tags_str}
---"""

        # Format Vocab Table
        vocab_rows = []
        for word, ipa, level, wtype, vn, ex in item["vocab"]:
            vocab_rows.append(f"| **{word}** | `{ipa}` | `{level}` | *{wtype}* | {vn} | *\"{ex}\"* |")
        vocab_table = "\n".join(vocab_rows)

        # Format Grammar
        grammar_list = []
        for g_desc, g_link in item["grammar"]:
            grammar_list.append(f"1. {g_desc}\n   - 🔗 *Tài liệu đối chiếu:* [[{g_link}]]")
        grammar_str = "\n".join(grammar_list)

        # Image if available
        image_sec = ""
        if "image_url" in item and item["image_url"]:
            image_sec = f"""
> [!NOTE] Minh Họa Đề Bài
> ![]({item["image_url"]})
"""

        content = f"""{yaml_header}

# {item["title"]}

> [!QUESTION] Đề Bài (Exam Prompt)
> *{item["prompt"]}*
{image_sec}
---

## 1. 💡 Phân Tích Đề & Dàn Ý Logic (Idea & Outline)
{item["outline"]}

---

## 2. 📝 Bài Viết Mẫu Chuẩn (Band {item["meta"]["band_target"]} Model Answer)
{item["model_essay"]}

---

## 3. 💎 Kho Từ Vựng & Collocations "Ăn Điểm" (Lexical Resource)

| Từ vựng / Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa ngắn gọn | Ngữ cảnh ứng dụng trong bài |
| :--- | :--- | :---: | :---: | :--- | :--- |
{vocab_table}

---

## 4. 🛠️ Cấu Trúc Ngữ Pháp Đắt Giá (Grammar & Cohesion)
{grammar_str}

---

## 5. 🎯 Hướng Dẫn Tự Viết & Template Ứng Dụng (Actionable Guide)
{item["guide"]}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created: {file_path}")

if __name__ == "__main__":
    generate()
