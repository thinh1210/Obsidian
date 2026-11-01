/**
 * 01_packed_vs_aligned.c - Khảo sát cơ chế Struct Padding & __attribute__((packed))
 * Chạy: gcc -Wall -Wextra -std=c11 01_packed_vs_aligned.c -o 01_packed_vs_aligned && ./01_packed_vs_aligned
 */

#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

// Struct sắp xếp lộn xộn (Bị chèn nhiều padding bytes)
struct SensorBad {
    uint8_t  id;        // 1 byte  - offset 0
    // [Padding 3 bytes để căn chỉnh 4 bytes]
    uint32_t timestamp; // 4 bytes - offset 4
    uint8_t  status;    // 1 byte  - offset 8
    // [Padding 1 byte để căn chỉnh 2 bytes]
    uint16_t value;     // 2 bytes - offset 10
    uint8_t  checksum;  // 1 byte  - offset 12
    // [Tail padding 3 bytes để tổng kích thước chia hết cho 4]
};

// Struct sắp xếp tối ưu (Từ lớn đến nhỏ)
struct SensorGood {
    uint32_t timestamp; // 4 bytes - offset 0
    uint16_t value;     // 2 bytes - offset 4
    uint8_t  id;        // 1 byte  - offset 6
    uint8_t  status;    // 1 byte  - offset 7
    uint8_t  checksum;  // 1 byte  - offset 8
    // [Tail padding 3 bytes để tổng kích thước chia hết cho 4]
};

// Struct ép bỏ toàn bộ padding bằng GCC attribute
struct __attribute__((packed)) SensorPacked {
    uint8_t  id;        // 1 byte  - offset 0
    uint32_t timestamp; // 4 bytes - offset 1 (ĐỊA CHỈ LẺ!)
    uint8_t  status;    // 1 byte  - offset 5
    uint16_t value;     // 2 bytes - offset 6
    uint8_t  checksum;  // 1 byte  - offset 8
};

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 01: STRUCT PADDING & __attribute__((packed))\n");
    printf("============================================================\n\n");

    printf("[1] Kich thuoc struct SensorBad (Sap xep lon xon):\n");
    printf("    - Tong sizeof: %zu bytes (Du lieu that: 9 bytes, Lang phi: %zu bytes)\n",
           sizeof(struct SensorBad), sizeof(struct SensorBad) - 9);
    printf("    - Offset 'id':        %zu\n", offsetof(struct SensorBad, id));
    printf("    - Offset 'timestamp': %zu\n", offsetof(struct SensorBad, timestamp));
    printf("    - Offset 'status':    %zu\n", offsetof(struct SensorBad, status));
    printf("    - Offset 'value':     %zu\n", offsetof(struct SensorBad, value));
    printf("    - Offset 'checksum':  %zu\n\n", offsetof(struct SensorBad, checksum));

    printf("[2] Kich thuoc struct SensorGood (Sap xep toi uu giam dan):\n");
    printf("    - Tong sizeof: %zu bytes (Tiet kiem duoc 4 bytes so voi cach tren!)\n",
           sizeof(struct SensorGood));
    printf("    - Offset 'timestamp': %zu\n", offsetof(struct SensorGood, timestamp));
    printf("    - Offset 'value':     %zu\n", offsetof(struct SensorGood, value));
    printf("    - Offset 'id':        %zu\n", offsetof(struct SensorGood, id));
    printf("    - Offset 'status':    %zu\n", offsetof(struct SensorGood, status));
    printf("    - Offset 'checksum':  %zu\n\n", offsetof(struct SensorGood, checksum));

    printf("[3] Kich thuoc struct SensorPacked (__attribute__((packed))):\n");
    printf("    - Tong sizeof: %zu bytes (Triet tieu 100%% padding! Dung cho truyen thong)\n",
           sizeof(struct SensorPacked));
    printf("    - Offset 'id':        %zu\n", offsetof(struct SensorPacked, id));
    printf("    - Offset 'timestamp': %zu  <-- Chu y: nam o dia chi le!\n",
           offsetof(struct SensorPacked, timestamp));
    printf("    - Offset 'value':     %zu\n", offsetof(struct SensorPacked, value));

    return 0;
}
