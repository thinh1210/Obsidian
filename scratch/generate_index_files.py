import os

BASE_DIR = "/home/thinh/Obsidian/English/Writing"

task1_types = [
    ("bar_chart", "Bar Chart (Biểu đồ cột)", "📊", "0_Bar_Chart_Index.md"),
    ("line_graph", "Line Graph (Biểu đồ đường)", "📈", "0_Line_Graph_Index.md"),
    ("pie_chart", "Pie Chart (Biểu đồ tròn)", "🥧", "0_Pie_Chart_Index.md"),
    ("table", "Table (Bảng số liệu)", "📋", "0_Table_Index.md"),
    ("map", "Map (Bản đồ biến đổi)", "🗺️", "0_Map_Index.md"),
    ("process", "Process (Quy trình sản xuất / Tự nhiên)", "⚙️", "0_Process_Index.md"),
    ("mixed_chart", "Mixed Chart (Biểu đồ kết hợp)", "📑", "0_Mixed_Chart_Index.md"),
]

task2_types = [
    ("agree_disagree", "Agree or Disagree (Quan điểm / Opinion)", "⚖️", "0_Agree_Disagree_Index.md"),
    ("discuss_both_views", "Discuss Both Views (Thảo luận 2 mặt)", "👥", "0_Discuss_Both_Views_Index.md"),
    ("problem_solution", "Cause / Problem & Solution (Nguyên nhân & Giải pháp)", "🔍", "0_Problem_Solution_Index.md"),
    ("advantages_disadvantages", "Advantages & Disadvantages (Lợi ích & Bất lợi)", "⚖️", "0_Advantages_Disadvantages_Index.md"),
    ("direct_questions", "Direct Questions (Câu hỏi trực tiếp / Hai phần)", "❓", "0_Direct_Questions_Index.md"),
]

def make_type_index(task, folder, name, icon, index_filename):
    dir_path = os.path.join(BASE_DIR, task, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    files = [f for f in os.listdir(dir_path) if f.endswith(".md") and not f.startswith("0_")]
    files.sort()
    
    rows = []
    for f in files:
        fpath = os.path.join(dir_path, f)
        title = f.replace(".md", "").replace("Sample_", "Bài mẫu ")
        with open(fpath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # parse title from # header
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

    content = f"""---
task: {task.upper()}
type: {name}
tags:
  - ielts/writing
  - index/{folder}
---

# {icon} Mục Lục Dạng Bài: {name}

> [!INFO] Giới Thiệu Dạng Bài
> Thư mục này tập hợp các bài viết mẫu chuẩn Band 8.5 - 9.0 cho dạng **{name}**, đi kèm phân tích dàn ý tư duy, kho từ vựng C1-C2 và khung hướng dẫn viết từng bước.

---

## 📚 Danh Sách Bài Mẫu Đã Phân Tích

| Tiêu Đề Bài Học | Band Mục Tiêu | Chủ Đề (Topic) | Bài Mẫu | Kho Từ Vựng | Hướng Dẫn Viết |
| :--- | :---: | :--- | :---: | :---: | :---: |
{table_content}

---

## 📌 Hướng Dẫn Ôn Luyện Dạng Bài Này
1. **Đọc kỹ đề & dàn ý:** Phân tích cách tác giả bẻ khóa câu hỏi và sắp xếp cấu trúc đoạn mạch lạc.
2. **Học thuộc từ vựng & Collocations:** Đọc bảng Lexical Resource và liên kết các cụm từ đắt giá vào bài tập của riêng bạn.
3. **Thực hành với Template:** Sử dụng mục 5 (*Hướng Dẫn Tự Viết*) để tự viết lại một đề bài tương tự trước khi so sánh với bài mẫu.
"""
    with open(os.path.join(dir_path, index_filename), "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated Index: {index_filename}")

def make_master_index():
    master_path = os.path.join(BASE_DIR, "0_Writing_Master_Index.md")
    
    t1_rows = []
    for folder, name, icon, ifile in task1_types:
        dir_path = os.path.join(BASE_DIR, "task1", folder)
        count = len([f for f in os.listdir(dir_path) if f.endswith(".md") and not f.startswith("0_")])
        note_link = f"task1/{folder}/{ifile}".replace(".md", "")
        t1_rows.append(f"| {icon} **{name}** | `{count} bài mẫu` | [[{note_link}\\|Mục lục chi tiết 🔗]] |")
        
    t2_rows = []
    for folder, name, icon, ifile in task2_types:
        dir_path = os.path.join(BASE_DIR, "task2", folder)
        count = len([f for f in os.listdir(dir_path) if f.endswith(".md") and not f.startswith("0_")])
        note_link = f"task2/{folder}/{ifile}".replace(".md", "")
        t2_rows.append(f"| {icon} **{name}** | `{count} bài mẫu` | [[{note_link}\\|Mục lục chi tiết 🔗]] |")

    t1_table = "\n".join(t1_rows)
    t2_table = "\n".join(t2_rows)

    content = f"""---
title: "IELTS Writing Master Index"
tags:
  - ielts/writing
  - master_index
---

# 📖 IELTS Writing Master Hub: Kho Bài Mẫu & Phân Tích Chuyên Sâu

Chào mừng bạn đến với hệ sinh thái học **IELTS Writing** được chuẩn hóa và lưu trữ trực tiếp trong Obsidian Vault.

> [!TIP] Cấu Trúc Khóa Học Writing
> Mỗi bài học được thiết kế theo chuẩn 5 phần:
> 1. **Đề thi & Minh họa trực quan**
> 2. **Phân tích đề & Dàn ý logic (Idea Generation & Outline)**
> 3. **Bài mẫu chuẩn mực Band 8.5 - 9.0**
> 4. **Kho từ vựng & Collocations C1-C2 (Lexical Resource table)**
> 5. **Cấu trúc ngữ pháp đắt giá & Hướng dẫn tự viết (Writing Guide)**

---

## 📊 1. IELTS Writing Task 1 (Academic Reports)

| Dạng Bài (Task 1 Type) | Số Lượng Bài Đã Có | Liên Kết Mục Lục Chi Tiết |
| :--- | :---: | :--- |
{t1_table}

---

## 📝 2. IELTS Writing Task 2 (Academic Essays)

| Dạng Bài (Task 2 Type) | Số Lượng Bài Đã Có | Liên Kết Mục Lục Chi Tiết |
| :--- | :---: | :--- |
{t2_table}

---

## 🔗 Liên Kết Kho Dữ Liệu Obsidian Khác
- 📂 **Kho Từ Vựng Chủ Đề:** [[English/Vocabulary Topics/]]
- 📐 **Kho Ngữ Pháp & Liên Kết Câu:** [[English/Grammar & Cohesion/]]
- 🎙️ **Luyện Nói IELTS Speaking:** [[English/.agent/SKILL/ielts-speaking-generator/]]
"""
    with open(master_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated Master Index: {master_path}")

if __name__ == "__main__":
    for folder, name, icon, ifile in task1_types:
        make_type_index("task1", folder, name, icon, ifile)
    for folder, name, icon, ifile in task2_types:
        make_type_index("task2", folder, name, icon, ifile)
    make_master_index()
