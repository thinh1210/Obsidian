import os

BASE_DIR = "/home/thinh/Obsidian/English/Writing"

task1_guides = {
    "bar_chart": {
        "name": "Bar Chart (Biểu đồ cột)",
        "icon": "📊",
        "index_filename": "0_Bar_Chart_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Paraphrase lại đề bài bằng cách thay đổi chủ ngữ, động từ và cách biểu đạt thời gian (VD: *The bar chart illustrates/depicts the amount of money spent on...*).
2. **Overview (1 - 2 câu quan trọng nhất):**
   - Chỉ ra đối tượng có số liệu cao nhất/thấp nhất (Highest / Lowest).
   - Chỉ ra sự khác biệt hoặc cách biệt lớn nhất giữa các nhóm (Most significant disparity).
   - *Lưu ý tuyệt đối:* Không đưa số liệu chi tiết vào Overview!
3. **Body Paragraph 1 (3 - 4 câu - Nhóm số liệu nổi bật / cao nhất):**
   - Gom nhóm 2-3 cột có giá trị cao nhất hoặc cùng xu hướng nổi trội.
   - So sánh trực tiếp giữa các đối tượng bằng các liên từ đối chiếu (*while, whereas, as opposed to*).
4. **Body Paragraph 2 (3 - 4 câu - Nhóm số liệu còn lại / thấp nhất):**
   - Báo cáo nhóm số liệu thấp hơn hoặc các điểm dị biệt (anomalies).
   - Nêu số liệu cụ thể kèm đơn vị đo chuẩn xác (*pounds sterling, million tons, percentage*).""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **illustrates / depicts** | `/ˈɪləstreɪts/ - /dɪˈpɪkts/` | Verb | Minh họa, mô tả trực quan số liệu |
| **expenditure on / outlay on** | `/ɪkˈspendɪtʃər ɒn/` | Collocation | Mức chi tiêu / số tiền bỏ ra cho mặt hàng nào |
| **as opposed to / in comparison with** | `/æz əˈpəʊzd tuː/` | Phrase | Trái ngược với / so sánh tương phản với |
| **respectively** | `/rɪˈspektɪvli/` | Adverb | Lần lượt theo thứ tự liệt kê trước đó |
| **outstrip / surpass** | `/aʊtˈstrɪp/ - /səˈpɑːst/` | Verb | Vượt xa, bỏ xa đối tượng còn lại |
| **marked disparity / noticeable gap** | `/mɑːkt dɪˈspærəti/` | Noun Phrase | Sự chênh lệch / khoảng cách rõ rệt |
| **stand at / account for** | `/stænd æt/` | Verb Collocation | Đứng ở mức... / chiếm tỉ trọng... |
| **the figures for [X] and [Y]** | `/ðə ˈfɪɡəz fɔː/` | Phrase | Số liệu đại diện cho đối tượng X và Y |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The bar chart provides a comparative breakdown of [đối tượng khảo sát] in terms of [tiêu chí đo lường] across [địa điểm/thời gian].*
- **Overview:** *Overall, it is readily apparent that [Đối tượng A] dominated the chart, whereas the reverse was true for [Đối tượng B]. Furthermore, the most pronounced difference between [Nhóm 1] and [Nhóm 2] was observed in [Hạng mục C].*

#### B. Mẫu câu So sánh & Báo cáo số liệu Thân bài:
- **So sánh hơn:** *[Subject A] spent significantly more on [Category], with figures standing at [Số liệu 1] compared to merely [Số liệu 2] for [Subject B].*
- **Đối chiếu kép:** *Both [A] and [B] allocated the vast majority of their budget to [Item 1], whereas expenditure on [Item 2] was marginal, registering at only [Số liệu].*
- **Lần lượt theo thứ tự:** *Expenditure on [X] and [Y] was recorded at [Số 1] and [Số 2] respectively.*"""
    },

    "line_graph": {
        "name": "Line Graph (Biểu đồ đường)",
        "icon": "📈",
        "index_filename": "0_Line_Graph_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Paraphrase đề bài (biểu đồ thể hiện sự biến thiên/thay đổi của các yếu tố qua một khoảng thời gian).
2. **Overview (1 - 2 câu):**
   - Chỉ ra xu hướng chung của các đường (Đường nào tăng chung, đường nào giảm chung, đường nào giữ nguyên/dao động).
   - Nêu đối tượng dẫn đầu ở điểm đầu và điểm cuối thời kỳ (Highest starting point vs Final winner).
3. **Body Paragraph 1 (3 - 4 câu - Các đường có cùng xu hướng chính):**
   - Gom các đường có cùng quỹ đạo (VD: các đường cùng giảm hoặc cùng tăng mạnh).
   - Mô tả mốc khởi đầu, tốc độ thay đổi và các bước ngoặt quan trọng.
4. **Body Paragraph 2 (3 - 4 câu - Các đường đối nghịch / có điểm giao cắt):**
   - Phân tích đường có xu hướng ngược lại.
   - Nhấn mạnh điểm giao cắt (intersection point/overtaking) và số liệu chốt sổ cuối kỳ.""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **upward / downward trajectory** | `/ˈʌpwəd trəˈdʒektəri/` | Noun Phrase | Quỹ đạo đi lên / quỹ đạo sụt giảm |
| **surge / climb sharply** | `/sɜːdʒ/ - /klaɪm ˈʃɑːpli/` | Verb + Adv | Tăng vọt, tăng đột biến trong thời gian ngắn |
| **plummet / plunge** | `/ˈplʌmɪt/ - /plʌndʒ/` | Verb | Lao dốc, tụt giảm cực mạnh |
| **peak at / reach a zenith of** | `/piːkt æt/ - /ˈzenɪθ/` | Collocation | Đạt đỉnh điểm tại mức nào đó |
| **bottom out at / hit a trough** | `/ˈbɒtəm aʊt æt/ - /trɒf/` | Collocation | Chạm đáy, rơi xuống mức thấp nhất rồi chững lại |
| **plateau / level off** | `/ˈplætəʊ/ - /ˈlevl ɒf/` | Verb | Giữ nguyên mức ổn định sau một chu kỳ tăng/giảm |
| **fluctuate wildly / erratically** | `/ˈflʌktʃueɪt ˈwaɪldli/` | Collocation | Biến động mạnh, dao động trồi sụt thất thường |
| **overtake / surpass that of** | `/ˌəʊvəˈteɪk/ - /səˈpɑːst/` | Verb Phrase | Vượt qua số liệu của đối tượng khác |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The line graph illustrates changes in the consumption/levels of [X, Y, and Z] over a [N]-year period between [Năm 1] and [Năm 2].*
- **Overview:** *Overall, while the figures for [X and Y] exhibited an overall downward trend, [Z] witnessed a remarkable climb. Additionally, [X] was the most dominant category initially, but was ultimately overtaken by [Z] by the end of the timeframe.*

#### B. Mẫu câu Mô tả Xu hướng & Giao cắt:
- **Mô tả tăng vọt:** *Beginning at [Số liệu] in [Năm], the figure for [X] experienced a steep ascent, peaking at [Số liệu đỉnh] in [Năm].*
- **Mô tả sụt giảm liên tục:** *Conversely, [Y] followed a persistent downward trajectory, plunging from [Số 1] to a trough of [Số 2].*
- **Điểm vượt mặt:** *Around [Năm], consumption of [Z] surpassed that of [X], thereby becoming the predominant category.*"""
    },

    "pie_chart": {
        "name": "Pie Chart (Biểu đồ tròn)",
        "icon": "🥧",
        "index_filename": "0_Pie_Chart_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Paraphrase đề bài (biểu đồ thể hiện cơ cấu phần trăm / tỷ trọng phân bổ của các phân khúc).
2. **Overview (1 - 2 câu):**
   - Chỉ ra phân khúc chiếm tỷ trọng áp đảo (The dominant segment / majority share).
   - Chỉ ra phân khúc nhỏ nhất hoặc phân khúc có sự biến động ngoạn mục nhất qua các năm.
3. **Body Paragraph 1 (3 - 4 câu - Các phần tư / phân khúc chủ chốt):**
   - Mô tả các mảng chiếm trên 50% hoặc 2 mảng lớn nhất.
   - So sánh trực tiếp cơ cấu giữa các năm hoặc giữa các đối tượng.
4. **Body Paragraph 2 (3 - 4 câu - Các phân khúc nhỏ & sự biến động):**
   - Mô tả các phần nhỏ còn lại, sử dụng linh hoạt phân số (*half, third, quarter, fifth*).""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **account for / constitute / comprise** | `/əˈkaʊnt fɔː/ - /ˈkɒnstɪtjuːt/` | Verb | Chiếm bao nhiêu phần trăm tổng thể |
| **represent the lion's share of** | `/ðə ˈlaɪənz ʃeər ɒv/` | Idiom | Chiếm phần lớn nhất, áp đảo nhất |
| **vast bulk of / overwhelming majority** | `/væst bʌlk ɒv/` | Noun Phrase | Đại bộ phận, phần đa số áp đảo |
| **marginal fraction / negligible proportion** | `/ˈmɑːdʒɪnl ˈfrækʃn/` | Noun Phrase | Một tỷ lệ rất nhỏ, không đáng kể |
| **swell from ... to ...** | `/swel/` | Verb | Phình to, tăng mạnh tỷ trọng từ... lên... |
| **diminish / shrink significantly** | `/dɪˈmɪnɪʃ/ - /ʃrɪŋk/` | Verb + Adv | Thu hẹp đáng kể thị phần/tỷ trọng |
| **two-fifths / three-quarters** | `/tuː fɪfθs/` | Fraction | Cách gọi phân số (2/5 = 40%, 3/4 = 75%) |
| **a negligible gap of** | `/ə ˈneɡlɪdʒəbl ɡæp ɒv/` | Collocation | Một khoảng cách chênh lệch không đáng kể |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The pie charts delineate the proportional distribution of [đối tượng] across [các hạng mục] in [Năm 1] and [Năm 2].*
- **Overview:** *Overall, [Category A and B] constituted the vast majority of the total throughout the period, whereas [Category C] made up the smallest fraction. Furthermore, [Category D] recorded the most noticeable expansion.*

#### B. Mẫu câu Phân tích Tỷ trọng:
- **Chiếm phần lớn:** *In [Năm], [Category A] represented the lion's share of total production at [X]%, followed closely by [B] at [Y]%.*
- **Phân số thay thế:** *Together, these two sectors accounted for approximately three-fifths of the overall energy mix.*
- **Sự thu hẹp/Mở rộng:** *Over the decade in question, the share of [C] swelled from [X]% to [Y]%, whereas that of [D] shrunk to merely [Z]%.*"""
    },

    "table": {
        "name": "Table (Bảng số liệu)",
        "icon": "📋",
        "index_filename": "0_Table_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Paraphrase tiêu đề bảng số liệu (các hạng mục, quốc gia/đơn vị và thời điểm).
2. **Overview (1 - 2 câu):**
   - Khái quát hàng hoặc cột có giá trị tổng thể cao nhất/thấp nhất.
   - Nhận diện hạng mục có sự chênh lệch sâu sắc nhất giữa các đối tượng.
3. **Body Paragraph 1 (3 - 4 câu - Hạng mục chủ đạo / Số liệu lớn nhất):**
   - Phân tích chi tiết hạng mục dẫn đầu qua các nước/tiêu chí.
   - So sánh mức độ phân bổ vốn, chi tiêu hoặc số lượng.
4. **Body Paragraph 2 (3 - 4 câu - Các hạng mục thứ cấp & Nhóm số liệu nhỏ):**
   - Báo cáo các hạng mục còn lại, nêu rõ quốc gia/đơn vị giữ vị trí đầu và cuối bảng.""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **allocate ... to / direct towards** | `/ˈæləkeɪt/ - /dəˈrekt/` | Verb Collocation | Phân bổ / rót tiền, nguồn lực vào lĩnh vực nào |
| **in terms of / with respect to** | `/ɪn tɜːmz ɒv/` | Phrase | Xét về phương diện, liên quan tới... |
| **closely followed by** | `/ˈkləʊsli ˈfɒləʊd baɪ/` | Phrase | Được bám sát ngay phía sau bởi... |
| **register / document the lowest figure** | `/ˈredʒɪstər/ - /ˈdɒkjument/` | Verb Phrase | Ghi nhận con số thấp nhất |
| **corresponding figure** | `/ˌkɒrəˈspɒndɪŋ ˈfɪɡər/` | Noun Phrase | Con số tương ứng ở đối tượng đối chiếu |
| **an anomaly / outlier** | `/əˈnɒməli/ - /ˈaʊtlaɪər/` | Noun | Điểm dị biệt, trường hợp ngoại lệ khác thường |
| **expenditure outlay** | `/ɪkˈspendɪtʃər ˈaʊtleɪ/` | Noun | Khoản chi tiêu tài chính |
| **rank highest / lowest** | `/ræŋk ˈhaɪɪst/` | Verb Phrase | Xếp hạng cao nhất / thấp nhất |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The table provides a detailed breakdown of [tiêu chí] across [số lượng] different [quốc gia/nhóm] in [Năm].*
- **Overview:** *Overall, [Category 1] represented the highest area of expenditure across all surveyed nations, whereas [Category 2] consistently ranked lowest. Furthermore, the overall outlay of [Country A] generally surpassed that of its counterparts.*

#### B. Mẫu câu So sánh & Liệt kê Số liệu:
- **Đứng đầu bảng:** *In terms of [Category A], [Country 1] took the lead with [X]%, closely followed by [Country 2] at [Y]%.*
- **Số liệu tương ứng:** *[Country 3] allocated [A]% to this sector, while the corresponding figures for [Country 4] and [Country 5] stood at [B]% and [C]% respectively.*
- **Đối chiếu cực đoan:** *At the other end of the spectrum, [Country 6] recorded the lowest outlay in all measured categories.*"""
    },

    "map": {
        "name": "Map (Bản đồ biến đổi địa lý / đô thị)",
        "icon": "🗺️",
        "index_filename": "0_Map_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Giới thiệu khu vực địa lý và khung thời gian quy hoạch/biến đổi (từ năm X đến năm Y hoặc đến Hiện tại).
2. **Overview (1 - 2 câu):**
   - Nêu nét chuyển mình lớn nhất (VD: Từ nông thôn thành đô thị hiện đại, mở rộng diện tích, sáp nhập 2 thị trấn).
   - Nêu bật sự phát triển của cơ sở hạ tầng giao thông và dịch vụ công cộng.
3. **Body Paragraph 1 (3 - 4 câu - Khu vực phía Bắc / Giai đoạn đầu):**
   - Mô tả hiện trạng ban đầu và các công trình được xây dựng/thay thế đầu tiên.
4. **Body Paragraph 2 (3 - 4 câu - Khu vực phía Nam / Giai đoạn sau):**
   - Mô tả các công trình quy mô lớn hoàn thiện sau cùng (đường tránh, bệnh viện, khu dân cư mới).""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **be erected / constructed** | `/ɪˈrektɪd/ - /kənˈstrʌktɪd/` | Passive Verb | Được xây dựng, dựng lên |
| **demolished / knocked down** | `/dɪˈmɒlɪʃt/ - /nɒkt daʊn/` | Passive Verb | Bị phá dỡ, san phẳng |
| **flattened to make way for** | /ˈflætnd tuː meɪk weɪ fɔː/` | Passive Phrase | Bị san phẳng để nhường chỗ xây công trình mới |
| **transform into / converted into** | `/trænsˈfɔːm ˈɪntuː/` | Verb Collocation | Biến đổi hoàn toàn thành... |
| **ring road / bypass** | `/rɪŋ rəʊd/ - /ˈbaɪpɑːs/` | Noun | Tuyến đường vành đai / đường tránh bao quanh |
| **residential area / housing estates** | `/ˌrezɪˈdenʃl ˈeəriə/` | Noun Phrase | Khu dân cư, khu đô thị nhà ở |
| **arable land / green fields** | /ˈærəbl lænd/ - /ɡriːn fiːldz/` | Noun Phrase | Đất canh tác nông nghiệp / bãi cỏ tự nhiên |
| **suburban hub / merged together** | `/səˈbɜːbən hʌb/ - /mɜːdʒd/` | Collocation | Trung tâm ngoại ô sầm uất / sáp nhập lại với nhau |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The maps depict the architectural and infrastructural transformations that occurred in [Địa danh] between [Năm 1] and [Năm 2/the present day].*
- **Overview:** *Overall, the area underwent dramatic modernization, transforming from a largely rural settlement into a bustling suburban hub. The most prominent developments included the expansion of residential zones and the modernization of transport infrastructure.*

#### B. Mẫu câu Miêu tả Vị trí & Sự Thay thế:
- **Thay thế công trình cũ:** *The old industrial warehouse in the north-east was completely demolished to make way for a state-of-the-art medical facility.*
- **Xây mới trên đất trống:** *A vast expanse of farmland situated to the south of the river was repurposed for substantial housing estates.*
- **Mở rộng giao thông:** *Transport links were substantially enhanced with the construction of a dual carriageway circumventing the main town center.*"""
    },

    "process": {
        "name": "Process (Quy trình sản xuất / Tự nhiên)",
        "icon": "⚙️",
        "index_filename": "0_Process_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 câu):** Paraphrase quy trình (mô tả cách thức một sản phẩm được làm ra hoặc chu kỳ tự nhiên diễn ra).
2. **Overview (1 - 2 câu):**
   - Đếm rõ tổng số bước (stages/steps).
   - Chỉ ra điểm bắt đầu (vật liệu thô) và điểm kết thúc (thành phẩm cuối cùng/tiêu thụ).
3. **Body Paragraph 1 (3 - 4 câu - Nửa đầu quy trình):**
   - Thu gom nguyên liệu, sơ chế, nghiền, lọc hoặc xử lý ban đầu.
4. **Body Paragraph 2 (3 - 4 câu - Nửa sau quy trình):**
   - Tinh chế, khử trùng/nung nhiệt, đóng chai/bao bì và vận chuyển phân phối.""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **sequential process** | `/sɪˈkwenʃl ˈprəʊses/` | Noun Phrase | Quy trình diễn biến tuần tự từng bước |
| **commences with / begins by** | `/kəˈmensɪz wɪð/` | Verb Collocation | Khởi đầu bằng hành động gì |
| **undergo refinement / purification** | `/ˌʌndəˈɡəʊ rɪˈfaɪnmənt/` | Collocation | Trải qua quá trình tinh chế / làm sạch |
| **subsequently / concurrently** | `/ˈsʌbsɪkwəntli/ - /kənˈkʌrəntli/` | Adverb | Sau đó tiếp theo / Diễn ra đồng thời song song |
| **piped into / channeled into** | `/paɪpt ˈɪntuː/ - /ˈtʃænld/` | Passive Verb | Được bơm qua đường ống vào / dẫn dòng vào |
| **be subjected to heat / chemicals** | `/səbˈdʒektɪd tuː/` | Passive Collocation | Được đem đi xử lý nhiệt độ / hóa chất |
| **the final phase culminates in** | `/ˈkʌlmɪneɪts ɪn/` | Verb Collocation | Giai đoạn cuối cùng khép lại ở việc... |
| **potable water / finished product** | /ˈpəʊtəbl/ - /ˈfɪnɪʃt ˈprɒdʌkt/` | Noun Phrase | Nước uống được an toàn / Thành phẩm hoàn chỉnh |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The diagram illustrates the sequential stages involved in the manufacturing of [Sản phẩm] / the biological life cycle of [Sinh vật].*
- **Overview:** *Overall, the procedure comprises [N] distinct phases, commencing with the extraction of raw materials and culminating in the commercial distribution of the finished product.*

#### B. Mẫu câu Kết nối các Bước Tuần tự:
- **Bước đầu:** *In the initial stage of the process, [nguyên liệu] is gathered and delivered to a processing facility.*
- **Bước tiếp theo (dùng phân từ hoàn thành):** *Having been filtered to remove impurities, the liquid is subsequently channeled into high-pressure boilers.*
- **Bước cuối:** *Once the cooling phase is concluded, the items are packaged securely and transported to retail outlets.*"""
    },

    "mixed_chart": {
        "name": "Mixed Chart (Biểu đồ kết hợp đa dạng)",
        "icon": "📑",
        "index_filename": "0_Mixed_Chart_Index.md",
        "structure": """### 1. Cấu Trúc Báo Cáo Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (1 - 2 câu):** Giới thiệu từng biểu đồ một cách gãy gọn (Biểu đồ 1 thể hiện cái gì VÀ Biểu đồ 2 cung cấp thông tin gì).
2. **Overview (2 câu tách biệt):**
   - Câu 1: Rút ra xu hướng/đặc điểm nổi bật nhất của **Biểu đồ 1**.
   - Câu 2: Rút ra xu hướng/đặc điểm nổi bật nhất của **Biểu đồ 2**.
3. **Body Paragraph 1 (3 - 4 câu):** Báo cáo và so sánh số liệu chuyên sâu dành riêng cho **Biểu đồ 1**.
4. **Body Paragraph 2 (3 - 4 câu):** Báo cáo và đối chiếu số liệu chuyên sâu dành riêng cho **Biểu đồ 2** (tìm mối liên hệ nếu có).""",
        "vocab": """| Thuật ngữ / Cụm từ | Phiên âm IPA | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :--- |
| **divided into ... and categorized by** | `/dɪˈvaɪdɪd ˈɪntuː/` | Passive Phrase | Được chia thành... và phân loại theo... |
| **diametrically reversed** | `/ˌdaɪəˈmetrɪkli rɪˈvɜːst/` | Collocation | Hoàn toàn đảo ngược theo hướng đối lập |
| **age brackets / cohorts** | `/eɪdʒ ˈbrækɪts/ - /ˈkəʊhɔːts/` | Noun Phrase | Các khung độ tuổi / nhóm nhân khẩu học |
| **exceptionally balanced** | `/ɪkˈsepʃənəli ˈbælənst/` | Collocation | Vô cùng cân bằng, gần như đồng đều tuyệt đối |
| **turning to the pie charts** | /ˈtɜːnɪŋ tuː/` | Signpost | Chuyển sự chú ý sang biểu đồ tròn (từ nối mạch lạc) |
| **virtually identical** | `/ˈvɜːtʃuəli aɪˈdentɪkl/` | Collocation | Gần như y hệt nhau, không có khác biệt |
| **negligible disparity** | `/ˈneɡlɪdʒəbl dɪˈspærəti/` | Noun Phrase | Sự chênh lệch quá nhỏ không đáng kể |
| **mirrored the pattern of** | /ˈmɪrəd ðə ˈpætn ɒv/` | Collocation | Phản ánh / mô phỏng lại y hệt xu hướng của... |""",
        "templates": """#### A. Mẫu câu Introduction & Overview:
- **Intro:** *The bar chart illustrates [Thông tin 1], while the accompanying pie charts depict [Thông tin 2] in the year [Năm].*
- **Overview:** *Overall, [Đặc điểm 1 của biểu đồ thứ nhất]. Regarding the secondary chart, [Đặc điểm 2 của biểu đồ thứ hai].*

#### B. Mẫu câu Tách Biệt Thân bài:
- **Thân bài 1 (Biểu đồ thứ nhất):** *Looking first at the bar chart, the proportion of [A] stood at [X]% for [Nhóm 1], before experiencing a sharp drop to merely [Y]% in [Nhóm 2].*
- **Thân bài 2 (Biểu đồ thứ hai):** *Turning to the pie charts, the distribution between [X and Y] was remarkably homogenous, with both genders registering approximately one third across all surveyed categories.*"""
    }
}

