/**
 * 06_safe_overflow.c - Bắt lỗi tràn số nguyên an toàn bằng __builtin_add_overflow (SEI CERT C)
 * Chạy: gcc -Wall -Wextra -std=c11 06_safe_overflow.c -o 06_safe_overflow && ./06_safe_overflow
 */

#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <stdbool.h>

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 06: SAFE ARITHMETIC & INTEGER OVERFLOW (SEI CERT C)\n");
    printf("============================================================\n\n");

    // 1. Phép cộng bình thường
    int32_t a = 1000000;
    int32_t b = 2000000;
    int32_t result;

    if (__builtin_add_overflow(a, b, &result)) {
        printf("[1] Loi: Phep cong bi tran so!\n");
    } else {
        printf("[1] Hop le: %d + %d = %d\n\n", a, b, result);
    }

    // 2. Phép cộng gây tràn số nguyên có dấu (Signed Integer Overflow)
    int32_t max_val = INT32_MAX; // 2,147,483,647
    int32_t add_one = 1;

    printf("[2] Thu thuc hien INT32_MAX + 1:\n");
    printf("    Gia tri goc: %d\n", max_val);

    if (__builtin_add_overflow(max_val, add_one, &result)) {
        printf("    --> [CANH BAO AN TOAN]: Phat hien TRAN SO NGUYEN (Overflow Flag = 1)!\n");
        printf("    --> Chuong trinh ngan chan kip thoi, khong bi roi vao Undefined Behavior!\n\n");
    } else {
        printf("    Ket qua: %d (Khong the toi day)\n\n", result);
    }

    // 3. Phép nhân gây tràn số (Multiplication Overflow)
    int32_t mul_a = 1000000;
    int32_t mul_b = 3000;
    if (__builtin_mul_overflow(mul_a, mul_b, &result)) {
        printf("[3] Thu thuc hien %d * %d:\n", mul_a, mul_b);
        printf("    --> [CANH BAO AN TOAN]: Phat hien TRAN SO PHEP NHAN!\n");
    }

    // 4. Cạm bẫy so sánh signed vs unsigned (Integer Promotion)
    int s = -1;
    unsigned int u = 1;
    printf("\n[4] Kiem tra cạm bẫy so sánh Signed vs Unsigned (Integer Promotion):\n");
    printf("    int s = -1;\n");
    printf("    unsigned int u = 1;\n");
    if (s < u) {
        printf("    Ket qua: -1 < 1 la TRUE\n");
    } else {
        printf("    Ket qua: -1 < 1 la FALSE! (Vi -1 bi ngam dinh ep kieu thanh %u)\n", (unsigned int)s);
    }

    return 0;
}
