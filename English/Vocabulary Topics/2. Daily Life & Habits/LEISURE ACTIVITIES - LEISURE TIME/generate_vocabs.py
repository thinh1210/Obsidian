import os
import json

topic = "LEISURE ACTIVITIES - LEISURE TIME"
output_dir = "/home/thinh/Documents/Obsidian Vault/English/Vocabulary Topics/2. Daily Life & Habits/LEISURE ACTIVITIES - LEISURE TIME"

words_data = [
    # A1-A2 (15 words)
    {
        "word": "Hobby", "pos": "n", "ipa": "/ˈhɒbi/", "lvl": "A1", "ctx": "Daily",
        "en": "An activity done regularly in one's leisure time for pleasure.",
        "vn": "Sở thích",
        "m": "Hobby nghe như 'hóp bi' - nhặt bi là một sở thích của trẻ em.",
        "cols": ["have a hobby: có sở thích", "take up a hobby: bắt đầu một sở thích"],
        "ex1": "My favorite hobby is reading.", "ex1v": "Sở thích của tôi là đọc sách.",
        "ex2": "Having a hobby reduces work stress.", "ex2v": "Có một sở thích làm giảm căng thẳng công việc.",
        "ex3": "In the movie, his hobby is collecting stamps.", "ex3v": "Trong phim, sở thích của anh ấy là sưu tầm tem.",
        "fam": "Hobbies (n)", "syn": "pastime, interest", "ant": "work, profession"
    },
    {
        "word": "Read", "pos": "v", "ipa": "/riːd/", "lvl": "A1", "ctx": "Daily",
        "en": "Look at and comprehend the meaning of written or printed matter.",
        "vn": "Đọc",
        "m": "Read - rít một hơi để lấy sức đọc truyện.",
        "cols": ["read a book: đọc sách", "read aloud: đọc to"],
        "ex1": "I read before going to bed.", "ex1v": "Tôi đọc sách trước khi đi ngủ.",
        "ex2": "Students must read the guidelines.", "ex2v": "Học sinh phải đọc hướng dẫn.",
        "ex3": "He reads a newspaper in the cafe scene.", "ex3v": "Anh ấy đọc báo trong cảnh quán cà phê.",
        "fam": "Reader (n), Reading (n)", "syn": "peruse, scan", "ant": "write"
    },
    {
        "word": "Game", "pos": "n", "ipa": "/ɡeɪm/", "lvl": "A1", "ctx": "Daily",
        "en": "A form of play or sport, especially a competitive one played according to rules.",
        "vn": "Trò chơi",
        "m": "Game là game thôi.",
        "cols": ["play a game: chơi một trò chơi", "board game: trò chơi cờ bàn"],
        "ex1": "We played a game of chess.", "ex1v": "Chúng tôi đã chơi một ván cờ.",
        "ex2": "The team analyzed the game strategy.", "ex2v": "Đội đã phân tích chiến lược trò chơi.",
        "ex3": "The Hunger Games is a famous movie.", "ex3v": "The Hunger Games là một bộ phim nổi tiếng.",
        "fam": "Gamer (n), Gaming (n)", "syn": "match, play", "ant": "work, chore"
    },
    {
        "word": "Movie", "pos": "n", "ipa": "/ˈmuːvi/", "lvl": "A1", "ctx": "Daily",
        "en": "A story or event recorded by a camera as a set of moving images.",
        "vn": "Phim",
        "m": "Movie từ chữ move (chuyển động).",
        "cols": ["watch a movie: xem phim", "go to the movies: đi xem phim"],
        "ex1": "Let's watch a movie tonight.", "ex1v": "Tối nay xem phim nhé.",
        "ex2": "The documentary is an educational movie.", "ex2v": "Phim tài liệu là một bộ phim mang tính giáo dục.",
        "ex3": "Action movies are very popular.", "ex3v": "Phim hành động rất phổ biến.",
        "fam": "Movies (n)", "syn": "film, picture", "ant": "book"
    },
    {
        "word": "Music", "pos": "n", "ipa": "/ˈmjuːzɪk/", "lvl": "A1", "ctx": "Daily",
        "en": "Vocal or instrumental sounds combined in such a way as to produce beauty of form, harmony.",
        "vn": "Âm nhạc",
        "m": "Music - Miu (mèo) thích nghe nhạc (sic).",
        "cols": ["listen to music: nghe nhạc", "pop music: nhạc pop"],
        "ex1": "I love listening to music.", "ex1v": "Tôi thích nghe nhạc.",
        "ex2": "Music therapy helps patients recover.", "ex2v": "Liệu pháp âm nhạc giúp bệnh nhân phục hồi.",
        "ex3": "The movie's background music is thrilling.", "ex3v": "Nhạc nền của phim rất gay cấn.",
        "fam": "Musical (adj), Musician (n)", "syn": "melody, tune", "ant": "silence"
    },
    {
        "word": "Relax", "pos": "v", "ipa": "/rɪˈlæks/", "lvl": "A1", "ctx": "Daily",
        "en": "Rest and feel less tense or anxious.",
        "vn": "Thư giãn",
        "m": "Re (lại) + lax (lắc) -> lắc lư để thư giãn.",
        "cols": ["relax at home: thư giãn ở nhà", "relax your mind: thư giãn tâm trí"],
        "ex1": "I just want to relax this weekend.", "ex1v": "Tôi chỉ muốn thư giãn cuối tuần này.",
        "ex2": "Relaxation techniques improve productivity.", "ex2v": "Các kỹ thuật thư giãn cải thiện năng suất.",
        "ex3": "He relaxes by the pool in the scene.", "ex3v": "Anh ấy thư giãn bên hồ bơi trong cảnh đó.",
        "fam": "Relaxation (n), Relaxed (adj)", "syn": "rest, unwind", "ant": "stress, worry"
    },
    {
        "word": "Sport", "pos": "n", "ipa": "/spɔːt/", "lvl": "A1", "ctx": "Daily",
        "en": "An activity involving physical exertion and skill.",
        "vn": "Thể thao",
        "m": "Sport - sờ pót (pot) chơi thể thao ra mồ hôi ướt bình nước.",
        "cols": ["play sports: chơi thể thao", "extreme sports: thể thao mạo hiểm"],
        "ex1": "Football is my favorite sport.", "ex1v": "Bóng đá là môn thể thao yêu thích của tôi.",
        "ex2": "Sports science is a growing field.", "ex2v": "Khoa học thể thao là một lĩnh vực đang phát triển.",
        "ex3": "The sports channel broadcasts live matches.", "ex3v": "Kênh thể thao phát sóng trực tiếp các trận đấu.",
        "fam": "Sporty (adj)", "syn": "athletics, games", "ant": "inactivity"
    },
    {
        "word": "Swim", "pos": "v", "ipa": "/swɪm/", "lvl": "A1", "ctx": "Daily",
        "en": "Propel the body through water using the limbs.",
        "vn": "Bơi",
        "m": "Swim nghe như sờ-wim -> sóng vỗ khi bơi.",
        "cols": ["go swimming: đi bơi", "swim in the pool: bơi trong hồ"],
        "ex1": "Can you swim?", "ex1v": "Bạn biết bơi không?",
        "ex2": "Swimming is excellent cardiovascular exercise.", "ex2v": "Bơi lội là bài tập tim mạch tuyệt vời.",
        "ex3": "The protagonist swims across the river.", "ex3v": "Nhân vật chính bơi qua sông.",
        "fam": "Swimmer (n), Swimming (n)", "syn": "bathe, float", "ant": "sink, drown"
    },
    {
        "word": "Dance", "pos": "v", "ipa": "/dɑːns/", "lvl": "A1", "ctx": "Daily",
        "en": "Move rhythmically to music.",
        "vn": "Nhảy múa",
        "m": "Dance - Đan (tên người) thích nhảy.",
        "cols": ["dance gracefully: nhảy duyên dáng", "dance to the music: nhảy theo nhạc"],
        "ex1": "They danced all night.", "ex1v": "Họ đã nhảy múa suốt đêm.",
        "ex2": "Dance therapy is studied at the university.", "ex2v": "Liệu pháp nhảy múa được nghiên cứu tại trường đại học.",
        "ex3": "The final scene features a big dance.", "ex3v": "Cảnh cuối có một điệu nhảy lớn.",
        "fam": "Dancer (n), Dancing (n)", "syn": "groove, waltz", "ant": "stand still"
    },
    {
        "word": "Walk", "pos": "v", "ipa": "/wɔːk/", "lvl": "A1", "ctx": "Daily",
        "en": "Move at a regular pace by lifting and setting down each foot in turn.",
        "vn": "Đi bộ",
        "m": "Walk - Quắc mắt nhìn ai đang đi bộ.",
        "cols": ["go for a walk: đi dạo", "walk the dog: dắt chó đi dạo"],
        "ex1": "I walk in the park every morning.", "ex1v": "Tôi đi bộ trong công viên mỗi sáng.",
        "ex2": "Walking meetings encourage creativity.", "ex2v": "Các cuộc họp đi bộ khuyến khích sự sáng tạo.",
        "ex3": "They walk into the sunset.", "ex3v": "Họ đi bộ về phía hoàng hôn.",
        "fam": "Walker (n), Walking (n)", "syn": "stroll, hike", "ant": "run, stay"
    },
    {
        "word": "Paint", "pos": "v", "ipa": "/peɪnt/", "lvl": "A2", "ctx": "Daily",
        "en": "Apply paint to a surface as a hobby or art.",
        "vn": "Vẽ, sơn",
        "m": "Paint - 'Bên' này đang vẽ tranh.",
        "cols": ["paint a picture: vẽ một bức tranh", "oil paint: sơn dầu"],
        "ex1": "She likes to paint landscapes.", "ex1v": "Cô ấy thích vẽ phong cảnh.",
        "ex2": "Painting requires understanding of color theory.", "ex2v": "Vẽ đòi hỏi sự hiểu biết về lý thuyết màu sắc.",
        "ex3": "The artist paints a masterpiece on screen.", "ex3v": "Người nghệ sĩ vẽ một kiệt tác trên màn ảnh.",
        "fam": "Painter (n), Painting (n)", "syn": "draw, color", "ant": "erase"
    },
    {
        "word": "Sing", "pos": "v", "ipa": "/sɪŋ/", "lvl": "A1", "ctx": "Daily",
        "en": "Make musical sounds with the voice.",
        "vn": "Hát",
        "m": "Sing - Sinh ra đã thích hát.",
        "cols": ["sing a song: hát một bài", "sing karaoke: hát karaoke"],
        "ex1": "He sings beautifully.", "ex1v": "Anh ấy hát rất hay.",
        "ex2": "Vocal training is essential to sing professionally.", "ex2v": "Luyện thanh là cần thiết để hát chuyên nghiệp.",
        "ex3": "The choir sings in the opening scene.", "ex3v": "Dàn hợp xướng hát trong cảnh mở đầu.",
        "fam": "Singer (n), Song (n)", "syn": "vocalize, hum", "ant": "be silent"
    },
    {
        "word": "Travel", "pos": "v", "ipa": "/ˈtrævl/", "lvl": "A2", "ctx": "Daily",
        "en": "Make a journey, typically of some length.",
        "vn": "Du lịch",
        "m": "Travel - Trà và vờ đi du lịch.",
        "cols": ["travel abroad: du lịch nước ngoài", "travel light: đi du lịch mang ít đồ"],
        "ex1": "We plan to travel to Japan.", "ex1v": "Chúng tôi dự định du lịch Nhật Bản.",
        "ex2": "International travel broadens one's perspective.", "ex2v": "Du lịch quốc tế mở rộng tầm nhìn của một người.",
        "ex3": "The film is about time travel.", "ex3v": "Bộ phim nói về du hành thời gian.",
        "fam": "Traveler (n), Traveling (n)", "syn": "journey, tour", "ant": "stay"
    },
    {
        "word": "Garden", "pos": "v", "ipa": "/ˈɡɑːdn/", "lvl": "A2", "ctx": "Daily",
        "en": "Cultivate or work in a garden.",
        "vn": "Làm vườn",
        "m": "Garden - Gà đến phá vườn.",
        "cols": ["do the gardening: làm vườn", "flower garden: vườn hoa"],
        "ex1": "My mom gardens every Sunday.", "ex1v": "Mẹ tôi làm vườn mỗi Chủ nhật.",
        "ex2": "Urban gardening is a sustainable practice.", "ex2v": "Làm vườn đô thị là một thực hành bền vững.",
        "ex3": "The secret garden blooms in spring.", "ex3v": "Khu vườn bí mật nở hoa vào mùa xuân.",
        "fam": "Gardener (n), Gardening (n)", "syn": "plant, cultivate", "ant": "destroy"
    },
    {
        "word": "Cook", "pos": "v", "ipa": "/kʊk/", "lvl": "A1", "ctx": "Daily",
        "en": "Prepare food by heating it.",
        "vn": "Nấu ăn",
        "m": "Cook - Cúc (tên) rất thích nấu ăn.",
        "cols": ["cook dinner: nấu bữa tối", "learn to cook: học nấu ăn"],
        "ex1": "I cook for my family daily.", "ex1v": "Tôi nấu ăn cho gia đình mỗi ngày.",
        "ex2": "Culinary students learn how to cook efficiently.", "ex2v": "Sinh viên ẩm thực học cách nấu ăn hiệu quả.",
        "ex3": "Ratatouille is about a rat who loves to cook.", "ex3v": "Ratatouille kể về một chú chuột thích nấu ăn.",
        "fam": "Cooker (n), Cooking (n)", "syn": "bake, fry", "ant": "eat raw"
    },

    # B1-B2 (20 words)
    {
        "word": "Entertainment", "pos": "n", "ipa": "/ˌentəˈteɪnmənt/", "lvl": "B1", "ctx": "Formal",
        "en": "The action of providing or being provided with amusement or enjoyment.",
        "vn": "Sự giải trí",
        "m": "Entertain (giải trí) + ment (sự) -> sự giải trí.",
        "cols": ["live entertainment: giải trí trực tiếp", "entertainment industry: ngành công nghiệp giải trí"],
        "ex1": "TV is our main source of entertainment.", "ex1v": "TV là nguồn giải trí chính của chúng tôi.",
        "ex2": "The entertainment sector contributes greatly to the economy.", "ex2v": "Khu vực giải trí đóng góp lớn cho nền kinh tế.",
        "ex3": "Tonight's entertainment features a live band.", "ex3v": "Chương trình giải trí tối nay có một ban nhạc sống.",
        "fam": "Entertain (v), Entertaining (adj)", "syn": "amusement, fun", "ant": "boredom"
    },
    {
        "word": "Photography", "pos": "n", "ipa": "/fəˈtɒɡrəfi/", "lvl": "B1", "ctx": "Daily",
        "en": "The art or practice of taking and processing photographs.",
        "vn": "Nhiếp ảnh",
        "m": "Photo (ảnh) + graphy (ghi lại) -> nhiếp ảnh.",
        "cols": ["digital photography: nhiếp ảnh kỹ thuật số", "amateur photography: nhiếp ảnh nghiệp dư"],
        "ex1": "He took up photography as a hobby.", "ex1v": "Anh ấy bắt đầu theo đuổi nhiếp ảnh như một sở thích.",
        "ex2": "Photography plays a key role in visual journalism.", "ex2v": "Nhiếp ảnh đóng vai trò quan trọng trong báo chí trực quan.",
        "ex3": "The movie's photography is stunning.", "ex3v": "Kỹ thuật nhiếp ảnh của bộ phim rất tuyệt vời.",
        "fam": "Photographer (n), Photograph (n)", "syn": "picture-taking", "ant": "None"
    },
    {
        "word": "Instrument", "pos": "n", "ipa": "/ˈɪnstrəmənt/", "lvl": "B1", "ctx": "Daily",
        "en": "An object or device for producing musical sounds.",
        "vn": "Nhạc cụ",
        "m": "In (trong) + stru (trung) + ment -> trong trung tâm có nhạc cụ.",
        "cols": ["play an instrument: chơi nhạc cụ", "musical instrument: nhạc cụ"],
        "ex1": "I want to learn a new instrument.", "ex1v": "Tôi muốn học một nhạc cụ mới.",
        "ex2": "Playing an instrument enhances cognitive skills.", "ex2v": "Chơi nhạc cụ nâng cao kỹ năng nhận thức.",
        "ex3": "She tunes her instrument before the concert.", "ex3v": "Cô ấy chỉnh âm nhạc cụ trước buổi hòa nhạc.",
        "fam": "Instrumental (adj)", "syn": "device, tool", "ant": "None"
    },
    {
        "word": "Jogging", "pos": "n", "ipa": "/ˈdʒɒɡɪŋ/", "lvl": "B1", "ctx": "Daily",
        "en": "The activity of running at a steady, gentle pace.",
        "vn": "Chạy bộ",
        "m": "Jog - dốc sức chạy bộ.",
        "cols": ["go jogging: đi chạy bộ", "morning jogging: chạy bộ buổi sáng"],
        "ex1": "Jogging helps me stay fit.", "ex1v": "Chạy bộ giúp tôi giữ dáng.",
        "ex2": "Regular jogging reduces the risk of heart disease.", "ex2v": "Chạy bộ thường xuyên giảm nguy cơ bệnh tim.",
        "ex3": "The character goes jogging every sunrise.", "ex3v": "Nhân vật đi chạy bộ mỗi lúc bình minh.",
        "fam": "Jog (v), Jogger (n)", "syn": "running, sprinting", "ant": "resting"
    },
    {
        "word": "Craft", "pos": "n", "ipa": "/krɑːft/", "lvl": "B1", "ctx": "Daily",
        "en": "An activity involving skill in making things by hand.",
        "vn": "Đồ thủ công",
        "m": "Craft - ráp các thứ lại thành đồ thủ công.",
        "cols": ["arts and crafts: nghệ thuật và thủ công", "craft fair: hội chợ thủ công"],
        "ex1": "She makes beautiful paper crafts.", "ex1v": "Cô ấy làm đồ thủ công bằng giấy rất đẹp.",
        "ex2": "Local crafts are important for tourism.", "ex2v": "Đồ thủ công địa phương quan trọng đối với du lịch.",
        "ex3": "The witch uses her craft to cast spells.", "ex3v": "Phù thủy sử dụng nghề thủ công của mình để niệm chú.",
        "fam": "Craftsman (n), Crafty (adj)", "syn": "handiwork, trade", "ant": "mass-production"
    },
    {
        "word": "Exhibition", "pos": "n", "ipa": "/ˌeksɪˈbɪʃn/", "lvl": "B1", "ctx": "Formal",
        "en": "A public display of works of art or items of interest.",
        "vn": "Cuộc triển lãm",
        "m": "Exhibit (trưng bày) + ion -> triển lãm.",
        "cols": ["art exhibition: triển lãm nghệ thuật", "hold an exhibition: tổ chức triển lãm"],
        "ex1": "We visited an art exhibition.", "ex1v": "Chúng tôi đã thăm một cuộc triển lãm nghệ thuật.",
        "ex2": "The exhibition showcases innovative technologies.", "ex2v": "Triển lãm trưng bày các công nghệ đổi mới.",
        "ex3": "They steal a painting from the exhibition in the movie.", "ex3v": "Họ đánh cắp một bức tranh từ triển lãm trong phim.",
        "fam": "Exhibit (v), Exhibitor (n)", "syn": "display, show", "ant": "concealment"
    },
    {
        "word": "Concert", "pos": "n", "ipa": "/ˈkɒnsət/", "lvl": "B1", "ctx": "Daily",
        "en": "A musical performance given in public.",
        "vn": "Buổi hòa nhạc",
        "m": "Concert - Con (cùng) cert (chắc chắn) -> cùng nhau đi xem hòa nhạc.",
        "cols": ["attend a concert: tham dự buổi hòa nhạc", "live concert: hòa nhạc trực tiếp"],
        "ex1": "I got tickets for the rock concert.", "ex1v": "Tôi có vé xem buổi hòa nhạc rock.",
        "ex2": "The symphony concert raised funds for charity.", "ex2v": "Buổi hòa nhạc giao hưởng gây quỹ từ thiện.",
        "ex3": "The film ends with a massive concert.", "ex3v": "Phim kết thúc bằng một buổi hòa nhạc hoành tráng.",
        "fam": "None", "syn": "gig, show", "ant": "None"
    },
    {
        "word": "Boardgame", "pos": "n", "ipa": "/ˈbɔːd ɡeɪm/", "lvl": "B1", "ctx": "Daily",
        "en": "A game played on a board by people moving pieces.",
        "vn": "Trò chơi cờ bàn",
        "m": "Board (bảng) + game (trò chơi).",
        "cols": ["play a boardgame: chơi cờ bàn", "strategy boardgame: cờ bàn chiến thuật"],
        "ex1": "Monopoly is my favorite boardgame.", "ex1v": "Cờ tỷ phú là trò chơi cờ bàn yêu thích của tôi.",
        "ex2": "Boardgames improve strategic thinking in children.", "ex2v": "Cờ bàn cải thiện tư duy chiến lược ở trẻ em.",
        "ex3": "Jumanji is a movie about a magical boardgame.", "ex3v": "Jumanji là phim về một trò chơi cờ bàn ma thuật.",
        "fam": "None", "syn": "tabletop game", "ant": "video game"
    },
    {
        "word": "Meditation", "pos": "n", "ipa": "/ˌmedɪˈteɪʃn/", "lvl": "B2", "ctx": "Daily",
        "en": "The practice of thinking deeply in silence for relaxation.",
        "vn": "Thiền",
        "m": "Meditate (thiền) + ion -> sự thiền.",
        "cols": ["practice meditation: tập thiền", "guided meditation: thiền có hướng dẫn"],
        "ex1": "Meditation helps me clear my mind.", "ex1v": "Thiền giúp tôi thanh lọc tâm trí.",
        "ex2": "Meditation has proven psychological benefits.", "ex2v": "Thiền có những lợi ích tâm lý đã được chứng minh.",
        "ex3": "The monk practices meditation on the mountain.", "ex3v": "Nhà sư tập thiền trên núi.",
        "fam": "Meditate (v), Meditative (adj)", "syn": "contemplation, reflection", "ant": "agitation"
    },
    {
        "word": "Amusement", "pos": "n", "ipa": "/əˈmjuːzmənt/", "lvl": "B2", "ctx": "Formal",
        "en": "The state or experience of finding something funny or entertaining.",
        "vn": "Sự giải trí, vui chơi",
        "m": "Amuse (làm vui) + ment -> sự làm vui.",
        "cols": ["amusement park: công viên giải trí", "to one's amusement: làm ai đó vui vẻ"],
        "ex1": "We went to the amusement park.", "ex1v": "Chúng tôi đã đi công viên giải trí.",
        "ex2": "The activity was provided for the students' amusement.", "ex2v": "Hoạt động được cung cấp để học sinh vui chơi.",
        "ex3": "He watched the comedy with great amusement.", "ex3v": "Anh ấy xem hài kịch với sự thích thú lớn.",
        "fam": "Amuse (v), Amusing (adj)", "syn": "enjoyment, delight", "ant": "sadness, boredom"
    },
    {
        "word": "Volunteer", "pos": "v", "ipa": "/ˌvɒlənˈtɪə(r)/", "lvl": "B1", "ctx": "Daily",
        "en": "Freely offer to do something.",
        "vn": "Tình nguyện",
        "m": "Vo (vô) + lun (luôn) + teer -> vô luôn làm tình nguyện.",
        "cols": ["volunteer work: công việc tình nguyện", "volunteer for a charity: tình nguyện cho tổ chức từ thiện"],
        "ex1": "I volunteer at the local shelter.", "ex1v": "Tôi làm tình nguyện tại mái ấm địa phương.",
        "ex2": "Volunteering provides valuable work experience.", "ex2v": "Tình nguyện cung cấp kinh nghiệm làm việc quý báu.",
        "ex3": "Katniss volunteers as tribute.", "ex3v": "Katniss tình nguyện làm vật tế thần.",
        "fam": "Voluntary (adj)", "syn": "offer, step forward", "ant": "refuse, compel"
    },
    {
        "word": "Socialize", "pos": "v", "ipa": "/ˈsəʊʃəlaɪz/", "lvl": "B2", "ctx": "Daily",
        "en": "Participate in social activities; mix socially with others.",
        "vn": "Giao lưu",
        "m": "Social (xã hội) + ize -> hòa nhập xã hội.",
        "cols": ["socialize with friends: giao lưu với bạn bè", "difficult to socialize: khó giao lưu"],
        "ex1": "I like to socialize on weekends.", "ex1v": "Tôi thích giao lưu vào cuối tuần.",
        "ex2": "Networking events allow professionals to socialize.", "ex2v": "Các sự kiện mạng lưới cho phép chuyên gia giao lưu.",
        "ex3": "The characters socialize at the grand ball.", "ex3v": "Các nhân vật giao lưu tại vũ hội lớn.",
        "fam": "Socialization (n), Social (adj)", "syn": "mingle, interact", "ant": "isolate"
    },
    {
        "word": "Pottery", "pos": "n", "ipa": "/ˈpɒtəri/", "lvl": "B2", "ctx": "Daily",
        "en": "The craft of making ceramic material into pots or wares.",
        "vn": "Đồ gốm",
        "m": "Pot (cái bình) + tery -> nghề làm bình gốm.",
        "cols": ["make pottery: làm gốm", "pottery class: lớp học làm gốm"],
        "ex1": "She took a pottery class.", "ex1v": "Cô ấy đã tham gia một lớp học làm gốm.",
        "ex2": "Ancient pottery helps archaeologists understand history.", "ex2v": "Gốm cổ giúp các nhà khảo cổ hiểu về lịch sử.",
        "ex3": "The famous romantic scene involves making pottery.", "ex3v": "Cảnh lãng mạn nổi tiếng liên quan đến việc làm gốm.",
        "fam": "Potter (n)", "syn": "ceramics", "ant": "None"
    },
    {
        "word": "Bake", "pos": "v", "ipa": "/beɪk/", "lvl": "B1", "ctx": "Daily",
        "en": "Cook food by dry heat without direct exposure to a flame.",
        "vn": "Nướng bánh",
        "m": "Bake - Bê cái bánh đi nướng.",
        "cols": ["bake a cake: nướng bánh", "baking powder: bột nở"],
        "ex1": "I love to bake cookies.", "ex1v": "Tôi thích nướng bánh quy.",
        "ex2": "Baking requires precise measurements.", "ex2v": "Nướng bánh yêu cầu đo lường chính xác.",
        "ex3": "They bake pies for the town festival.", "ex3v": "Họ nướng bánh pie cho lễ hội thị trấn.",
        "fam": "Baker (n), Bakery (n)", "syn": "roast, cook", "ant": "freeze"
    },
    {
        "word": "Camp", "pos": "v", "ipa": "/kæmp/", "lvl": "B1", "ctx": "Daily",
        "en": "Live for a time in a tent, especially while on holiday.",
        "vn": "Cắm trại",
        "m": "Camp - Cầm lều đi cắm trại.",
        "cols": ["go camping: đi cắm trại", "summer camp: trại hè"],
        "ex1": "We camp in the mountains every summer.", "ex1v": "Chúng tôi cắm trại trên núi mỗi mùa hè.",
        "ex2": "Camping promotes outdoor survival skills.", "ex2v": "Cắm trại thúc đẩy kỹ năng sinh tồn ngoài trời.",
        "ex3": "The kids camp in the backyard in the movie.", "ex3v": "Những đứa trẻ cắm trại ở sân sau trong phim.",
        "fam": "Camper (n), Camping (n)", "syn": "tent, bivouac", "ant": "stay indoors"
    },
    {
        "word": "Hike", "pos": "v", "ipa": "/haɪk/", "lvl": "B1", "ctx": "Daily",
        "en": "Walk for a long distance, especially across country.",
        "vn": "Đi bộ đường dài",
        "m": "Hike - Hái hoa khi đi bộ đường dài.",
        "cols": ["go hiking: đi bộ đường dài", "hiking trail: đường mòn đi bộ"],
        "ex1": "We hiked up the hill.", "ex1v": "Chúng tôi đi bộ lên đồi.",
        "ex2": "Hiking is a popular ecotourism activity.", "ex2v": "Đi bộ đường dài là một hoạt động du lịch sinh thái phổ biến.",
        "ex3": "They hike through the wilderness to find treasure.", "ex3v": "Họ đi bộ qua nơi hoang dã để tìm kho báu.",
        "fam": "Hiker (n), Hiking (n)", "syn": "trek, walk", "ant": "ride"
    },
    {
        "word": "Tournament", "pos": "n", "ipa": "/ˈtʊənəmənt/", "lvl": "B2", "ctx": "Formal",
        "en": "A series of contests between a number of competitors.",
        "vn": "Giải đấu",
        "m": "Tour (chuyến đi) + nament -> đi đấu giải.",
        "cols": ["chess tournament: giải đấu cờ vua", "win a tournament: thắng giải đấu"],
        "ex1": "He won the local tennis tournament.", "ex1v": "Anh ấy đã thắng giải quần vợt địa phương.",
        "ex2": "Organizing a sports tournament requires meticulous planning.", "ex2v": "Tổ chức giải thể thao đòi hỏi lập kế hoạch tỉ mỉ.",
        "ex3": "The karate tournament is the movie's climax.", "ex3v": "Giải đấu karate là cao trào của phim.",
        "fam": "None", "syn": "competition, match", "ant": "None"
    },
    {
        "word": "Leisure", "pos": "n", "ipa": "/ˈleʒə(r)/", "lvl": "B1", "ctx": "Academic",
        "en": "Free time when one is not working.",
        "vn": "Thời gian rảnh rỗi",
        "m": "Leisure - Lê la lúc rảnh rỗi.",
        "cols": ["leisure time: thời gian rảnh", "leisure activities: hoạt động giải trí"],
        "ex1": "What do you do in your leisure time?", "ex1v": "Bạn làm gì vào thời gian rảnh?",
        "ex2": "The study analyzes changes in leisure habits.", "ex2v": "Nghiên cứu phân tích những thay đổi trong thói quen giải trí.",
        "ex3": "The wealthy characters have abundant leisure.", "ex3v": "Các nhân vật giàu có có rất nhiều thời gian rảnh rỗi.",
        "fam": "Leisurely (adj)", "syn": "free time, spare time", "ant": "work, labor"
    },
    {
        "word": "Unwind", "pos": "v", "ipa": "/ˌʌnˈwaɪnd/", "lvl": "B2", "ctx": "Daily",
        "en": "Relax after a period of work or tension.",
        "vn": "Thư giãn, xả hơi",
        "m": "Un (không) + wind (cuộn) -> mở cuộn dây ra, tức là xả hơi.",
        "cols": ["unwind after work: xả hơi sau giờ làm", "unwind with a book: thư giãn với một cuốn sách"],
        "ex1": "A hot bath helps me unwind.", "ex1v": "Tắm nước nóng giúp tôi xả hơi.",
        "ex2": "It is important for employees to have time to unwind.", "ex2v": "Việc nhân viên có thời gian xả hơi là rất quan trọng.",
        "ex3": "He unwinds at the local bar after a hard day.", "ex3v": "Anh ấy xả hơi tại quán bar địa phương sau một ngày mệt nhọc.",
        "fam": "None", "syn": "relax, wind down", "ant": "stress, tense"
    },
    {
        "word": "Pastime", "pos": "n", "ipa": "/ˈpɑːstaɪm/", "lvl": "B2", "ctx": "Academic",
        "en": "An activity that someone does regularly for enjoyment.",
        "vn": "Thú vui",
        "m": "Pass (trôi qua) + time (thời gian) -> thú vui giết thời gian.",
        "cols": ["favorite pastime: thú vui yêu thích", "national pastime: thú vui quốc gia"],
        "ex1": "Reading is my favorite pastime.", "ex1v": "Đọc sách là thú vui yêu thích của tôi.",
        "ex2": "Baseball is known as America's national pastime.", "ex2v": "Bóng chày được biết đến là thú vui quốc gia của Mỹ.",
        "ex3": "In the Victorian era, embroidery was a common pastime.", "ex3v": "Thời kỳ Victoria, thêu thùa là một thú vui phổ biến.",
        "fam": "None", "syn": "hobby, recreation", "ant": "chore, work"
    },

    # C1-C2 (15 words)
    {
        "word": "Excursion", "pos": "n", "ipa": "/ɪkˈskɜːʃn/", "lvl": "C1", "ctx": "Formal",
        "en": "A short journey or trip, especially one engaged in as a leisure activity.",
        "vn": "Chuyến du ngoạn",
        "m": "Ex (ra ngoài) + cursion -> đi ra ngoài dạo chơi.",
        "cols": ["go on an excursion: đi du ngoạn", "weekend excursion: chuyến du ngoạn cuối tuần"],
        "ex1": "We went on an excursion to the mountains.", "ex1v": "Chúng tôi đã đi du ngoạn trên núi.",
        "ex2": "Educational excursions enhance students' learning experiences.", "ex2v": "Các chuyến du ngoạn giáo dục nâng cao trải nghiệm học tập của học sinh.",
        "ex3": "The crew's shore excursion turned into an adventure.", "ex3v": "Chuyến du ngoạn trên bờ của phi hành đoàn biến thành một cuộc phiêu lưu.",
        "fam": "None", "syn": "trip, outing", "ant": "staycation"
    },
    {
        "word": "Philately", "pos": "n", "ipa": "/fɪˈlætəli/", "lvl": "C2", "ctx": "Academic",
        "en": "The collection and study of postage stamps.",
        "vn": "Thú sưu tập tem",
        "m": "Phil (yêu thích) + ately -> yêu thích tem.",
        "cols": ["rare philately: tem hiếm", "philately exhibition: triển lãm tem"],
        "ex1": "His grandfather introduced him to philately.", "ex1v": "Ông nội đã giới thiệu cho anh ấy thú sưu tập tem.",
        "ex2": "Philately can be a highly lucrative alternative investment.", "ex2v": "Sưu tập tem có thể là một khoản đầu tư thay thế sinh lời cao.",
        "ex3": "The movie features a rare stamp sought by experts in philately.", "ex3v": "Bộ phim có một con tem hiếm được các chuyên gia sưu tập tem săn lùng.",
        "fam": "Philatelist (n)", "syn": "stamp collecting", "ant": "None"
    },
    {
        "word": "Numismatics", "pos": "n", "ipa": "/ˌnjuːmɪzˈmætɪks/", "lvl": "C2", "ctx": "Academic",
        "en": "The study or collection of coins, paper money, and medals.",
        "vn": "Thú sưu tập tiền xu",
        "m": "Numis (số/tiền) -> học thuật về tiền xu.",
        "cols": ["expert in numismatics: chuyên gia về sưu tập tiền xu", "numismatics club: câu lạc bộ sưu tập tiền xu"],
        "ex1": "Numismatics is a fascinating hobby for history buffs.", "ex1v": "Sưu tập tiền xu là thú vui hấp dẫn cho người đam mê lịch sử.",
        "ex2": "Numismatics offers insights into the economic history of civilizations.", "ex2v": "Sưu tập tiền xu cung cấp cái nhìn sâu sắc về lịch sử kinh tế.",
        "ex3": "The thief stole a priceless coin valued in numismatics.", "ex3v": "Tên trộm đã đánh cắp một đồng xu vô giá trong giới sưu tập.",
        "fam": "Numismatist (n)", "syn": "coin collecting", "ant": "None"
    },
    {
        "word": "Rejuvenate", "pos": "v", "ipa": "/rɪˈdʒuːvəneɪt/", "lvl": "C1", "ctx": "Formal",
        "en": "Make someone or something look or feel younger, fresher, or more lively.",
        "vn": "Làm trẻ lại, phục hồi",
        "m": "Re (lại) + juven (trẻ) -> làm trẻ lại.",
        "cols": ["rejuvenate the mind: phục hồi tâm trí", "feel rejuvenated: cảm thấy được trẻ lại"],
        "ex1": "A weekend spa trip rejuvenated her.", "ex1v": "Chuyến đi spa cuối tuần đã giúp cô ấy phục hồi.",
        "ex2": "The company needs a new CEO to rejuvenate its operations.", "ex2v": "Công ty cần một CEO mới để vực dậy hoạt động.",
        "ex3": "The magic potion rejuvenates the old wizard.", "ex3v": "Liều thuốc tiên làm vị pháp sư già trẻ lại.",
        "fam": "Rejuvenation (n)", "syn": "revive, refresh", "ant": "exhaust, tire"
    },
    {
        "word": "Calligraphy", "pos": "n", "ipa": "/kəˈlɪɡrəfi/", "lvl": "C1", "ctx": "Academic",
        "en": "Decorative handwriting or handwritten lettering.",
        "vn": "Thư pháp",
        "m": "Calli (đẹp) + graphy (viết) -> viết chữ đẹp.",
        "cols": ["Chinese calligraphy: thư pháp Trung Quốc", "practice calligraphy: luyện thư pháp"],
        "ex1": "She wrote the invitations in beautiful calligraphy.", "ex1v": "Cô ấy viết thiệp mời bằng thư pháp tuyệt đẹp.",
        "ex2": "Calligraphy requires intense concentration and fine motor skills.", "ex2v": "Thư pháp đòi hỏi sự tập trung cao độ và kỹ năng vận động tinh.",
        "ex3": "The ancient scroll showcases exquisite calligraphy.", "ex3v": "Cuộn giấy cổ trưng bày nghệ thuật thư pháp tinh tế.",
        "fam": "Calligrapher (n)", "syn": "penmanship", "ant": "scribble"
    },
    {
        "word": "Mountaineering", "pos": "n", "ipa": "/ˌmaʊntəˈnɪərɪŋ/", "lvl": "C1", "ctx": "Formal",
        "en": "The sport or activity of climbing mountains.",
        "vn": "Môn leo núi",
        "m": "Mountain (núi) + eering -> việc leo núi.",
        "cols": ["mountaineering expedition: chuyến thám hiểm leo núi", "mountaineering gear: dụng cụ leo núi"],
        "ex1": "Mountaineering is a dangerous but thrilling hobby.", "ex1v": "Leo núi là một sở thích nguy hiểm nhưng thú vị.",
        "ex2": "Mountaineering requires rigorous physical conditioning.", "ex2v": "Leo núi yêu cầu thể lực nghiêm ngặt.",
        "ex3": "The documentary covers the perils of high-altitude mountaineering.", "ex3v": "Phim tài liệu đề cập đến những nguy hiểm của leo núi độ cao lớn.",
        "fam": "Mountaineer (n)", "syn": "mountain climbing, alpinism", "ant": "None"
    },
    {
        "word": "Gastronomy", "pos": "n", "ipa": "/ɡæˈstrɒnəmi/", "lvl": "C2", "ctx": "Academic",
        "en": "The practice or art of choosing, cooking, and eating good food.",
        "vn": "Ẩm thực học",
        "m": "Gastro (dạ dày) + nomy (học thuật) -> nghệ thuật ăn uống.",
        "cols": ["molecular gastronomy: ẩm thực phân tử", "fine gastronomy: nghệ thuật ẩm thực tinh tế"],
        "ex1": "He studies French gastronomy.", "ex1v": "Anh ấy nghiên cứu ẩm thực Pháp.",
        "ex2": "Gastronomy is deeply intertwined with cultural identity.", "ex2v": "Ẩm thực học đan xen sâu sắc với bản sắc văn hóa.",
        "ex3": "The chef's skills in molecular gastronomy amazed the critics.", "ex3v": "Kỹ năng ẩm thực phân tử của đầu bếp khiến các nhà phê bình kinh ngạc.",
        "fam": "Gastronomic (adj)", "syn": "culinary arts", "ant": "None"
    },
    {
        "word": "Bibliophile", "pos": "n", "ipa": "/ˈbɪbliəfaɪl/", "lvl": "C2", "ctx": "Academic",
        "en": "A person who collects or has a great love of books.",
        "vn": "Người yêu sách",
        "m": "Biblio (sách) + phile (người yêu thích).",
        "cols": ["avid bibliophile: người đam mê sách", "bibliophile club: câu lạc bộ người yêu sách"],
        "ex1": "As a bibliophile, his room is filled with books.", "ex1v": "Là một người yêu sách, phòng anh ấy đầy sách.",
        "ex2": "The rare manuscript was purchased by a wealthy bibliophile.", "ex2v": "Bản thảo quý hiếm được mua bởi một người yêu sách giàu có.",
        "ex3": "The protagonist is a bibliophile who discovers a magical book.", "ex3v": "Nhân vật chính là người yêu sách đã phát hiện ra cuốn sách ma thuật.",
        "fam": "None", "syn": "bookworm", "ant": "None"
    },
    {
        "word": "Equestrianism", "pos": "n", "ipa": "/ɪˈkwestriənɪzəm/", "lvl": "C2", "ctx": "Formal",
        "en": "The skill or sport of horse riding.",
        "vn": "Môn cưỡi ngựa",
        "m": "Equus (ngựa trong tiếng Latin) -> equestrian (thuộc về ngựa).",
        "cols": ["equestrianism events: các sự kiện cưỡi ngựa", "master equestrianism: thành thạo môn cưỡi ngựa"],
        "ex1": "She has a passion for equestrianism.", "ex1v": "Cô ấy có niềm đam mê với môn cưỡi ngựa.",
        "ex2": "Equestrianism has been an Olympic sport since 1900.", "ex2v": "Môn cưỡi ngựa đã là môn thể thao Olympic từ năm 1900.",
        "ex3": "The elite family prides itself on its equestrianism traditions.", "ex3v": "Gia đình tinh hoa tự hào về truyền thống cưỡi ngựa.",
        "fam": "Equestrian (adj/n)", "syn": "horseback riding", "ant": "None"
    },
    {
        "word": "Connoisseur", "pos": "n", "ipa": "/ˌkɒnəˈsɜː(r)/", "lvl": "C2", "ctx": "Formal",
        "en": "An expert judge in matters of taste.",
        "vn": "Người sành sỏi",
        "m": "Connoisseur - Cổ (con) nói (noi) sờ sờ, chứng tỏ chuyên gia sành sỏi.",
        "cols": ["wine connoisseur: người sành rượu", "art connoisseur: người sành nghệ thuật"],
        "ex1": "He is a connoisseur of Italian food.", "ex1v": "Anh ấy là người sành ăn đồ ăn Ý.",
        "ex2": "To appreciate the subtle flavors, one must be a coffee connoisseur.", "ex2v": "Để trân trọng những hương vị tinh tế, người ta phải là người sành cà phê.",
        "ex3": "The villain is a wealthy art connoisseur.", "ex3v": "Nhân vật phản diện là một người sành nghệ thuật giàu có.",
        "fam": "None", "syn": "expert, specialist", "ant": "ignoramus"
    },
    {
        "word": "Enthrall", "pos": "v", "ipa": "/ɪnˈθrɔːl/", "lvl": "C2", "ctx": "Formal",
        "en": "Capture the fascinated attention of.",
        "vn": "Làm say mê",
        "m": "En (vào) + thrall (nô lệ) -> biến ai thành nô lệ của sự say mê.",
        "cols": ["be enthralled by: bị say mê bởi", "enthralling performance: màn trình diễn say đắm"],
        "ex1": "The children were enthralled by the magic show.", "ex1v": "Bọn trẻ bị say mê bởi màn ảo thuật.",
        "ex2": "The novel has the power to enthrall its readers entirely.", "ex2v": "Cuốn tiểu thuyết có sức mạnh làm say mê hoàn toàn độc giả.",
        "ex3": "The heroine is enthralled by the mysterious stranger.", "ex3v": "Nữ chính bị say mê bởi người lạ bí ẩn.",
        "fam": "Enthralling (adj)", "syn": "captivate, fascinate", "ant": "bore, repel"
    },
    {
        "word": "Avocation", "pos": "n", "ipa": "/ˌævəˈkeɪʃn/", "lvl": "C2", "ctx": "Formal",
        "en": "A hobby or minor occupation.",
        "vn": "Nghề phụ, thú vui",
        "m": "A (không) + vocation (nghề nghiệp chính) -> nghề phụ, thú vui.",
        "cols": ["pursue an avocation: theo đuổi thú vui", "avocation and vocation: nghề phụ và nghề chính"],
        "ex1": "Photography is his avocation, not his job.", "ex1v": "Nhiếp ảnh là thú vui của anh ấy, không phải công việc.",
        "ex2": "Many professionals find an avocation to balance their stressful careers.", "ex2v": "Nhiều chuyên gia tìm một thú vui để cân bằng sự nghiệp căng thẳng.",
        "ex3": "The detective's avocation is playing the violin.", "ex3v": "Thú vui của vị thám tử là chơi vĩ cầm.",
        "fam": "Avocational (adj)", "syn": "hobby, side interest", "ant": "profession, vocation"
    },
    {
        "word": "Tranquility", "pos": "n", "ipa": "/træŋˈkwɪləti/", "lvl": "C1", "ctx": "Formal",
        "en": "The quality or state of being tranquil; calm.",
        "vn": "Sự yên tĩnh, thanh bình",
        "m": "Tranquil (yên bình) + ity -> sự yên bình.",
        "cols": ["peace and tranquility: hòa bình và yên tĩnh", "sense of tranquility: cảm giác thanh bình"],
        "ex1": "I love the tranquility of the countryside.", "ex1v": "Tôi thích sự thanh bình của vùng quê.",
        "ex2": "Achieving mental tranquility is essential for well-being.", "ex2v": "Đạt được sự thanh bình tâm trí là cần thiết cho sức khỏe.",
        "ex3": "The garden scene evokes a deep sense of tranquility.", "ex3v": "Cảnh khu vườn gợi lên cảm giác thanh bình sâu sắc.",
        "fam": "Tranquil (adj)", "syn": "peace, calmness", "ant": "chaos, noise"
    },
    {
        "word": "Dilettante", "pos": "n", "ipa": "/ˌdɪləˈtænti/", "lvl": "C2", "ctx": "Academic",
        "en": "A person who cultivates an area of interest, such as the arts, without real commitment or knowledge.",
        "vn": "Người chơi tài tử, người am hiểu nông cạn",
        "m": "Dile (đi lang thang) + tante -> lang thang chơi bời không chuyên.",
        "cols": ["wealthy dilettante: người tài tử giàu có", "act like a dilettante: hành động như dân nghiệp dư"],
        "ex1": "He's just a dilettante when it comes to painting.", "ex1v": "Anh ta chỉ là tay chơi tài tử khi nói đến hội họa.",
        "ex2": "The art world often dismisses a dilettante for lacking formal training.", "ex2v": "Thế giới nghệ thuật thường gạt bỏ một tay tài tử vì thiếu đào tạo bài bản.",
        "ex3": "The rich heir plays the role of a dilettante.", "ex3v": "Người thừa kế giàu có đóng vai một tay tài tử.",
        "fam": "None", "syn": "amateur, dabbler", "ant": "professional, expert"
    },
    {
        "word": "Horticulture", "pos": "n", "ipa": "/ˈhɔːtɪkʌltʃə(r)/", "lvl": "C1", "ctx": "Academic",
        "en": "The art or practice of garden cultivation and management.",
        "vn": "Nghề làm vườn",
        "m": "Horti (vườn) + culture (nuôi trồng) -> nghề trồng trọt, làm vườn.",
        "cols": ["study horticulture: học nghề làm vườn", "horticulture exhibition: triển lãm làm vườn"],
        "ex1": "She has a degree in horticulture.", "ex1v": "Cô ấy có bằng cấp về nghề làm vườn.",
        "ex2": "Horticulture is critical for sustainable urban landscaping.", "ex2v": "Nghề làm vườn rất quan trọng cho cảnh quan đô thị bền vững.",
        "ex3": "The royal gardens are a masterpiece of horticulture.", "ex3v": "Khu vườn hoàng gia là kiệt tác của nghệ thuật làm vườn.",
        "fam": "Horticultural (adj)", "syn": "gardening, agriculture", "ant": "None"
    }
]

