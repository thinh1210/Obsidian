/**
 * 10_systemd_raii_autoptr.c - Mô phỏng hệ thống macro _cleanup_ và Chuyển giao quyền sở hữu (Ownership Transfer) của systemd
 * Chạy: gcc -Wall -Wextra -std=c11 10_systemd_raii_autoptr.c -o 10_systemd_raii_autoptr && ./10_systemd_raii_autoptr
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Định nghĩa hệ thống _cleanup_ tương tự systemd
#define _cleanup_(f) __attribute__((cleanup(f)))

static inline void freep(void *p) {
    void **ptr = (void**)p;
    if (*ptr) {
        printf("    [systemd-cleanup] freep: Tu dong giai phong bo nho tai %p\n", *ptr);
        free(*ptr);
        *ptr = NULL;
    }
}

#define _cleanup_free_ _cleanup_(freep)

// Hàm mô phỏng tải tài nguyên có nhiều nhánh lỗi và chuyển giao quyền sở hữu
int parse_config_file(const char *filename, char **out_result) {
    printf("--> parse_config_file: Dang xu ly file '%s'\n", filename);

    // temp_buf tự động được giải phóng nếu hàm gặp lỗi thoát sớm
    _cleanup_free_ char *temp_buf = (char*)malloc(128);
    if (!temp_buf) return -1;
    snprintf(temp_buf, 128, "CONFIG_PARAM=ENABLED_FOR_%s", filename);

    if (strcmp(filename, "invalid.conf") == 0) {
        printf("    [!] Phat hien file khong hop le -> Return loi som!\n");
        // Khi return tại đây, temp_buf TỰ ĐỘNG ĐƯỢC GIẢI PHÓNG, không bao giờ leak!
        return -2;
    }

    printf("    [v] Parse thanh cong! Chuan bi ban giao du lieu cho caller.\n");

    // KỸ THUẬT SYSTEMD OWNERSHIP TRANSFER (Tuong duong std::move()):
    // Gán con trỏ cho biến đầu ra, và đặt con trỏ temp_buf = NULL
    // để khi thoát hàm, freep(&temp_buf) khong free vung nho nay!
    *out_result = temp_buf;
    temp_buf = NULL; // TƯỚC QUYỀN SỞ HỮU!

    return 0; // Caller bay gio so huu vung nho nay!
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 10: SYSTEMD _cleanup_ MACRO & OWNERSHIP TRANSFER\n");
    printf("============================================================\n\n");

    printf("--- TEST 1: Goi voi file loi 'invalid.conf' ---\n");
    char *result1 = NULL;
    int ret1 = parse_config_file("invalid.conf", &result1);
    printf("    Ket qua tra ve: %d (result1 = %p)\n\n", ret1, (void*)result1);

    printf("--- TEST 2: Goi voi file hop le 'app.conf' ---\n");
    // Caller cung dung _cleanup_free_ de quan ly vung nho nhan duoc!
    _cleanup_free_ char *result2 = NULL;
    int ret2 = parse_config_file("app.conf", &result2);
    printf("    Ket qua tra ve: %d\n", ret2);
    if (ret2 == 0) {
        printf("    Du lieu nhan duoc: '%s'\n", result2);
    }
    printf("<-- Thoat khoi main: result2 se tu dong duoc giai phong boi caller!\n");

    return 0;
}