task2_guides = {
    "agree_disagree": {
        "name": "Agree or Disagree (Quan điểm / Opinion Essay)",
        "icon": "⚖️",
        "index_filename": "0_Agree_Disagree_Index.md",
        "structure": """### 1. Cấu Trúc Bài Luận Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (2 câu):**
   - *Sentence 1 (Background Statement):* Paraphrase lại ý kiến/vấn đề trong đề bài.
   - *Sentence 2 (Thesis Statement):* Nêu rõ quan điểm của bạn ngay từ đầu (Hoàn toàn đồng ý / Hoàn toàn không đồng ý / Đồng ý một phần có điều kiện).
2. **Body Paragraph 1 (Reason 1 - 4-5 câu):**
   - *Topic Sentence:* Khẳng định lý do đầu tiên ủng hộ quan điểm của bạn.
   - *Explanation:* Đào sâu nguyên nhân tại sao điều này đúng (Why is this the case?).
   - *Example:* Đưa ví dụ thực tế hoặc số liệu/nghiên cứu minh họa.
   - *Mini-Conclusion/Result:* Khẳng định hệ quả tích cực/tiêu cực.
3. **Body Paragraph 2 (Reason 2 hoặc Mặt bổ trợ - 4-5 câu):**
   - *Topic Sentence:* Nêu lý do quan trọng thứ hai (hoặc điều kiện bổ trợ nếu chọn góc nhìn cân bằng).
   - *Explanation & Example:* Phát triển ý tương tự Thân bài 1.
4. **Conclusion (1 - 2 câu):** Khẳng định lại quan điểm và tóm tắt 2 lý do then chốt (Không đưa ý tưởng mới vào kết bài!).""",
        "vocab": """| Từ vựng / Cụm Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :---: | :--- |
| **advocate / champion** | `/ˈædvəkeɪt/ - /ˈtʃæmpiən/` | C1 | Verb | Ủng hộ mạnh mẽ một quan điểm/chính sách |
| **compelling justification** | `/kəmˈpelɪŋ ˌdʒʌstɪfɪˈkeɪʃn/` | C2 | Noun Phrase | Lý do / sự biện minh cực kỳ thuyết phục |
| **exert a detrimental effect on** | `/ɪɡˈzɜːt ə ˌdetrɪˈmentl/` | C1 | Collocation | Gây tác động tiêu cực, tổn hại đến cái gì |
| **be of paramount importance** | `/ɒv ˈpærəmaʊnt ɪmˈpɔːtns/` | C2 | Phrase | Có tầm quan trọng tối thượng, cốt tử |
| **indispensable prerequisite** | `/ˌɪndɪˈspensəbl ˌpriːˈrekwəzɪt/` | C2 | Noun Phrase | Điều kiện tiên quyết không thể thiếu |
| **counteract / mitigate** | `/ˌkaʊntərˈækt/ - /ˈmɪtɪɡeɪt/` | C1 | Verb | Giảm thiểu, triệt tiêu tác hại tiêu cực |
| **far-reaching ramifications** | /ˈfɑː riːtʃɪŋ ˌræmɪfɪˈkeɪʃnz/` | C2 | Noun Phrase | Những hệ lụy / tác động sâu rộng |
| **untenable assertion** | `/ʌnˈtenəbl əˈsɜːʃn/` | C2 | Noun Phrase | Một luận điểm thiếu căn cứ, khó bảo vệ |""",
        "templates": """#### A. Mẫu câu Mở bài (Thesis Statements):
- **Một chiều tuyệt đối (Strong Stance):** *While some argue that [quan điểm đối lập], I completely agree/disagree with this assertion because [Lý do 1] and [Lý do 2].*
- **Cân bằng một phần (Balanced Stance):** *I agree that [Ý kiến A] represents a viable approach; however, I firmly believe that [Ý kiến B] must also be prioritized to ensure comprehensive results.*

#### B. Mẫu câu Triển khai Thân bài:
- **Topic Sentence 1:** *The primary justification for my viewpoint is that [Luận điểm 1].*
- **Giải thích sâu:** *In other words, when [Hành động xảy ra], it inevitably leads to [Hệ quả tất yếu].*
- **Đưa ví dụ minh họa:** *A prominent instance of this is [Ví dụ thực tế], which clearly demonstrates that [Ý đúc kết].*
- **Chuyển đoạn Thân bài 2:** *Furthermore, another persuasive reason supporting this stance pertains to [Luận điểm 2].*

#### C. Mẫu câu Kết bài:
- *In conclusion, I reiterate my firm conviction that [Quan điểm của bạn]. As long as [Điều kiện xảy ra], this approach will undoubtedly foster [Lợi ích lâu dài].*"""
    },

    "discuss_both_views": {
        "name": "Discuss Both Views (Thảo luận 2 mặt & Nêu quan điểm)",
        "icon": "👥",
        "index_filename": "0_Discuss_Both_Views_Index.md",
        "structure": """### 1. Cấu Trúc Bài Luận Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (2 câu):**
   - *Sentence 1:* Giới thiệu 2 luồng quan điểm trái ngược của xã hội.
   - *Sentence 2 (Thesis):* Nêu rõ quan điểm cá nhân nghiêng về phía bên nào ngay tại mở bài.
2. **Body Paragraph 1 (Phân tích View 1 - 4-5 câu):**
   - Trình bày tại sao một nhóm người lại ủng hộ View 1 (*On the one hand, proponents of X argue that...*).
   - Đưa lập luận và ví dụ khách quan để chứng minh mặt hợp lý của họ.
3. **Body Paragraph 2 (Phân tích View 2 & Quan điểm của bạn - 4-5 câu):**
   - Phân tích View 2 (*On the other hand, it is believed that Y...*).
   - Khẳng định rõ tại sao bạn đồng tình với View này hơn (*From my perspective, this viewpoint carries greater weight because...*).
4. **Conclusion (1 - 2 câu):** Khẳng định lại tính hai mặt của vấn đề và chốt hạ quan điểm của bạn.""",
        "vocab": """| Từ vựng / Cụm Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :---: | :--- |
| **proponents / advocates of** | `/prəˈpəʊnənts/` | C1 | Noun | Những người ủng hộ luồng quan điểm nào đó |
| **opponents / detractors of** | `/əˈpəʊnənts/ - /dɪˈtræktəz/` | C1 | Noun | Những người phản đối, chỉ trích quan điểm đó |
| **carries greater weight** | /ˈkæriz ˈɡreɪtə weɪt/` | C1 | Idiom | Có trọng lượng hơn, thuyết phục hơn |
| **throw the balance in favour of** | `/θrəʊ ðə ˈbæləns/` | C2 | Idiom | Làm cán cân nghiêng hẳn về phía có lợi cho... |
| **the former ... the latter** | `/ðə ˈfɔːmə ... ðə ˈlætə/` | B2/C1 | Cohesive Pair | Cái đề cập trước ... cái đề cập sau |
| **transferable skills** | `/trænsˈfɜːrəbl skɪlz/` | C1 | Noun Phrase | Kỹ năng có thể chuyển giao linh hoạt giữa các ngành |
| **intellectual curiosity** | /ˌɪntəˈlektʃuəl ˌkjʊəriˈɒsəti/` | C2 | Noun Phrase | Niềm đam mê tìm tòi học thuật trí tuệ |
| **hands-on experience** | `/hændz ɒn ɪkˈspɪəriəns/` | B2/C1 | Noun Phrase | Kinh nghiệm thực tế cọ xát trực tiếp |""",
        "templates": """#### A. Mẫu câu Introduction & Thesis:
- *While it is commonly contended that [View A], others maintain that [View B]. In my estimation, although both stances have merit, I am more inclined to side with the latter due to [Lý do then chốt].*

#### B. Mẫu câu Thân bài:
- **Body 1 (View đối lập):** *On the one hand, there are compelling reasons why many people champion [View A]. Chief among these is that [Luận cứ 1]. For instance, [Dẫn chứng]...*
- **Body 2 (View ủng hộ):** *On the other hand, the argument for [View B] appears considerably stronger. Not only does this approach foster [Lợi ích 1], but it also ensures [Lợi ích 2]. From my personal perspective, [Khẳng định quan điểm cá nhân]...*

#### C. Mẫu câu Kết bài:
- *In conclusion, whilst acknowledging the rational basis of [View A], I firmly maintain that [View B] offers far superior advantages in the modern era.*"""
    },

    "problem_solution": {
        "name": "Cause / Problem & Solution (Nguyên nhân & Giải pháp)",
        "icon": "🔍",
        "index_filename": "0_Problem_Solution_Index.md",
        "structure": """### 1. Cấu Trúc Bài Luận Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (2 câu):**
   - *Sentence 1:* Nêu thực trạng đáng báo động của vấn đề được đưa ra trong đề bài.
   - *Sentence 2 (Thesis):* Khẳng định vấn đề này bắt nguồn từ nhiều nguyên nhân phức tạp và đòi hỏi các biện pháp can thiệp đồng bộ.
2. **Body Paragraph 1 (Nguyên nhân cốt lõi - Causes / Problems - 4-5 câu):**
   - Trình bày **2 nguyên nhân chính**: Nguyên nhân 1 (chủ quan/cá nhân) và Nguyên nhân 2 (khách quan/xã hội/hệ thống).
3. **Body Paragraph 2 (Các giải pháp đối ứng - Solutions - 4-5 câu):**
   - Đưa ra **2 giải pháp đối ứng trực tiếp** giải quyết dứt điểm 2 nguyên nhân ở Body 1 (Giải pháp 1 của Chính phủ/Tổ chức, Giải pháp 2 của Cá nhân/Cộng đồng).
4. **Conclusion (1 - 2 câu):** Tóm lược lại tính cấp bách của vấn đề và khẳng định tính khả thi của các giải pháp.""",
        "vocab": """| Từ vựng / Cụm Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :---: | :--- |
| **root cause / catalyst of** | `/ruːt kɔːz/ - /ˈkætəlɪst/` | C1 | Noun Phrase | Căn nguyên cốt lõi / chất xúc tác châm ngòi |
| **stem from / be attributed to** | `/stem frɒm/ - /əˈtrɪbjuːtɪd/` | C1 | Verb Collocation | Xuất phát từ / được quy cho nguyên nhân nào |
| **alleviate / mitigate the dilemma** | `/əˈliːvieɪt/ - /ˈmɪtɪɡeɪt/` | C1 | Verb Phrase | Xoa dịu / làm thuyên giảm tình thế nan giải |
| **enact stringent legislation** | `/ɪˈnækt ˈstrɪndʒənt/` | C2 | Collocation | Ban hành luật pháp cứng rắn, nghiêm ngặt |
| **a multifaceted approach** | `/ə ˌmʌltiˈfæsɪtɪd əˈprəʊtʃ/` | C2 | Noun Phrase | Phương pháp tiếp cận đa diện, toàn diện |
| **rehabilitation programs** | `/ˌriːəˌbɪlɪˈteɪʃn/` | C1 | Noun Phrase | Các chương trình cải tạo, phục hồi nhân phẩm |
| **timely intervention** | `/ˈtaɪmli ˌɪntəˈvenʃn/` | C1 | Noun Phrase | Sự can thiệp đúng lúc, kịp thời |
| **curb this worrying trend** | `/kɜːb ðɪs ˈwʌriɪŋ trend/` | C1 | Collocation | Ngăn chặn, kiềm chế xu hướng đáng lo ngại này |""",
        "templates": """#### A. Mẫu câu Introduction & Thesis:
- *In contemporary society, [Hiện tượng] has emerged as a grave concern posing significant challenges. This perplexing phenomenon primarily stems from [Nguyên nhân A and B]; nevertheless, it can be effectively mitigated through targeted intervention.*

#### B. Mẫu câu Triển khai Thân bài:
- **Body 1 (Nguyên nhân):** *A multitude of factors account for this dilemma. First and foremost, [Nguyên nhân 1]. This is compounded by the fact that [Nguyên nhân 2]...*
- **Body 2 (Giải pháp đối ứng):** *To curb this issue, a concerted effort from both governing bodies and individuals is imperative. One pragmatic measure is for authorities to [Giải pháp 1]. Additionally, on a community level, [Giải pháp 2] should be fostered...*

#### C. Mẫu câu Kết bài:
- *In conclusion, whilst [Vấn đề] remains a daunting challenge driven by [Tóm tắt nguyên nhân], implementing [Tóm tắt giải pháp] will undoubtedly provide a sustainable remedy.*"""
    },

    "advantages_disadvantages": {
        "name": "Advantages & Disadvantages (Lợi ích & Bất lợi)",
        "icon": "⚖️",
        "index_filename": "0_Advantages_Disadvantages_Index.md",
        "structure": """### 1. Cấu Trúc Bài Luận Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (2 câu):**
   - *Sentence 1:* Dẫn dắt xu hướng/sự phát triển được nêu trong đề bài.
   - *Sentence 2 (Thesis):* Nêu rõ sự tồn tại song song của cả ưu điểm và nhược điểm. Nếu đề bài hỏi *"Do the advantages outweigh the disadvantages?"*, bắt buộc phải khẳng định rõ mặt nào chiếm ưu thế hơn.
2. **Body Paragraph 1 (Phân tích các Ưu điểm - Advantages - 4-5 câu):**
   - Trình bày 2 ưu điểm nổi bật (Ví dụ: Đẩy mạnh kinh tế, gắn kết quốc tế).
3. **Body Paragraph 2 (Phân tích các Nhược điểm - Disadvantages - 4-5 câu):**
   - Trình bày các rủi ro, mặt trái (Ví dụ: Đánh mất bản sắc văn hóa, chi phí môi trường).
4. **Conclusion (1 - 2 câu):** Cân nhắc tổng thể và đưa ra kết luận dứt khoát về tác động lâu dài.""",
        "vocab": """| Từ vựng / Cụm Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :---: | :--- |
| **merits / boons / virtues** | `/ˈmerɪts/ - /buːnz/` | C1 | Noun | Những lợi ích, phước lành, điểm cộng |
| **pitfalls / drawbacks / downsides** | /ˈpɪtfɔːlz/ - /ˈdrɔːbæks/` | C1 | Noun | Những cạm bẫy, mặt trái, hạn chế tiêu cực |
| **eclipses / overshadows** | `/ɪˈklɪpsɪz/ - /ˌəʊvəˈʃædəʊz/` | C2 | Verb | Che khuất, áp đảo hoàn toàn (vượt trội hơn hẳn) |
| **predominate over** | `/prɪˈdɒmɪneɪt ˈəʊvər/` | C2 | Verb | Chiếm vị thế thống soái, áp đảo hoàn toàn |
| **indispensable asset** | `/ˌɪndɪˈspensəbl ˈæset/` | C1 | Collocation | Tài sản vô giá, không thể thiếu |
| **loss of cultural identity** | `/lɒs ɒv ˈkʌltʃərəl aɪˈdentəti/`| C1 | Collocation | Sự đánh mất bản sắc văn hóa |
| **adverse repercussions** | `/ˈædvɜːs ˌriːpəˈkʌʃnz/` | C2 | Noun Phrase | Những phản ứng phụ, hậu quả bất lợi |
| **a double-edged sword** | `/ə ˌdʌbl edʒd sɔːd/` | C1 | Idiom | Con dao hai lưỡi (vừa có lợi vừa có hại) |""",
        "templates": """#### A. Mẫu câu Introduction & Thesis (Dạng Outweigh):
- *The tendency towards [Hiện tượng] has ignited intense debate regarding its overarching societal implications. While I acknowledge the noticeable benefits regarding [Mặt lợi], I firmly contend that the accompanying hazards significantly eclipse these advantages.*

#### B. Mẫu câu Thân bài:
- **Body 1 (Lợi ích):** *On the one hand, it is undeniable that [Hiện tượng] brings substantial boons. Primary among these is that [Lợi ích 1]. Furthermore, [Lợi ích 2]...*
- **Body 2 (Mặt trái):** *On the other hand, the aforementioned benefits are heavily counterbalanced by severe pitfalls. Chief among these is [Nhược điểm 1]. Moreover, [Nhược điểm 2]...*

#### C. Mẫu câu Kết bài:
- *In conclusion, while [Hiện tượng] offers undoubted economic/practical virtues, I remain convinced that its detrimental cultural/social impacts are far more substantial.*"""
    },

    "direct_questions": {
        "name": "Direct Questions (Câu hỏi trực tiếp / Hai câu hỏi)",
        "icon": "❓",
        "index_filename": "0_Direct_Questions_Index.md",
        "structure": """### 1. Cấu Trúc Bài Luận Chuẩn (Standard 4-Paragraph Structure)
1. **Introduction (2 câu):**
   - *Sentence 1:* Paraphrase vấn đề được đưa ra ở tiền đề.
   - *Sentence 2 (Thesis):* Trả lời trực tiếp và ngắn gọn cả 2 câu hỏi của đề bài trong một câu phức hoàn chỉnh.
2. **Body Paragraph 1 (Dành riêng trả lời trọn vẹn Câu hỏi 1 - 4-5 câu):**
   - Đưa câu trả lời dứt khoát ngay tại Topic Sentence.
   - Phát triển lý lẽ và ví dụ chi tiết cho Câu hỏi 1.
3. **Body Paragraph 2 (Dành riêng trả lời trọn vẹn Câu hỏi 2 - 4-5 câu):**
   - Đưa câu trả lời cho Câu hỏi 2.
   - Phân tích sâu 2-3 nhân tố hoặc giải pháp liên quan.
4. **Conclusion (1 - 2 câu):** Tóm tắt câu trả lời cho cả hai câu hỏi một cách trang trọng.""",
        "vocab": """| Từ vựng / Cụm Collocation | Phiên âm IPA | Cấp độ | Phân loại | Định nghĩa & Ngữ cảnh áp dụng |
| :--- | :--- | :---: | :---: | :--- |
| **hinge on / rely upon** | `/hɪndʒ ɒn/` | C1 | Phrasal Verb | Phụ thuộc hoàn toàn vào điều gì |
| **profound contentment** | `/prəˈfaʊnd kənˈtentmənt/` | C2 | Noun Phrase | Sự bằng lòng, thỏa nguyện thanh thản sâu sắc |
| **fulfilling social bonds** | `/fʊlˈfɪlɪŋ ˈsəʊʃl bɒndz/` | C1 | Noun Phrase | Các mối quan hệ xã hội gắn kết, ý nghĩa |
| **unconditional emotional support** | `/ˌʌnkənˈdɪʃənl ɪˈməʊʃənl səˈpɔːt/`| C1| Noun Phrase | Sự hỗ trợ tinh thần vô điều kiện |
| **cornerstones of human joy** | /ˈkɔːnəstəʊnz/` | C2 | Metaphor | Những viên đá tảng / nền móng cho hạnh phúc |
| **altruistic contribution** | `/ˌæltruˈɪstɪk ˌkɒntrɪˈbjuːʃn/` | C2 | Noun Phrase | Sự cống hiến vị tha vì cộng đồng |
| **play an indispensable role in** | /ˈplæt ən ˌɪndɪˈspensəbl rəʊl/`| C1 | Collocation | Đóng vai trò thiết yếu không thể thay thế |
| **temporary gratification** | `/ˈtemprəri ˌɡrætɪfɪˈkeɪʃn/` | C2 | Noun Phrase | Sự thỏa mãn nhất thời |""",
        "templates": """#### A. Mẫu câu Introduction & Thesis:
- *In current times, the issue of [Chủ đề] has garnered widespread discussion. In response to the first inquiry, I firmly believe that [Trả lời câu 1]; regarding the second question, [Trả lời câu 2] play an indispensable role.*

#### B. Mẫu câu Thân bài:
- **Body 1 (Trả lời câu hỏi 1):** *Addressing the first query, it is entirely feasible for individuals to [Trả lời Q1]. The primary explanation is that [Lý do 1]. Furthermore, [Lý do 2]...*
- **Body 2 (Trả lời câu hỏi 2):** *Turning to the second question, a variety of other factors contribute significantly to [Vấn đề]. Foremost among these is [Nhân tố A]. Additionally, [Nhân tố B] is equally paramount because [Giải thích]...*

#### C. Mẫu câu Kết bài:
- *To recapitulate, [Tóm tắt trả lời câu 1]. Simultaneously, [Tóm tắt trả lời câu 2] remain the definitive pillars determining this outcome.*"""
    }
}