template = '''# {word}
*{pos}*
> {ipa}

---
**Level:** {lvl} | **Ngữ cảnh:** {ctx} | **Chủ đề:** {topic}

## 📌 Ý nghĩa (Meaning)
- **[EN]:** {en}
- **[VN]:** {vn}

## 🧠 Mẹo nhớ (Mnemonics)
💡 {m}

## 🧩 Cụm từ thường đi kèm (Collocations)
{collocations}

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
'''

os.makedirs(output_dir, exist_ok=True)

for data in words_data:
    col_str = "\\n".join([f"- `{c.split(':')[0].strip()}`: {c.split(':')[1].strip()}" for c in data['cols']])
    
    content = template.format(
        word=data['word'],
        pos=data['pos'],
        ipa=data['ipa'],
        lvl=data['lvl'],
        ctx=data['ctx'],
        topic=topic,
        en=data['en'],
        vn=data['vn'],
        m=data['m'],
        collocations=col_str,
        ex1=data['ex1'], ex1v=data['ex1v'],
        ex2=data['ex2'], ex2v=data['ex2v'],
        ex3=data['ex3'], ex3v=data['ex3v'],
        fam=data['fam'],
        syn=data['syn'],
        ant=data['ant']
    )
    
    file_path = os.path.join(output_dir, f"{data['word']}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Successfully generated 50 vocabulary markdown files.")
