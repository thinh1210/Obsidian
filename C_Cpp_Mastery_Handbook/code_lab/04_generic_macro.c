/**
 * 04_generic_macro.c - Hiện thực hóa Function Overloading tĩnh trong C11 bằng _Generic
 * Chạy: gcc -Wall -Wextra -std=c11 04_generic_macro.c -o 04_generic_macro && ./04_generic_macro
 */

#include <stdio.h>
#include <stdint.h>

void print_int(int x)            { printf("  [Dispatch Int]       Gia tri = %d\n", x); }
void print_double(double x)      { printf("  [Dispatch Double]    Gia tri = %lf\n", x); }
void print_string(const char *x) { printf("  [Dispatch String]    Gia tri = \"%s\"\n", x); }
void print_uint64(uint64_t x)    { printf("  [Dispatch Uint64]    Gia tri = %lu (ULL)\n", x); }

// Macro thông minh tự động ánh xạ hàm theo kiểu dữ liệu lúc compile-time
#define smart_print(X) _Generic((X), \
    int:           print_int, \
    double:        print_double, \
    float:         print_double, \
    char*:         print_string, \
    const char*:   print_string, \
    uint64_t:      print_uint64, \
    default:       print_int \
)(X)

// Macro tính giá trị tuyệt đối đa kiểu (Generic Abs)
#define generic_abs(X) _Generic((X), \
    int: (X) < 0 ? -(X) : (X), \
    double: (X) < 0.0 ? -(X) : (X), \
    float: (X) < 0.0f ? -(X) : (X) \
)

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 04: C11 _Generic SELECTION (PURE C OVERLOADING)\n");
    printf("============================================================\n\n");

    int i = 100;
    double d = 3.14159;
    const char *str = "Hello Embedded C11";
    uint64_t big = 0xFFFFFFFF12345678ULL;

    printf("Goi smart_print() voi cac kieu du lieu khac nhau:\n");
    smart_print(i);
    smart_print(d);
    smart_print(str);
    smart_print(big);

    printf("\nKiem tra generic_abs():\n");
    printf("    abs(-42):   %d\n", generic_abs(-42));
    printf("    abs(-9.81): %lf\n", generic_abs(-9.81));

    return 0;
}
