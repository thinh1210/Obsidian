/**
 * 03_branch_predict.c - Kiểm chứng __builtin_expect (likely/unlikely) & Bitwise Intrinsics
 * Chạy: gcc -O2 -Wall -Wextra -std=c11 03_branch_predict.c -o 03_branch_predict && ./03_branch_predict
 */

#include <stdio.h>
#include <stdint.h>

#define likely(x)       __builtin_expect(!!(x), 1)
#define unlikely(x)     __builtin_expect(!!(x), 0)

int process_data(int *data, size_t len) {
    // Nhánh kiểm tra con trỏ NULL là cực kỳ hiếm khi xảy ra
    if (unlikely(data == NULL || len == 0)) {
        return -1;
    }
    return (int)len * 2;
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 03: COMPILER INTRINSICS & BIT MANIPULATION\n");
    printf("============================================================\n\n");

    int dummy = 42;
    printf("[1] Kiem tra likely/unlikely logic:\n");
    printf("    process_data(&dummy, 1):  %d\n", process_data(&dummy, 1));
    printf("    process_data(NULL, 0):    %d\n\n", process_data(NULL, 0));

    uint32_t val = 0x000F0000;
    printf("[2] Kiem tra Bit Manipulation Intrinsics voi gia tri 0x%08X:\n", val);
    
    // __builtin_clz: Đếm số 0 ở đầu (32 - vị trí bit cao nhất)
    int clz = __builtin_clz(val);
    printf("    - __builtin_clz (Count Leading Zeros):  %d\n", clz);
    printf("      => Log2(val) xap xi = 31 - %d = %d (2^19 = 0x00080000)\n", clz, 31 - clz);

    // __builtin_ctz: Đếm số 0 ở cuối
    int ctz = __builtin_ctz(val);
    printf("    - __builtin_ctz (Count Trailing Zeros): %d\n", ctz);

    // __builtin_popcount: Đếm tổng số bit 1
    int pop = __builtin_popcount(val);
    printf("    - __builtin_popcount (Hamming Weight):  %d (Trong 0xF co 4 bit 1)\n", pop);

    // __builtin_bswap32: Đảo Endianness
    uint32_t be_val = 0x12345678;
    uint32_t swapped = __builtin_bswap32(be_val);
    printf("    - __builtin_bswap32: Goc = 0x%08X  -->  Dao = 0x%08X\n", be_val, swapped);

    return 0;
}
