#!/usr/bin/env python3
"""
Tự động tải 3.294 file phát âm MP3 (chuẩn US) cho toàn bộ từ vựng trong Obsidian Vault.
Nguồn: Youdao Audio API (US Accent) + Fallback Google TTS.
Hỗ trợ tải đa luồng (multi-threaded), tự động tiếp tục (resume) nếu bị ngắt quãng.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

VAULT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(VAULT_DIR, "English", "audio")
JSON_FILE = os.path.join(AUDIO_DIR, "words_to_download.json")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_one_word(item):
    filename, word = item
    dest_path = os.path.join(AUDIO_DIR, filename)
    
    # Bỏ qua nếu đã tải thành công (> 500 bytes)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 500:
        return filename, True, "Already exists"
        
    encoded_word = urllib.parse.quote(word)
    
    # 1. Nguồn chính: Youdao Audio (US Accent: type=2)
    url_primary = f"https://dict.youdao.com/dictvoice?audio={encoded_word}&type=2"
    # 2. Nguồn dự phòng: Google Translate TTS
    url_fallback = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q={encoded_word}"
    
    for url in [url_primary, url_fallback]:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                # Kiểm tra dữ liệu hợp lệ (> 500 bytes và không phải HTML lỗi)
                if len(data) > 500 and not data.startswith(b"<!DOCTYPE") and not data.startswith(b"<html"):
                    with open(dest_path, "wb") as f:
                        f.write(data)
                    return filename, True, "Success"
        except Exception:
            pass
        time.sleep(0.2)
        
    return filename, False, "Failed to download"

def main():
    if not os.path.exists(JSON_FILE):
        print(f"Error: Không tìm thấy file danh sách {JSON_FILE}")
        sys.exit(1)
        
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        words = json.load(f)
        
    total = len(words)
    print("=" * 60)
    print(f"BẮT ĐẦU TẢI PHÁT ÂM AUDIO MP3 ({total} TỪ)")
    print(f"Thư mục lưu trữ: {AUDIO_DIR}")
    print("=" * 60)
    
    items = list(words.items())
    completed = 0
    success_count = 0
    fail_count = 0
    
    start_time = time.time()
    
    # Tải đa luồng (16 luồng song song)
    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = {executor.submit(download_one_word, item): item for item in items}
        
        for future in as_completed(futures):
            completed += 1
            filename, success, msg = future.result()
            if success:
                success_count += 1
            else:
                fail_count += 1
                
            percent = (completed / total) * 100
            bar_len = 30
            filled = int(bar_len * completed // total)
            bar = "=" * filled + "-" * (bar_len - filled)
            
            # In tiến độ
            if sys.stdout.isatty():
                sys.stdout.write(f"\r[{bar}] {completed}/{total} ({percent:.1f}%) | Đã xong: {success_count} | Lỗi: {fail_count}")
                sys.stdout.flush()
            elif completed % 100 == 0 or completed == total:
                print(f"[{completed}/{total}] ({percent:.1f}%) | Đã xong: {success_count} | Lỗi: {fail_count}", flush=True)
            
    elapsed = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"HOÀN THÀNH trong {elapsed:.1f} giây!")
    print(f"Thành công: {success_count} / {total} files.")
    if fail_count > 0:
        print(f"Thất bại: {fail_count} files (có thể chạy lại script để tải bù các file lỗi).")
    print("=" * 60)

if __name__ == "__main__":
    main()
