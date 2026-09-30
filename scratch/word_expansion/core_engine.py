import os
import re
import json
import urllib.request
import urllib.parse
import time
from typing import List, Dict, Any, Union

VAULT_DIR = "/home/thinh/Obsidian"
CAT2_DIR = os.path.join(VAULT_DIR, "English", "Vocabulary Topics", "2. Daily Life & Habits")
AUDIO_DIR = os.path.join(VAULT_DIR, "English", "audio")
JSON_AUDIO_FILE = os.path.join(AUDIO_DIR, "words_to_download.json")

LEVEL_ORDER = {
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4,
    "C1": 5,
    "C2": 6
}

NOTE_TEMPLATE = """# {word}
*{pos}*
> {ipa}

![[{audio_file}]]

---
**Level:** {level} | **Ngữ cảnh:** Daily | **Chủ đề:** {topic} | **Phân nhóm:** {group_name_clean}

## 📌 Ý nghĩa (Meaning)
- **[EN]:** {meaning_en}
- **[VN]:** {meaning_vn}

## 🧠 Mẹo nhớ (Mnemonics)
💡 {mnemonic}

## 🧩 Cụm từ thường đi kèm (Collocations)
{collocations_str}

## 🎬 Ví dụ thực tế (Real-world Examples)
1. 💬 *Daily:* {ex1_en}
   *-> {ex1_vn}*
2. 💼 *Work/Academic:* {ex2_en}
   *-> {ex2_vn}*
3. 🎬 *Media/Movie:* {ex3_en}
   *-> {ex3_vn}*

## 🕸️ Mạng lưới từ (Word Network)
**Word Family:**
{word_family_str}

**Synonyms:** {synonyms}
**Antonyms:** {antonyms}
"""

def clean_audio_filename(word: str) -> str:
    cleaned = re.sub(r"[^\w\-_]", "_", word.strip().replace(" ", "_").replace("-", "_").lower())
    # remove duplicate underscores
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return f"{cleaned}.mp3"

def format_collocations(collocations: Union[List, str]) -> str:
    if isinstance(collocations, str):
        return collocations
    lines = []
    for item in collocations:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            col, vn = item[0], item[1]
            lines.append(f"- `{col}`: {vn}")
        elif isinstance(item, dict):
            col = item.get("col") or item.get("collocation") or item.get("phrase")
            vn = item.get("vn") or item.get("meaning") or item.get("translation")
            lines.append(f"- `{col}`: {vn}")
        elif isinstance(item, str):
            if item.startswith("- "):
                lines.append(item)
            else:
                lines.append(f"- {item}")
    return "\n".join(lines)

def format_examples(examples: Union[List, Dict, str]) -> tuple:
    ex1_en, ex1_vn = "", ""
    ex2_en, ex2_vn = "", ""
    ex3_en, ex3_vn = "", ""

    if isinstance(examples, (list, tuple)):
        if len(examples) >= 1:
            e = examples[0]
            if isinstance(e, (list, tuple)) and len(e) >= 3:
                ex1_en, ex1_vn = e[1], e[2]
            elif isinstance(e, (list, tuple)) and len(e) >= 2:
                ex1_en, ex1_vn = e[0], e[1]
            elif isinstance(e, dict):
                ex1_en = e.get("en", "")
                ex1_vn = e.get("vn", "")
        if len(examples) >= 2:
            e = examples[1]
            if isinstance(e, (list, tuple)) and len(e) >= 3:
                ex2_en, ex2_vn = e[1], e[2]
            elif isinstance(e, (list, tuple)) and len(e) >= 2:
                ex2_en, ex2_vn = e[0], e[1]
            elif isinstance(e, dict):
                ex2_en = e.get("en", "")
                ex2_vn = e.get("vn", "")
        if len(examples) >= 3:
            e = examples[2]
            if isinstance(e, (list, tuple)) and len(e) >= 3:
                ex3_en, ex3_vn = e[1], e[2]
            elif isinstance(e, (list, tuple)) and len(e) >= 2:
                ex3_en, ex3_vn = e[0], e[1]
            elif isinstance(e, dict):
                ex3_en = e.get("en", "")
                ex3_vn = e.get("vn", "")
    elif isinstance(examples, dict):
        ex1_en = examples.get("ex1") or examples.get("daily_en", "")
        ex1_vn = examples.get("ex1v") or examples.get("daily_vn", "")
        ex2_en = examples.get("ex2") or examples.get("work_en", "")
        ex2_vn = examples.get("ex2v") or examples.get("work_vn", "")
        ex3_en = examples.get("ex3") or examples.get("media_en", "")
        ex3_vn = examples.get("ex3v") or examples.get("media_vn", "")

    return ex1_en, ex1_vn, ex2_en, ex2_vn, ex3_en, ex3_vn