def generate_index_content(task, folder, info):
    dir_path = os.path.join(BASE_DIR, task, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    files = [f for f in os.listdir(dir_path) if f.endswith(".md") and not f.startswith("0_")]
    files.sort()
    
    rows = []
    for f in files:
        fpath = os.path.join(dir_path, f)
        title = f.replace(".md", "")
        with open(fpath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        topic = "General"
        band = "8.5+"
        for line in lines:
            if line.startswith("topic:"):
                topic = line.split(":", 1)[1].strip()
            elif line.startswith("band_target:"):
                band = line.split(":", 1)[1].strip()
            elif line.startswith("# "):
                title = line.replace("# ", "").strip()
                break
                
        note_name = f.replace(".md", "")
        rows.append(f"| [[{note_name}]] | `{band}` | `{topic}` | [[{note_name}#2. 📝 Bài Viết Mẫu Chuẩn|Xem Bài Mẫu]] | [[{note_name}#3. 💎 Kho Từ Vựng & Collocations \"Ăn Điểm\"|Tra Từ Vựng]] | [[{note_name}#5. 🎯 Hướng Dẫn Tự Viết & Template Ứng Dụng|Cách Viết]] |")

    table_content = "\n".join(rows) if rows else "| *Đang cập nhật thêm bài mẫu* | - | - | - | - | - |"

    md = f"""---
task: {task.upper()}
type: {info["name"]}
tags:
  - ielts/writing
  - index/{folder}
---

# {info["icon"]} Cẩm Nang Dạng Bài: {info["name"]}

> [!TIP] Bản Đồ Chiến Lược Dạng Bài
> File Index này đóng vai trò như một **bộ cẩm nang hoàn chỉnh** cho dạng bài **{info["name"]}**, bao gồm:
> - **Cấu trúc khung chuẩn 4 đoạn**
> - **Kho từ vựng & Collocations cốt lõi**
> - **Ngân hàng mẫu câu ăn điểm (Sentence Frames)**
> - **Danh sách các bài mẫu Band 8.5 - 9.0 đã được phân tích sâu**

---

## 🏛️ I. Cấu Trúc Khung Chuẩn (Essay / Report Architecture)

{info["structure"]}

---

## 💎 II. Kho Từ Vựng & Collocations Cốt Lõi (Lexical Resource)

{info["vocab"]}

---

## 🎯 III. Ngân Hàng Mẫu Câu Ăn Điểm (High-Scoring Sentence Frames)

{info["templates"]}

---

## 📚 IV. Danh Sách Bài Mẫu Đã Phân Tích (Curated Sample Essays)

| Tiêu Đề Bài Học | Band | Chủ Đề | Bài Mẫu | Tra Từ Vựng | Hướng Dẫn Viết |
| :--- | :---: | :--- | :---: | :---: | :---: |
{table_content}

---

## 🤖 V. Quy Chuẩn Tiếp Nhận & Thêm Bài Mới Từ Người Dùng
Khi bạn muốn thêm bài mẫu hoặc đưa đề bài mới cho dạng bài này, hệ thống sẽ tự động thực hiện:
1. **Tiếp nhận đề bài:** Bẻ khóa câu hỏi, xác định hướng tiếp cận logic tối ưu.
2. **Soạn bài mẫu Band 8.5 - 9.0:** Sử dụng văn phong tự nhiên, học thuật và chính xác tuyệt đối.
3. **Phân tích 5 chiều:** Dàn ý logic $\\rightarrow$ Bài mẫu $\\rightarrow$ Bảng từ vựng kèm IPA & nghĩa tiếng Việt $\\rightarrow$ Cấu trúc ngữ pháp đắt giá $\\rightarrow$ Hướng dẫn tự viết.
4. **Tự động liên kết:** Tạo file `Sample_XX_[Topic].md` trong thư mục này và cập nhật bảng mục lục ở trên.
"""
    file_path = os.path.join(dir_path, info["index_filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md.strip() + "\n")
    print(f"Upgraded: {file_path}")

def main():
    for folder, info in task1_guides.items():
        generate_index_content("task1", folder, info)
    for folder, info in task2_guides.items():
        generate_index_content("task2", folder, info)

if __name__ == "__main__":
    main()
