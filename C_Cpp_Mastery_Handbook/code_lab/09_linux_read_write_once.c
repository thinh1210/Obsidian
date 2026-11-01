/**
 * 09_linux_read_write_once.c - Mô phỏng cơ chế READ_ONCE() và WRITE_ONCE() của Linux Kernel
 * Chạy: gcc -O2 -Wall -Wextra -std=c11 09_linux_read_write_once.c -o 09_linux_read_write_once && ./09_linux_read_write_once
 */

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// Macro chuẩn Linux Kernel (Dùng __typeof__ cho tương thích GCC/Clang)
#define READ_ONCE(x) (*(const volatile __typeof__(x) *)&(x))
#define WRITE_ONCE(x, val) do { *(volatile __typeof__(x) *)&(x) = (val); } while (0)

// Biến toàn cục chia sẻ (KHÔNG cần khai báo volatile vĩnh viễn)
int g_worker_status = 0;
int g_data_payload = 0;

void producer_task(void) {
    printf("--> Producer: Dang chuan bi du lieu...\n");
    g_data_payload = 1337;
    // Ghi an toàn bằng WRITE_ONCE để ngăn compiler hoãn lệnh hoặc store tearing
    WRITE_ONCE(g_worker_status, 1);
    printf("--> Producer: Da bat g_worker_status = 1 bang WRITE_ONCE.\n");
}

void consumer_task(void) {
    printf("<-- Consumer: Dang doi tin hieu status tu Producer...\n");
    int status;
    int spin_count = 0;

    // Vòng lặp chờ cờ với READ_ONCE
    // Nếu không có READ_ONCE và không có volatile, với cờ -O2 compiler có thể
    // nhấc việc đọc g_worker_status ra ngoài vòng lặp (Loop Invariant Hoisting) gây treo vô tận!
    while ((status = READ_ONCE(g_worker_status)) == 0) {
        spin_count++;
        if (spin_count == 3) {
            // Giả lập sau 3 lần kiểm tra thì Producer gửi xong
            producer_task();
        }
    }

    printf("<-- Consumer: Nhan duoc status = %d sau %d lan kiem tra.\n", status, spin_count);
    printf("<-- Consumer: Du lieu nhan duoc: %d (Ky vong: 1337)\n", g_data_payload);
}

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 09: LINUX KERNEL READ_ONCE() & WRITE_ONCE()\n");
    printf("============================================================\n\n");

    consumer_task();

    return 0;
}