def format_word_family(wf: Union[List, str]) -> str:
    if isinstance(wf, str):
        if wf.startswith("- "):
            return wf
        if wf.strip() == "-" or not wf.strip():
            return "- -"
        return f"- {wf}"
    elif isinstance(wf, (list, tuple)):
        if not wf:
            return "- -"
        return "\n".join(f"- {item}" for item in wf)
    return "- -"

def format_word_family_short(wf: Union[List, str]) -> str:
    if isinstance(wf, (list, tuple)):
        return ", ".join(wf) if wf else "-"
    if isinstance(wf, str):
        clean = wf.replace("- ", "").strip()
        return clean if clean else "-"
    return "-"

def get_group_number(group_val: Union[int, str]) -> int:
    if isinstance(group_val, int):
        return group_val
    m = re.search(r"(\d+)", str(group_val))
    if m:
        return int(m.group(1))
    return 1

def update_index_file(topic_name: str, new_words: List[Dict[str, Any]]) -> None:
    index_path = os.path.join(CAT2_DIR, topic_name, f"0_{topic_name}_Index.md")
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Index file not found: {index_path}")

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into sections by major headers
    parts = re.split(r"\n(?=### |## )", content)

    # Map new words to group numbers (1, 2, 3, 4)
    words_by_group = {1: [], 2: [], 3: [], 4: []}
    for w in new_words:
        grp_num = get_group_number(w.get("group_title") or w.get("group") or w.get("group_num", 1))
        words_by_group[grp_num].append(w)

    # 1. Update Semantic Map
    sem_map_idx = None
    for idx, part in enumerate(parts):
        if part.startswith("## 🗺️ Sơ đồ liên kết chủ đề"):
            sem_map_idx = idx
            break

    if sem_map_idx is not None:
        sem_lines = parts[sem_map_idx].splitlines()
        new_sem_lines = []
        for line in sem_lines:
            if line.startswith("- **"):
                # match group number in line
                m_grp = re.search(r"- \*\*.*?\b(\d+)\..*?\*\*.*?\): (.*)", line)
                if m_grp:
                    grp_num = int(m_grp.group(1))
                    existing_links = re.findall(r"\[\[(.*?)\]\]", m_grp.group(2))
                    existing_words_set = {w.strip() for w in existing_links}
                    # Add new words
                    for nw in words_by_group.get(grp_num, []):
                        w_name = nw["word"].strip()
                        existing_words_set.add(w_name)

                    # Sort case-insensitively
                    sorted_words = sorted(list(existing_words_set), key=lambda x: x.lower())
                    links_str = ", ".join(f"[[{w}]]" for w in sorted_words)
                    
                    # reconstruct line preserving prefix
                    prefix = line[:line.find("): ") + 3]
                    new_sem_lines.append(f"{prefix}{links_str}")
                    continue
            new_sem_lines.append(line)
        parts[sem_map_idx] = "\n".join(new_sem_lines)

    # 2. Update Tables under '## Danh sách từ vựng theo nhóm ngữ nghĩa'
    for idx, part in enumerate(parts):
        if part.startswith("### "):
            # Check if this part corresponds to group 1, 2, 3, or 4
            m_header = re.match(r"### .*?\b(\d+)\.", part)
            if m_header:
                grp_num = int(m_header.group(1))
                added_words = words_by_group.get(grp_num, [])
                if not added_words:
                    continue

                lines = part.splitlines()
                non_table_lines = []
                data_rows = []

                for line in lines:
                    if line.startswith("|") and not line.startswith("| Từ vựng") and not line.startswith("| ---"):
                        cols = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
                        if len(cols) >= 7:
                            data_rows.append(cols)
                    else:
                        non_table_lines.append(line)

                # Add new rows
                existing_table_words = {r[0].lower() for r in data_rows}
                for nw in added_words:
                    w_name = nw["word"].strip()
                    if w_name.lower() in existing_table_words:
                        continue
                    audio_fn = clean_audio_filename(w_name)
                    ipa = nw.get("ipa", "")
                    lvl = nw.get("level", "B1")
                    pos = nw.get("pos", "n.")
                    meaning_short = nw.get("meaning_short") or nw.get("meaning_vn", "")
                    wf_short = format_word_family_short(nw.get("word_family", "-"))
                    data_rows.append([
                        w_name,
                        f"{ipa} [[{audio_fn}\\|🔊]]",
                        lvl,
                        pos,
                        meaning_short,
                        wf_short,
                        f"[[{w_name}]]"
                    ])

                # Sort data_rows by Level, then Word
                data_rows.sort(key=lambda r: (LEVEL_ORDER.get(r[2].upper(), 99), r[0].lower()))

                # Reconstruct part
                reconstructed_lines = []
                table_inserted = False
                for line in non_table_lines:
                    reconstructed_lines.append(line)
                    if line.startswith("| ---"):
                        table_inserted = True
                        for r in data_rows:
                            reconstructed_lines.append(
                                f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |"
                            )

                if not table_inserted:
                    # In case table was somehow missing header
                    reconstructed_lines.append("| Từ vựng | Phát âm | Level | Loại từ | Nghĩa ngắn gọn | Word Family | Link Note |")
                    reconstructed_lines.append("| --- | --- | --- | --- | --- | --- | --- |")
                    for r in data_rows:
                        reconstructed_lines.append(
                            f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |"
                        )

                parts[idx] = "\n".join(reconstructed_lines)

    # Reassemble and save
    new_content = "\n".join(parts)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def add_words_to_topic(topic_name: str, word_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    topic_dir = os.path.join(CAT2_DIR, topic_name)
    os.makedirs(topic_dir, exist_ok=True)

    created_notes = []
    words_to_download_additions = {}

    for w in word_list:
        word = w["word"].strip()
        ipa = w.get("ipa", "")
        pos = w.get("pos", "n.")
        level = w.get("level", "B1")
        meaning_en = w.get("meaning_en", "")
        meaning_vn = w.get("meaning_vn", "")
        group_name_clean = w.get("group_name_clean", "")
        mnemonic = w.get("mnemonic", "")
        collocations_str = format_collocations(w.get("collocations", []))
        ex1_en, ex1_vn, ex2_en, ex2_vn, ex3_en, ex3_vn = format_examples(w.get("examples", []))
        word_family_str = format_word_family(w.get("word_family", "-"))
        synonyms = w.get("synonyms", "N/A")
        antonyms = w.get("antonyms", "N/A")

        audio_file = clean_audio_filename(word)
        words_to_download_additions[audio_file] = word

        note_content = NOTE_TEMPLATE.format(
            word=word,
            pos=pos,
            ipa=ipa,
            audio_file=audio_file,
            level=level,
            topic=topic_name,
            group_name_clean=group_name_clean,
            meaning_en=meaning_en,
            meaning_vn=meaning_vn,
            mnemonic=mnemonic,
            collocations_str=collocations_str,
            ex1_en=ex1_en,
            ex1_vn=ex1_vn,
            ex2_en=ex2_en,
            ex2_vn=ex2_vn,
            ex3_en=ex3_en,
            ex3_vn=ex3_vn,
            word_family_str=word_family_str,
            synonyms=synonyms,
            antonyms=antonyms
        )

        note_path = os.path.join(topic_dir, f"{word}.md")
        with open(note_path, "w", encoding="utf-8") as f:
            f.write(note_content)
        created_notes.append(note_path)

    # Update index file
    update_index_file(topic_name, word_list)

    # Update audio json
    if os.path.exists(JSON_AUDIO_FILE):
        try:
            with open(JSON_AUDIO_FILE, "r", encoding="utf-8") as f:
                audio_dict = json.load(f)
            audio_dict.update(words_to_download_additions)
            with open(JSON_AUDIO_FILE, "w", encoding="utf-8") as f:
                json.dump(audio_dict, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Warning: Failed to update audio json: {e}")

    return {
        "topic": topic_name,
        "count": len(created_notes),
        "created_notes": created_notes
    }
