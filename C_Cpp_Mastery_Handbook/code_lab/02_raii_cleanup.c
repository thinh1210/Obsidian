/**
 * 02_raii_cleanup.c - Kỹ thuật tối mật tạo RAII thuần C bằng __attribute__((cleanup))
 * Chạy: gcc -Wall -Wextra -std=c11 02_raii_cleanup.c -o 02_raii_cleanup && ./02_raii_cleanup
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Hàm tự động free con trỏ khi biến ra khỏi scope
static inline void auto_free(void *p) {
    void **ptr = (void**)p;
    if (*ptr) {
        printf("  [RAII-CLEANUP] Tu dong free bo nho tai dia chi: %p\n", *ptr);
        free(*ptr);
        *ptr = NULL;
    }
}

// Macro khai báo biến có tính năng RAII
#define AUTO_FREE __attribute__((cleanup(auto_free)))

// Hàm tự động đóng File khi ra khỏi scope
static inline void auto_close_file(FILE **f) {
    if (*f) {
        printf("  [RAII-CLEANUP] Tu dong dong file handle: %p\n", (void*)*f);
        fclose(*f);
        *f = NULL;
    }
}
#define AUTO_FILE __attribute__((cleanup(auto_close_file)))

void simulate_business_logic(int trigger_early_exit) {
    printf("--> Bat dau ham simulate_business_logic (trigger_early_exit = %d)\n", trigger_early_exit);

    // 1. Cấp phát động được bảo vệ bởi RAII
    AUTO_FREE char *buffer = (char*)malloc(64);
    if (!buffer) return;
    snprintf(buffer, 64, "Data payload 0xDEADBEEF");
    printf("    Da cap phat buffer (%p): '%s'\n", (void*)buffer, buffer);

    // 2. Mở file được bảo vệ bởi RAII
    AUTO_FILE FILE *fp = fopen("/tmp/test_raii_dummy.txt", "w");
    if (fp) {
        fprintf(fp, "Write test\n");
        printf("    Da mo file /tmp/test_raii_dummy.txt thanh cong.\n");
    }

    if (trigger_early_exit) {
        printf("    [!] Phat hien loi nghiep vu -> RETURN SOM NGAY TAI DAY!\n");
        // Bình thường code C truyền thống nếu return sớm ở đây sẽ làm LEAK CẢ RAM VÀ FILE HANDLE!
        // Nhưng với __attribute__((cleanup)), compiler tự động chèn dọn dẹp trước khi nhảy!
        return;
    }

    printf("    [v] Xu ly thanh cong den cuoi ham.\n");
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 02: PURE C RAII VIA __attribute__((cleanup))\n");
    printf("============================================================\n\n");

    printf("--- TEST 1: Thoat ham som (Early Return) ---\n");
    simulate_business_logic(1);
    printf("<-- Da thoat ra ngoai ham Test 1 an toan khong ro ri!\n\n");

    printf("--- TEST 2: Chay het toan bo ham binh thuong ---\n");
    simulate_business_logic(0);
    printf("<-- Da thoat ra ngoai ham Test 2 an toan khong ro ri!\n");

    return 0;
}
