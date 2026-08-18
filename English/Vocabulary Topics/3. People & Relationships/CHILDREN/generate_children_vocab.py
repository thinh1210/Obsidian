import os

target_dir = "/home/thinh/Documents/Obsidian Vault/English/Vocabulary Topics/3. People & Relationships/CHILDREN"
os.makedirs(target_dir, exist_ok=True)

vocab = [
    # A1-A2 (15)
    {
        "word": "Child", "pos": "noun", "ipa": "/tʃaɪld/", "lvl": "A1", "ctx": "Daily",
        "en": "A young human being.", "vn": "Trẻ em, đứa trẻ.",
        "m": "Child giống tiếng 'chài', bắt cá chài trẻ con.",
        "col": ["`only child`: con một"],
        "ex1": "The child is playing.", "ex1v": "Đứa trẻ đang chơi.",
        "ex2": "Child psychology is complex.", "ex2v": "Tâm lý học trẻ em rất phức tạp.",
        "ex3": "Look at that child!", "ex3v": "Nhìn đứa trẻ kia kìa!",
        "fam": "Childhood (n), Childless (adj)", "syn": "Kid", "ant": "Adult"
    },
    {
        "word": "Baby", "pos": "noun", "ipa": "/ˈbeɪ.bi/", "lvl": "A1", "ctx": "Daily",
        "en": "A very young child.", "vn": "Em bé.",
        "m": "Baby khóc oe oe.",
        "col": ["`have a baby`: sinh con"],
        "ex1": "The baby is sleeping.", "ex1v": "Em bé đang ngủ.",
        "ex2": "Baby food is expensive.", "ex2v": "Thức ăn trẻ em rất đắt.",
        "ex3": "Nobody puts Baby in a corner.", "ex3v": "Không ai được bắt nạt Baby.",
        "fam": "Babyhood (n)", "syn": "Infant", "ant": "Adult"
    },
    {
        "word": "Boy", "pos": "noun", "ipa": "/bɔɪ/", "lvl": "A1", "ctx": "Daily",
        "en": "A male child.", "vn": "Cậu bé, con trai.",
        "m": "Boy (boi) -> bơi, cậu bé đi bơi.",
        "col": ["`little boy`: cậu bé nhỏ"],
        "ex1": "The boy is running.", "ex1v": "Cậu bé đang chạy.",
        "ex2": "A boy's education is important.", "ex2v": "Giáo dục cho một cậu bé là quan trọng.",
        "ex3": "That boy is trouble.", "ex3v": "Cậu bé đó là một rắc rối.",
        "fam": "Boyhood (n)", "syn": "Lad", "ant": "Girl"
    },
    {
        "word": "Girl", "pos": "noun", "ipa": "/ɡɜːrl/", "lvl": "A1", "ctx": "Daily",
        "en": "A female child.", "vn": "Cô bé, con gái.",
        "m": "Girl xinh gái.",
        "col": ["`baby girl`: bé gái"],
        "ex1": "The girl is reading.", "ex1v": "Cô bé đang đọc sách.",
        "ex2": "Girl empowerment is a global goal.", "ex2v": "Trao quyền cho trẻ em gái là mục tiêu toàn cầu.",
        "ex3": "You go, girl!", "ex3v": "Cố lên cô gái!",
        "fam": "Girlhood (n)", "syn": "Lass", "ant": "Boy"
    },
    {
        "word": "Son", "pos": "noun", "ipa": "/sʌn/", "lvl": "A1", "ctx": "Daily",
        "en": "A boy or man in relation to his parents.", "vn": "Con trai.",
        "m": "Son giống sun (mặt trời), con trai là mặt trời của mẹ.",
        "col": ["`eldest son`: con trai cả"],
        "ex1": "He is my son.", "ex1v": "Nó là con trai tôi.",
        "ex2": "His son inherited the business.", "ex2v": "Con trai ông ấy kế thừa việc kinh doanh.",
        "ex3": "Luke, I am your father.", "ex3v": "Luke, ta là cha con.",
        "fam": "Son-in-law (n)", "syn": "Male offspring", "ant": "Daughter"
    },
    {
        "word": "Daughter", "pos": "noun", "ipa": "/ˈdɔː.tər/", "lvl": "A1", "ctx": "Daily",
        "en": "A girl or woman in relation to her parents.", "vn": "Con gái.",
        "m": "Daughter giống đó tớ (đó là tớ), con gái tớ.",
        "col": ["`only daughter`: con gái duy nhất"],
        "ex1": "She is my daughter.", "ex1v": "Cô ấy là con gái tôi.",
        "ex2": "Her daughter graduated today.", "ex2v": "Con gái cô ấy đã tốt nghiệp hôm nay.",
        "ex3": "My daughter is my world.", "ex3v": "Con gái là thế giới của tôi.",
        "fam": "Daughter-in-law (n)", "syn": "Female offspring", "ant": "Son"
    },
    {
        "word": "Kid", "pos": "noun", "ipa": "/kɪd/", "lvl": "A1", "ctx": "Daily",
        "en": "A child or young person.", "vn": "Đứa trẻ, nhóc.",
        "m": "Kid là kít, ăn kẹo kít cát.",
        "col": ["`kid sister`: em gái nhỏ"],
        "ex1": "The kids are playing outside.", "ex1v": "Bọn trẻ đang chơi bên ngoài.",
        "ex2": "The kid needs supervision.", "ex2v": "Đứa trẻ cần được giám sát.",
        "ex3": "Here's looking at you, kid.", "ex3v": "Chúc em may mắn, cô bé.",
        "fam": "Kidding (v)", "syn": "Child", "ant": "Adult"
    },
    {
        "word": "Toy", "pos": "noun", "ipa": "/tɔɪ/", "lvl": "A1", "ctx": "Daily",
        "en": "An object for a child to play with.", "vn": "Đồ chơi.",
        "m": "Toy giống tòi, đồ chơi lòi ra.",
        "col": ["`soft toy`: thú nhồi bông"],
        "ex1": "He bought a new toy.", "ex1v": "Cậu ấy đã mua một món đồ chơi mới.",
        "ex2": "The toy industry is booming.", "ex2v": "Ngành công nghiệp đồ chơi đang bùng nổ.",
        "ex3": "You are a toy!", "ex3v": "Cậu là một món đồ chơi!",
        "fam": "Toy (v)", "syn": "Plaything", "ant": "None"
    },
    {
        "word": "Play", "pos": "verb", "ipa": "/pleɪ/", "lvl": "A1", "ctx": "Daily",
        "en": "Engage in activity for enjoyment.", "vn": "Chơi.",
        "m": "Play là p-lây, lây niềm vui.",
        "col": ["`play outside`: chơi ngoài trời"],
        "ex1": "The children play in the park.", "ex1v": "Bọn trẻ chơi trong công viên.",
        "ex2": "Play is essential for development.", "ex2v": "Vui chơi là cần thiết cho sự phát triển.",
        "ex3": "Wanna play a game?", "ex3v": "Muốn chơi một trò chơi không?",
        "fam": "Playful (adj), Player (n)", "syn": "Amuse oneself", "ant": "Work"
    },
    {
        "word": "Cry", "pos": "verb", "ipa": "/kraɪ/", "lvl": "A1", "ctx": "Daily",
        "en": "Shed tears.", "vn": "Khóc.",
        "m": "Cry giống cờ rai, khóc vì cờ rớt.",
        "col": ["`cry out`: khóc to"],
        "ex1": "The baby started to cry.", "ex1v": "Em bé bắt đầu khóc.",
        "ex2": "The infant's cry indicates hunger.", "ex2v": "Tiếng khóc của trẻ sơ sinh cho thấy nó đói.",
        "ex3": "Boys don't cry.", "ex3v": "Con trai không khóc.",
        "fam": "Crying (n)", "syn": "Weep", "ant": "Laugh"
    },
    {
        "word": "Laugh", "pos": "verb", "ipa": "/læf/", "lvl": "A1", "ctx": "Daily",
        "en": "Make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement.", "vn": "Cười.",
        "m": "Laugh nghe như lấp, lấp liếm bằng nụ cười.",
        "col": ["`laugh out loud`: cười to"],
        "ex1": "The kids laugh a lot.", "ex1v": "Bọn trẻ cười rất nhiều.",
        "ex2": "Humor makes students laugh.", "ex2v": "Sự hài hước làm học sinh cười.",
        "ex3": "Don't make me laugh.", "ex3v": "Đừng làm tôi cười.",
        "fam": "Laughter (n)", "syn": "Giggle", "ant": "Cry"
    },
    {
        "word": "Young", "pos": "adj", "ipa": "/jʌŋ/", "lvl": "A1", "ctx": "Daily",
        "en": "Having lived or existed for only a short time.", "vn": "Trẻ tuổi.",
        "m": "Young giống răng, còn trẻ còn răng.",
        "col": ["`young people`: người trẻ"],
        "ex1": "She is very young.", "ex1v": "Cô ấy còn rất trẻ.",
        "ex2": "The young generation adapts quickly.", "ex2v": "Thế hệ trẻ thích nghi nhanh chóng.",
        "ex3": "We are young.", "ex3v": "Chúng ta còn trẻ.",
        "fam": "Youth (n)", "syn": "Youthful", "ant": "Old"
    },
    {
        "word": "Parent", "pos": "noun", "ipa": "/ˈper.ənt/", "lvl": "A1", "ctx": "Daily",
        "en": "A father or mother.", "vn": "Cha hoặc mẹ.",
        "m": "Parent giống ba-rèn, ba rèn con.",
        "col": ["`single parent`: bố mẹ đơn thân"],
        "ex1": "My parent is here.", "ex1v": "Cha mẹ tôi ở đây.",
        "ex2": "Parental consent is required.", "ex2v": "Cần có sự đồng ý của phụ huynh.",
        "ex3": "I am a parent now.", "ex3v": "Bây giờ tôi đã làm cha mẹ.",
        "fam": "Parental (adj), Parenthood (n)", "syn": "Guardian", "ant": "Child"
    },
    {
        "word": "Born", "pos": "adj", "ipa": "/bɔːrn/", "lvl": "A1", "ctx": "Daily",
        "en": "Existing as a result of birth.", "vn": "Được sinh ra.",
        "m": "Born giống bon, chạy bon bon lúc mới sinh.",
        "col": ["`be born`: được sinh ra"],
        "ex1": "The baby was born yesterday.", "ex1v": "Em bé được sinh ra hôm qua.",
        "ex2": "Infants born prematurely need care.", "ex2v": "Trẻ sơ sinh sinh non cần được chăm sóc.",
        "ex3": "A star is born.", "ex3v": "Một ngôi sao đã ra đời.",
        "fam": "Birth (n)", "syn": "Created", "ant": "Dead"
    },
    {
        "word": "Grow", "pos": "verb", "ipa": "/ɡroʊ/", "lvl": "A1", "ctx": "Daily",
        "en": "Undergo natural development by increasing in size and changing physically.", "vn": "Lớn lên, phát triển.",
        "m": "Grow giống râu, lớn lên có râu.",
        "col": ["`grow up`: lớn lên"],
        "ex1": "Children grow fast.", "ex1v": "Trẻ em lớn rất nhanh.",
        "ex2": "Nutrition helps children grow.", "ex2v": "Dinh dưỡng giúp trẻ phát triển.",
        "ex3": "Grow up, Peter Pan!", "ex3v": "Lớn lên đi, Peter Pan!",
        "fam": "Growth (n), Grown (adj)", "syn": "Develop", "ant": "Shrink"
    },

    # B1-B2 (20)
    {
        "word": "Toddler", "pos": "noun", "ipa": "/ˈtɑːd.lɚ/", "lvl": "B1", "ctx": "Daily",
        "en": "A young child, usually one between one and three years of age.", "vn": "Trẻ mới biết đi.",
        "m": "Toddler giống 'tót lơ', trẻ đi tót lơ ngơ.",
        "col": ["`toddler group`: nhóm trẻ chập chững"],
        "ex1": "My toddler loves playing with blocks.", "ex1v": "Đứa trẻ mới biết đi của tôi thích chơi xếp hình.",
        "ex2": "Toddler development includes motor skills.", "ex2v": "Sự phát triển của trẻ mới biết đi bao gồm các kỹ năng vận động.",
        "ex3": "He's just a toddler.", "ex3v": "Nó chỉ là một đứa trẻ mới biết đi.",
        "fam": "Toddle (v)", "syn": "Little child", "ant": "Adult"
    },
    {
        "word": "Teenager", "pos": "noun", "ipa": "/ˈtiːnˌeɪ.dʒɚ/", "lvl": "B1", "ctx": "Daily",
        "en": "A person aged between 13 and 19 years.", "vn": "Thanh thiếu niên.",
        "m": "Teen tuổi teen.",
        "col": ["`moody teenager`: thanh thiếu niên hay hờn dỗi"],
        "ex1": "The teenager is on his phone.", "ex1v": "Cậu thanh niên đang nghịch điện thoại.",
        "ex2": "Teenager crime rates have decreased.", "ex2v": "Tỷ lệ tội phạm thanh thiếu niên đã giảm.",
        "ex3": "I was a teenage werewolf.", "ex3v": "Tôi từng là một người sói tuổi teen.",
        "fam": "Teenage (adj)", "syn": "Adolescent", "ant": "Adult"
    },
    {
        "word": "Youth", "pos": "noun", "ipa": "/juːθ/", "lvl": "B1", "ctx": "Daily",
        "en": "The period between childhood and adult age.", "vn": "Tuổi trẻ, thanh niên.",
        "m": "Youth giống 'dút', rút lại tuổi trẻ.",
        "col": ["`youth club`: câu lạc bộ thanh niên"],
        "ex1": "In my youth, I played sports.", "ex1v": "Hồi trẻ tôi có chơi thể thao.",
        "ex2": "Youth unemployment is a major issue.", "ex2v": "Thất nghiệp ở giới trẻ là một vấn đề lớn.",
        "ex3": "The youth of today.", "ex3v": "Giới trẻ ngày nay.",
        "fam": "Youthful (adj)", "syn": "Young person", "ant": "Adulthood"
    },
    {
        "word": "Childhood", "pos": "noun", "ipa": "/ˈtʃaɪld.hʊd/", "lvl": "B1", "ctx": "Daily",
        "en": "The state of being a child.", "vn": "Tuổi thơ.",
        "m": "Child + hood (thời kỳ).",
        "col": ["`early childhood`: thời thơ ấu"],
        "ex1": "I had a happy childhood.", "ex1v": "Tôi đã có một tuổi thơ hạnh phúc.",
        "ex2": "Childhood obesity is rising.", "ex2v": "Béo phì ở trẻ em đang gia tăng.",
        "ex3": "My childhood was a lie.", "ex3v": "Tuổi thơ của tôi là một lời nói dối.",
        "fam": "Childish (adj)", "syn": "Youth", "ant": "Adulthood"
    },
    {
        "word": "Siblings", "pos": "noun", "ipa": "/ˈsɪb.lɪŋz/", "lvl": "B1", "ctx": "Daily",
        "en": "Brothers and sisters.", "vn": "Anh chị em ruột.",
        "m": "Siblings (xíp lình) -> xích lại gần anh em.",
        "col": ["`older sibling`: anh/chị lớn"],
        "ex1": "I have two siblings.", "ex1v": "Tôi có hai anh chị em ruột.",
        "ex2": "Sibling rivalry is common.", "ex2v": "Sự ganh đua giữa anh chị em là phổ biến.",
        "ex3": "Are they your siblings?", "ex3v": "Họ là anh chị em của bạn à?",
        "fam": "Sibling (n)", "syn": "Brothers and sisters", "ant": "Only child"
    },
    {
        "word": "Naughty", "pos": "adj", "ipa": "/ˈnɑː.t̬i/", "lvl": "B1", "ctx": "Daily",
        "en": "Disobedient or badly behaved.", "vn": "Nghịch ngợm, hư đốn.",
        "m": "Naughty (no-ti) -> no đòn vì nghịch ngợm.",
        "col": ["`naughty boy`: cậu bé hư"],
        "ex1": "The naughty child broke the vase.", "ex1v": "Đứa trẻ nghịch ngợm làm vỡ bình hoa.",
        "ex2": "Behavioral studies analyze naughty conduct.", "ex2v": "Các nghiên cứu hành vi phân tích thái độ hư đốn.",
        "ex3": "He's on the naughty list.", "ex3v": "Nó nằm trong danh sách trẻ hư.",
        "fam": "Naughtiness (n)", "syn": "Mischievous", "ant": "Well-behaved"
    },
    {
        "word": "Obedient", "pos": "adj", "ipa": "/oʊˈbiː.di.ənt/", "lvl": "B2", "ctx": "Daily",
        "en": "Complying or willing to comply with orders or requests.", "vn": "Ngoan ngoãn, vâng lời.",
        "m": "Obedient (o-bi-điên) -> không ngoan thì bị điên.",
        "col": ["`obedient child`: đứa trẻ vâng lời"],
        "ex1": "He is an obedient son.", "ex1v": "Cậu ấy là một người con ngoan.",
        "ex2": "Obedient behavior is rewarded.", "ex2v": "Hành vi vâng lời được khen thưởng.",
        "ex3": "Be obedient to your parents.", "ex3v": "Hãy vâng lời cha mẹ.",
        "fam": "Obedience (n), Obey (v)", "syn": "Docile", "ant": "Rebellious"
    },
    {
        "word": "Spoil", "pos": "verb", "ipa": "/spɔɪl/", "lvl": "B1", "ctx": "Daily",
        "en": "Harm the character of a child by being too lenient or indulgent.", "vn": "Làm hư (trẻ con).",
        "m": "Spoil giống 'sờ poi' -> sờ điểm, chiều chuộng quá.",
        "col": ["`spoil a child`: làm hư một đứa trẻ"],
        "ex1": "Grandparents often spoil their grandkids.", "ex1v": "Ông bà thường chiều hư các cháu.",
        "ex2": "Spoiling a child leads to entitlement.", "ex2v": "Làm hư một đứa trẻ dẫn đến sự ỷ lại.",
        "ex3": "You are spoiled rotten.", "ex3v": "Cậu bị chiều hư quá mức rồi.",
        "fam": "Spoiled (adj)", "syn": "Indulge", "ant": "Discipline"
    },
    {
        "word": "Raise", "pos": "verb", "ipa": "/reɪz/", "lvl": "B1", "ctx": "Daily",
        "en": "Bring up a child.", "vn": "Nuôi nấng.",
        "m": "Raise -> Rây, rây bột nuôi con.",
        "col": ["`raise a family`: nuôi nấng gia đình"],
        "ex1": "She had to raise the kids alone.", "ex1v": "Cô ấy phải nuôi bọn trẻ một mình.",
        "ex2": "It costs a lot to raise a child today.", "ex2v": "Nuôi một đứa trẻ ngày nay tốn rất nhiều tiền.",
        "ex3": "I was raised in the wild.", "ex3v": "Tôi được nuôi dưỡng trong môi trường hoang dã.",
        "fam": "Raising (n)", "syn": "Bring up", "ant": "Neglect"
    },
    {
        "word": "Upbringing", "pos": "noun", "ipa": "/ˈʌpˌbrɪŋ.ɪŋ/", "lvl": "B2", "ctx": "Daily",
        "en": "The treatment and instruction received by a child from its parents.", "vn": "Sự giáo dục, nuôi nấng.",
        "m": "Up (lên) + bring (mang) -> mang lớn lên.",
        "col": ["`strict upbringing`: sự giáo dục nghiêm khắc"],
        "ex1": "He had a strict upbringing.", "ex1v": "Anh ấy có một sự giáo dục nghiêm khắc.",
        "ex2": "Upbringing affects a child's psychology.", "ex2v": "Sự nuôi dưỡng ảnh hưởng đến tâm lý của một đứa trẻ.",
        "ex3": "It's all in the upbringing.", "ex3v": "Tất cả là do sự giáo dục.",
        "fam": "Bring up (v)", "syn": "Education", "ant": "Neglect"
    },
    {
        "word": "Orphan", "pos": "noun", "ipa": "/ˈɔːr.fən/", "lvl": "B2", "ctx": "Formal",
        "en": "A child whose parents are dead.", "vn": "Trẻ mồ côi.",
        "m": "Orphan (o-phần) -> không có phần cho trẻ mồ côi.",
        "col": ["`war orphan`: trẻ mồ côi do chiến tranh"],
        "ex1": "He grew up as an orphan.", "ex1v": "Cậu ấy lớn lên như một đứa trẻ mồ côi.",
        "ex2": "Orphanages provide shelter for orphans.", "ex2v": "Trại trẻ mồ côi cung cấp chỗ ở cho trẻ mồ côi.",
        "ex3": "I'm an orphan now.", "ex3v": "Tôi là trẻ mồ côi bây giờ.",
        "fam": "Orphanage (n)", "syn": "Foundling", "ant": "None"
    },
    {
        "word": "Adopt", "pos": "verb", "ipa": "/əˈdɑːpt/", "lvl": "B1", "ctx": "Daily",
        "en": "Legally take another's child and bring it up as one's own.", "vn": "Nhận nuôi.",
        "m": "Adopt (a-đóp) -> A đớp, nhận nuôi.",
        "col": ["`adopt a child`: nhận nuôi một đứa trẻ"],
        "ex1": "They decided to adopt a baby.", "ex1v": "Họ quyết định nhận nuôi một em bé.",
        "ex2": "The adoption process is legally complex.", "ex2v": "Quá trình nhận con nuôi rất phức tạp về mặt pháp lý.",
        "ex3": "You're adopted.", "ex3v": "Em là con nuôi.",
        "fam": "Adoption (n), Adoptive (adj)", "syn": "Take in", "ant": "Abandon"
    },
    {
        "word": "Foster", "pos": "verb", "ipa": "/ˈfɑː.stɚ/", "lvl": "B2", "ctx": "Daily",
        "en": "Bring up a child that is not one's own by birth.", "vn": "Nuôi dưỡng (không nhận làm con nuôi).",
        "m": "Foster (pho-x-tơ) -> phó thác nuôi nấng.",
        "col": ["`foster parent`: cha mẹ nuôi"],
        "ex1": "They foster children in need.", "ex1v": "Họ nuôi dưỡng những đứa trẻ cần giúp đỡ.",
        "ex2": "Foster care provides temporary housing.", "ex2v": "Chăm sóc thay thế cung cấp chỗ ở tạm thời.",
        "ex3": "He is my foster brother.", "ex3v": "Anh ấy là anh trai nuôi của tôi.",
        "fam": "Foster (adj)", "syn": "Raise", "ant": "Neglect"
    },
    {
        "word": "Infant", "pos": "noun", "ipa": "/ˈɪn.fənt/", "lvl": "B2", "ctx": "Academic",
        "en": "A very young child or baby.", "vn": "Trẻ sơ sinh.",
        "m": "Infant (in-phân) -> in phần của bé.",
        "col": ["`newborn infant`: trẻ sơ sinh mới đẻ"],
        "ex1": "The infant is asleep.", "ex1v": "Trẻ sơ sinh đang ngủ.",
        "ex2": "Infant mortality rates have dropped.", "ex2v": "Tỷ lệ tử vong ở trẻ sơ sinh đã giảm.",
        "ex3": "Save the infant!", "ex3v": "Hãy cứu đứa trẻ!",
        "fam": "Infancy (n), Infantile (adj)", "syn": "Baby", "ant": "Adult"
    },
    {
        "word": "Innocence", "pos": "noun", "ipa": "/ˈɪn.ə.səns/", "lvl": "B2", "ctx": "Daily",
        "en": "Lack of guile or corruption; purity.", "vn": "Sự ngây thơ.",
        "m": "Innocence (in-nơ-sân) -> in nơ, ngây thơ đeo nơ.",
        "col": ["`childlike innocence`: sự ngây thơ như trẻ con"],
        "ex1": "I miss the innocence of childhood.", "ex1v": "Tôi nhớ sự ngây thơ của tuổi thơ.",
        "ex2": "The loss of innocence is a literary theme.", "ex2v": "Sự mất đi ngây thơ là một chủ đề văn học.",
        "ex3": "Look at her innocence.", "ex3v": "Nhìn sự ngây thơ của cô ấy kìa.",
        "fam": "Innocent (adj)", "syn": "Purity", "ant": "Guilt"
    },
    {
        "word": "Tantrum", "pos": "noun", "ipa": "/ˈtæn.trəm/", "lvl": "B2", "ctx": "Daily",
        "en": "An uncontrolled outburst of anger and frustration, typically in a young child.", "vn": "Cơn ăn vạ, nổi cáu.",
        "m": "Tantrum (tăn-trùm) -> tăn trùm chăn ăn vạ.",
        "col": ["`throw a tantrum`: ăn vạ"],
        "ex1": "The toddler threw a tantrum.", "ex1v": "Đứa trẻ mới biết đi đã ăn vạ.",
        "ex2": "Tantrums are common in developmental stages.", "ex2v": "Các cơn giận dữ là phổ biến trong các giai đoạn phát triển.",
        "ex3": "Don't throw a tantrum now.", "ex3v": "Đừng có ăn vạ bây giờ.",
        "fam": "None", "syn": "Outburst", "ant": "Calmness"
    },
    {
        "word": "Preadolescent", "pos": "noun", "ipa": "/ˌpriː.æd.əˈles.ənt/", "lvl": "B2", "ctx": "Academic",
        "en": "A child just before the onset of puberty.", "vn": "Trẻ vị thành niên (sắp dậy thì).",
        "m": "Pre (trước) + adolescent (vị thành niên).",
        "col": ["`preadolescent child`: trẻ sắp dậy thì"],
        "ex1": "Preadolescent boys are active.", "ex1v": "Các bé trai tiền vị thành niên rất hiếu động.",
        "ex2": "Preadolescent psychology focuses on identity.", "ex2v": "Tâm lý học tiền vị thành niên tập trung vào bản sắc.",
        "ex3": "He's a preadolescent.", "ex3v": "Nó là một đứa trẻ sắp vị thành niên.",
        "fam": "Preadolescence (n)", "syn": "Preteen", "ant": "Adult"
    },
    {
        "word": "Misbehave", "pos": "verb", "ipa": "/ˌmɪs.bɪˈheɪv/", "lvl": "B1", "ctx": "Daily",
        "en": "Fail to conduct oneself in a way that is acceptable to others.", "vn": "Cư xử không đúng mực.",
        "m": "Mis (sai) + behave (cư xử).",
        "col": ["`misbehave in class`: cư xử hư trong lớp"],
        "ex1": "Don't misbehave at the party.", "ex1v": "Đừng cư xử không đúng mực ở bữa tiệc.",
        "ex2": "Children who misbehave often seek attention.", "ex2v": "Trẻ em cư xử tồi thường tìm kiếm sự chú ý.",
        "ex3": "Are you going to misbehave?", "ex3v": "Con định cư xử hư hả?",
        "fam": "Misbehavior (n)", "syn": "Act up", "ant": "Behave"
    },
    {
        "word": "Curfew", "pos": "noun", "ipa": "/ˈkɝː.fjuː/", "lvl": "B2", "ctx": "Daily",
        "en": "A regulation requiring people to remain indoors between specified hours.", "vn": "Giờ giới nghiêm.",
        "m": "Curfew (cơ-phiu) -> cờ phiu phiu giờ giới nghiêm.",
        "col": ["`strict curfew`: giờ giới nghiêm nghiêm ngặt"],
        "ex1": "My parents set a 9 PM curfew.", "ex1v": "Bố mẹ tôi đặt giờ giới nghiêm là 9 giờ tối.",
        "ex2": "Curfews reduce juvenile crime rates.", "ex2v": "Giờ giới nghiêm làm giảm tỷ lệ tội phạm vị thành niên.",
        "ex3": "You missed your curfew!", "ex3v": "Con đã lỡ giờ giới nghiêm rồi!",
        "fam": "None", "syn": "Deadline", "ant": "Freedom"
    },
    {
        "word": "Chores", "pos": "noun", "ipa": "/tʃɔːrz/", "lvl": "B1", "ctx": "Daily",
        "en": "A routine task, especially a household one.", "vn": "Việc vặt trong nhà.",
        "m": "Chores (cho) -> việc cho trẻ làm.",
        "col": ["`household chores`: việc nhà"],
        "ex1": "The kids help with chores.", "ex1v": "Bọn trẻ giúp làm việc nhà.",
        "ex2": "Assigning chores teaches responsibility.", "ex2v": "Giao việc nhà dạy trách nhiệm.",
        "ex3": "Do your chores!", "ex3v": "Làm việc nhà đi!",
        "fam": "None", "syn": "Tasks", "ant": "Play"
    },

    # C1-C2 (15)
    {
        "word": "Juvenile", "pos": "adj", "ipa": "/ˈdʒuː.və.nəl/", "lvl": "C1", "ctx": "Formal",
        "en": "Of, for, or relating to young people.", "vn": "Vị thành niên, trẻ con.",
        "m": "Juvenile (chu-vơ-nai) -> chu vu nai, trẻ con như nai.",
        "col": ["`juvenile delinquency`: tội phạm vị thành niên"],
        "ex1": "His behavior was very juvenile.", "ex1v": "Hành vi của anh ta rất trẻ con.",
        "ex2": "The juvenile justice system focuses on rehabilitation.", "ex2v": "Hệ thống tư pháp vị thành niên tập trung vào phục hồi.",
        "ex3": "Juveniles are strictly prohibited.", "ex3v": "Vị thành niên bị nghiêm cấm.",
        "fam": "Rejuvenate (v)", "syn": "Young", "ant": "Mature"
    },
    {
        "word": "Precocity", "pos": "noun", "ipa": "/prɪˈkɑː.sə.t̬i/", "lvl": "C2", "ctx": "Academic",
        "en": "Exceptionally early in development or occurrence.", "vn": "Sự sớm phát triển (trí tuệ).",
        "m": "Precocity (pre-co-xi-ti) -> trước cả khi co (rút).",
        "col": ["`intellectual precocity`: sự trưởng thành trí tuệ sớm"],
        "ex1": "Her precocity amazed her teachers.", "ex1v": "Sự sớm phát triển của cô bé làm giáo viên kinh ngạc.",
        "ex2": "Precocity in music is easily recognized.", "ex2v": "Năng khiếu âm nhạc sớm được nhận ra dễ dàng.",
        "ex3": "Such precocity is rare.", "ex3v": "Sự thông minh sớm như vậy rất hiếm.",
        "fam": "Precocious (adj)", "syn": "Forwardness", "ant": "Backwardness"
    },
    {
        "word": "Adolescent", "pos": "noun", "ipa": "/ˌæd.əˈles.ənt/", "lvl": "C1", "ctx": "Formal",
        "en": "In the process of developing from a child into an adult.", "vn": "Thanh thiếu niên.",
        "m": "Adolescent (a-đô-lét-xân) -> A, đô lên rồi.",
        "col": ["`adolescent behavior`: hành vi tuổi dậy thì"],
        "ex1": "The clinic helps adolescent patients.", "ex1v": "Phòng khám giúp đỡ bệnh nhân thanh thiếu niên.",
        "ex2": "Adolescent psychology explores identity crisis.", "ex2v": "Tâm lý học thanh thiếu niên khám phá khủng hoảng bản sắc.",
        "ex3": "Typical adolescent angst.", "ex3v": "Nỗi lo âu tuổi mới lớn điển hình.",
        "fam": "Adolescence (n)", "syn": "Teenager", "ant": "Adult"
    },
    {
        "word": "Progeny", "pos": "noun", "ipa": "/ˈprɑː.dʒə.ni/", "lvl": "C2", "ctx": "Formal",
        "en": "A descendant or the descendants of a person, animal, or plant.", "vn": "Con cái, dòng dõi.",
        "m": "Progeny (pro-gen-ni) -> gen của pro (giỏi).",
        "col": ["`produce progeny`: sinh con"],
        "ex1": "He was proud of his progeny.", "ex1v": "Ông ấy tự hào về con cái mình.",
        "ex2": "The genetic mutation was passed to its progeny.", "ex2v": "Đột biến gen được truyền cho dòng dõi của nó.",
        "ex3": "Behold, my progeny.", "ex3v": "Hãy xem dòng dõi của ta.",
        "fam": "Progenitor (n)", "syn": "Offspring", "ant": "Ancestor"
    },
    {
        "word": "Minor", "pos": "noun", "ipa": "/ˈmaɪ.nɚ/", "lvl": "C1", "ctx": "Formal",
        "en": "A person under the age of full legal responsibility.", "vn": "Người vị thành niên.",
        "m": "Minor (mai-nơ) -> nhỏ bé.",
        "col": ["`unaccompanied minor`: trẻ vị thành niên không có người lớn đi kèm"],
        "ex1": "It is illegal to sell alcohol to minors.", "ex1v": "Bán rượu cho người vị thành niên là bất hợp pháp.",
        "ex2": "The law protects the rights of minors.", "ex2v": "Pháp luật bảo vệ quyền lợi của người vị thành niên.",
        "ex3": "He is still a minor.", "ex3v": "Anh ta vẫn là người vị thành niên.",
        "fam": "Minority (n)", "syn": "Child", "ant": "Adult"
    },
    {
        "word": "Prodigy", "pos": "noun", "ipa": "/ˈprɑː.də.dʒi/", "lvl": "C2", "ctx": "Academic",
        "en": "A person, especially a young one, endowed with exceptional qualities or abilities.", "vn": "Thần đồng.",
        "m": "Prodigy (pro-đi-ghi) -> pro đi ghi danh thần đồng.",
        "col": ["`child prodigy`: thần đồng nhí"],
        "ex1": "Mozart was a child prodigy.", "ex1v": "Mozart là một thần đồng âm nhạc.",
        "ex2": "The institution nurtures young prodigies in mathematics.", "ex2v": "Viện nuôi dưỡng các thần đồng trẻ trong toán học.",
        "ex3": "You are a prodigy.", "ex3v": "Cậu là một thần đồng.",
        "fam": "Prodigious (adj)", "syn": "Genius", "ant": "Amateur"
    },
    {
        "word": "Rebellious", "pos": "adj", "ipa": "/rɪˈbel.i.əs/", "lvl": "C1", "ctx": "Academic",
        "en": "Showing a desire to resist authority, control, or convention.", "vn": "Nổi loạn.",
        "m": "Rebel (nổi loạn) + ious.",
        "col": ["`rebellious teenager`: thanh thiếu niên nổi loạn"],
        "ex1": "He went through a rebellious phase.", "ex1v": "Cậu ấy đã trải qua một giai đoạn nổi loạn.",
        "ex2": "Rebellious attitudes often stem from strict parenting.", "ex2v": "Thái độ nổi loạn thường xuất phát từ việc nuôi dạy nghiêm khắc.",
        "ex3": "The rebellious youth.", "ex3v": "Tuổi trẻ nổi loạn.",
        "fam": "Rebel (n), Rebellion (n)", "syn": "Defiant", "ant": "Obedient"
    },
    {
        "word": "Impressionable", "pos": "adj", "ipa": "/ɪmˈpreʃ.ən.ə.bəl/", "lvl": "C2", "ctx": "Formal",
        "en": "Easily influenced because of a lack of critical ability.", "vn": "Dễ bị ảnh hưởng.",
        "m": "Impression (ấn tượng) + able -> dễ bị ấn tượng.",
        "col": ["`impressionable age`: độ tuổi dễ bị ảnh hưởng"],
        "ex1": "Children are at an impressionable age.", "ex1v": "Trẻ em đang ở độ tuổi dễ bị ảnh hưởng.",
        "ex2": "Media significantly affects impressionable minds.", "ex2v": "Truyền thông ảnh hưởng đáng kể đến những tâm trí dễ bị tác động.",
        "ex3": "He's highly impressionable.", "ex3v": "Cậu ấy rất dễ bị ảnh hưởng.",
        "fam": "Impression (n)", "syn": "Suggestible", "ant": "Skeptical"
    },
    {
        "word": "Nurture", "pos": "verb", "ipa": "/ˈnɝː.tʃɚ/", "lvl": "C1", "ctx": "Academic",
        "en": "Care for and encourage the growth or development of.", "vn": "Nuôi dưỡng, bồi dưỡng.",
        "m": "Nurture (nơ-chờ) -> nơ chờ được nuôi dưỡng.",
        "col": ["`nurture talent`: nuôi dưỡng tài năng"],
        "ex1": "Parents must nurture their children's talents.", "ex1v": "Cha mẹ phải nuôi dưỡng tài năng của con cái.",
        "ex2": "The debate of nature versus nurture continues.", "ex2v": "Cuộc tranh luận giữa bẩm sinh và nuôi dưỡng vẫn tiếp tục.",
        "ex3": "Nurture the young.", "ex3v": "Hãy nuôi dưỡng thế hệ trẻ.",
        "fam": "Nurturing (adj)", "syn": "Cultivate", "ant": "Neglect"
    },
    {
        "word": "Paternal", "pos": "adj", "ipa": "/pəˈtɝː.nəl/", "lvl": "C1", "ctx": "Formal",
        "en": "Of or appropriate to a father.", "vn": "Thuộc về cha.",
        "m": "Pa (cha) + ternal.",
        "col": ["`paternal instinct`: bản năng làm cha"],
        "ex1": "He has a strong paternal instinct.", "ex1v": "Anh ấy có bản năng làm cha mạnh mẽ.",
        "ex2": "Paternal leave is becoming more common globally.", "ex2v": "Nghỉ thai sản cho cha đang trở nên phổ biến hơn trên toàn cầu.",
        "ex3": "My paternal grandmother.", "ex3v": "Bà nội của tôi.",
        "fam": "Paternity (n)", "syn": "Fatherly", "ant": "Maternal"
    },
    {
        "word": "Maternal", "pos": "adj", "ipa": "/məˈtɝː.nəl/", "lvl": "C1", "ctx": "Formal",
        "en": "Of or relating to a mother.", "vn": "Thuộc về mẹ.",
        "m": "Ma (mẹ) + ternal.",
        "col": ["`maternal care`: sự chăm sóc của mẹ"],
        "ex1": "Her maternal love is unconditional.", "ex1v": "Tình mẹ của cô ấy là vô điều kiện.",
        "ex2": "Maternal mortality rates are a key health indicator.", "ex2v": "Tỷ lệ tử vong ở mẹ là một chỉ số sức khỏe quan trọng.",
        "ex3": "She has strong maternal feelings.", "ex3v": "Cô ấy có những cảm xúc làm mẹ mãnh liệt.",
        "fam": "Maternity (n)", "syn": "Motherly", "ant": "Paternal"
    },
    {
        "word": "Infancy", "pos": "noun", "ipa": "/ˈɪn.fən.si/", "lvl": "C2", "ctx": "Academic",
        "en": "The state or period of early childhood or babyhood.", "vn": "Thời kỳ thơ ấu, lúc phôi thai.",
        "m": "Infant + cy.",
        "col": ["`in its infancy`: ở thời kỳ sơ khai"],
        "ex1": "He survived a disease in his infancy.", "ex1v": "Cậu ấy đã sống sót sau một căn bệnh từ thời thơ ấu.",
        "ex2": "The technology is still in its infancy.", "ex2v": "Công nghệ này vẫn còn ở giai đoạn sơ khai.",
        "ex3": "From infancy to adulthood.", "ex3v": "Từ thời thơ ấu đến tuổi trưởng thành.",
        "fam": "Infant (n)", "syn": "Babyhood", "ant": "Adulthood"
    },
    {
        "word": "Delinquency", "pos": "noun", "ipa": "/dɪˈlɪŋ.kwən.si/", "lvl": "C2", "ctx": "Formal",
        "en": "Minor crime, especially that committed by young people.", "vn": "Sự phạm pháp (vị thành niên).",
        "m": "Delinquency (đi-lin-quên-xi) -> đi linh tinh quên luật.",
        "col": ["`juvenile delinquency`: tội phạm vị thành niên"],
        "ex1": "The city has a high rate of juvenile delinquency.", "ex1v": "Thành phố có tỷ lệ tội phạm vị thành niên cao.",
        "ex2": "Poverty often correlates with youth delinquency.", "ex2v": "Nghèo đói thường tương quan với tội phạm vị thành niên.",
        "ex3": "Delinquency won't be tolerated.", "ex3v": "Phạm pháp sẽ không được dung thứ.",
        "fam": "Delinquent (n/adj)", "syn": "Crime", "ant": "Obedience"
    },
    {
        "word": "Brat", "pos": "noun", "ipa": "/bræt/", "lvl": "C1", "ctx": "Daily",
        "en": "A child, typically a badly behaved one.", "vn": "Đứa trẻ hư, ranh con.",
        "m": "Brat (b-rát) -> la rát tai.",
        "col": ["`spoiled brat`: đứa trẻ bị chiều hư"],
        "ex1": "Don't act like a spoiled brat.", "ex1v": "Đừng cư xử như một đứa trẻ bị chiều hư.",
        "ex2": "Psychologists advise against labeling children as brats.", "ex2v": "Các nhà tâm lý học khuyên không nên gán mác trẻ em là hư đốn.",
        "ex3": "You little brat!", "ex3v": "Thằng ranh con!",
        "fam": "Bratty (adj)", "syn": "Rascal", "ant": "Angel"
    },
    {
        "word": "Offspring", "pos": "noun", "ipa": "/ˈɑːf.sprɪŋ/", "lvl": "C1", "ctx": "Academic",
        "en": "A person's child or children.", "vn": "Con cái, dòng dõi.",
        "m": "Off (ra khỏi) + spring (mùa xuân) -> đâm chồi nảy lộc.",
        "col": ["`produce offspring`: sinh sản"],
        "ex1": "They are proud of their offspring.", "ex1v": "Họ tự hào về con cái của họ.",
        "ex2": "Evolution favors species that produce viable offspring.", "ex2v": "Tiến hóa ưu ái các loài tạo ra con cái có khả năng sống sót.",
        "ex3": "These are my offspring.", "ex3v": "Đây là những đứa con của tôi.",
        "fam": "None", "syn": "Children", "ant": "Parent"
    }
]

