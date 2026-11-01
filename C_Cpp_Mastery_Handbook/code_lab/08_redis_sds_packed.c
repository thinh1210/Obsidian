/**
 * 08_redis_sds_packed.c - Mô phỏng kỹ thuật chuỗi SDS của Redis (__attribute__((packed)) & s[-1])
 * Chạy: gcc -Wall -Wextra -std=c11 08_redis_sds_packed.c -o 08_redis_sds_packed && ./08_redis_sds_packed
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define SDS_TYPE_8 1

// Header SDS được ép packed tuyệt đối (không có padding)
struct __attribute__((__packed__)) sdshdr8 {
    uint8_t len;         /* Số byte đang sử dụng */
    uint8_t alloc;       /* Tổng số byte được cấp phát */
    unsigned char flags; /* 3 bit thấp là loại SDS, nằm ngay trước buf[] */
    char buf[];          /* Flexible array member */
};

typedef char* sds;

// Hàm tạo chuỗi SDS mới
sds sds_new(const char *init) {
    size_t initlen = (init == NULL) ? 0 : strlen(init);
    // Cấp phát 1 khối nhớ duy nhất cho cả Header + Chuỗi + Ký tự '\0'
    size_t total_size = sizeof(struct sdshdr8) + initlen + 1;
    struct sdshdr8 *sh = (struct sdshdr8*)malloc(total_size);
    if (!sh) return NULL;

    sh->len = (uint8_t)initlen;
    sh->alloc = (uint8_t)initlen;
    sh->flags = SDS_TYPE_8;

    if (initlen && init) {
        memcpy(sh->buf, init, initlen);
    }
    sh->buf[initlen] = '\0';

    // TRẢ VỀ CON TRỎ TRỎ THẲNG VÀO buf[]!
    return (char*)sh->buf;
}

// Lấy độ dài O(1) bằng cách lùi con trỏ s[-1]
static inline size_t sds_len(const sds s) {
    unsigned char flags = s[-1]; // Đọc ngược 1 byte để lấy cờ!
    if ((flags & 7) == SDS_TYPE_8) {
        // Tìm ngược địa chỉ của Struct Header
        struct sdshdr8 *sh = (struct sdshdr8*)((char*)s - sizeof(struct sdshdr8));
        return sh->len;
    }
    return 0;
}

// Giải phóng bộ nhớ SDS
void sds_free(sds s) {
    if (!s) return;
    struct sdshdr8 *sh = (struct sdshdr8*)((char*)s - sizeof(struct sdshdr8));
    free(sh);
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 08: REDIS SDS STRING (__attribute__((packed)) & s[-1])\n");
    printf("============================================================\n\n");

    sds my_str = sds_new("Hello Redis Architecture!");
    if (!my_str) return 1;

    printf("[1] Tuong thich 100%% voi cac ham C tieu chuan:\n");
    printf("    In bang printf(\"%%s\"): '%s'\n", my_str);
    printf("    Do dai theo strlen():    %zu bytes\n", strlen(my_str));

    printf("\n[2] Tinh toan do dai O(1) bang ky thuat lui con tro s[-1]:\n");
    printf("    Do dai lay qua sds_len(s): %zu bytes (Khong can duyet '\\0'!)\n", sds_len(my_str));
    printf("    Gia tri flags tai s[-1]:   0x%02X (Type = SDS_TYPE_8)\n", (unsigned char)my_str[-1]);

    printf("\n[3] Vi tri bo nho:\n");
    printf("    Dia chi con trỏ my_str (buf[0]): %p\n", (void*)my_str);
    printf("    Dia chi struct Header sdshdr8:   %p (Lui lai dung %zu bytes)\n",
           (void*)(my_str - sizeof(struct sdshdr8)), sizeof(struct sdshdr8));

    sds_free(my_str);
    printf("\n[v] Da giai phong bo nho SDS thanh cong.\n");

    return 0;
}
