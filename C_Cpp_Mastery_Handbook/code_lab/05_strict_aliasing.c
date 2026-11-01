/**
 * 05_strict_aliasing.c - Khảo sát Strict Aliasing Rule & Type Punning An Toàn
 * Chạy: gcc -Wall -Wextra -std=c11 05_strict_aliasing.c -o 05_strict_aliasing && ./05_strict_aliasing
 */

#include <stdio.h>
#include <stdint.h>
#include <string.h>

// Cách 1: Type Punning an toàn tuyệt đối bằng Union (C99/C11 defined)
union FloatPun {
    float f;
    uint32_t u;
};

// Cách 2: Type Punning an toàn bằng memcpy (Chuẩn hóa cho cả C và C++)
static inline uint32_t pun_via_memcpy(float f) {
    uint32_t u;
    memcpy(&u, &f, sizeof(u)); // Compiler tối ưu thành 1 lệnh MOV, 0 chi phí!
    return u;
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 05: STRICT ALIASING & SAFE TYPE PUNNING\n");
    printf("============================================================\n\n");

    float test_val = 3.14159265f;

    // 1. Dùng Union
    union FloatPun pun;
    pun.f = test_val;
    printf("[1] Type Punning qua Union:\n");
    printf("    float: %f  -->  Hex bits: 0x%08X\n\n", pun.f, pun.u);

    // 2. Dùng memcpy
    uint32_t bits = pun_via_memcpy(test_val);
    printf("[2] Type Punning qua memcpy (Khuyen nghi cho C++ & C):\n");
    printf("    float: %f  -->  Hex bits: 0x%08X\n\n", test_val, bits);

    // 3. Minh họa cạm bẫy ép kiểu con trỏ thô (Raw Pointer Cast)
    // CẢNH BÁO: Viết như dưới đây là VI PHẠM STRICT ALIASING RULE!
    // gcc với cờ -Wstrict-aliasing=2 sẽ ném ra Warning!
    uint32_t bad_cast = *(uint32_t*)&test_val;
    printf("[3] Ep kieu con tro tho *(uint32_t*)&val (NGUY HIEM, VI PHAM STRICT ALIASING):\n");
    printf("    bits: 0x%08X (Co the bi sai khi bat cờ -O2)\n", bad_cast);

    return 0;
}