template = """# {word}
*{pos}*
> {ipa}

---
**Level:** {lvl} | **Ngữ cảnh:** {ctx} | **Chủ đề:** CHILDREN

## 📌 Ý nghĩa (Meaning)
- **EN:** {en}
- **VN:** {vn}

## 🧠 Mẹo nhớ (Mnemonics)
💡 {m}

## 🧩 Cụm từ thường đi kèm (Collocations)
- {col1}

## 🎬 Ví dụ thực tế (Real-world Examples)
1. 💬 *Daily:* {ex1}
   *-> {ex1v}*
2. 💼 *Work/Academic:* {ex2}
   *-> {ex2v}*
3. 🎬 *Media/Movie:* {ex3}
   *-> {ex3v}*

## 🕸️ Mạng lưới từ (Word Network)
**Word Family:**
- {fam}

**Synonyms:** {syn}
**Antonyms:** {ant}
"""

for v in vocab:
    content = template.format(
        word=v["word"],
        pos=v["pos"],
        ipa=v["ipa"],
        lvl=v["lvl"],
        ctx=v["ctx"],
        en=v["en"],
        vn=v["vn"],
        m=v["m"],
        col1=v["col"][0] if v["col"] else "`none`: không có",
        ex1=v["ex1"], ex1v=v["ex1v"],
        ex2=v["ex2"], ex2v=v["ex2v"],
        ex3=v["ex3"], ex3v=v["ex3v"],
        fam=v["fam"],
        syn=v["syn"],
        ant=v["ant"]
    )
    
    file_path = os.path.join(target_dir, f"{v['word']}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Successfully generated 50 vocabulary markdown files.")
