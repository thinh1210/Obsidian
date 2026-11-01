/**
 * 07_linux_kernel_list.c - Mô phỏng cấu trúc Intrusive Linked List của Linux Kernel
 * Chạy: gcc -Wall -Wextra -std=c11 07_linux_kernel_list.c -o 07_linux_kernel_list && ./07_linux_kernel_list
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

// 1. Cấu trúc list_head kinh điển của Linux Kernel
struct list_head {
    struct list_head *next, *prev;
};

// Khởi tạo đầu danh sách
#define LIST_HEAD_INIT(name) { &(name), &(name) }
#define LIST_HEAD(name) struct list_head name = LIST_HEAD_INIT(name)

static inline void INIT_LIST_HEAD(struct list_head *list) {
    list->next = list;
    list->prev = list;
}

// Chèn node mới vào giữa hai node đã biết
static inline void __list_add(struct list_head *new_node,
                              struct list_head *prev,
                              struct list_head *next) {
    next->prev = new_node;
    new_node->next = next;
    new_node->prev = prev;
    prev->next = new_node;
}

// Chèn vào cuối danh sách (list_add_tail)
static inline void list_add_tail(struct list_head *new_node, struct list_head *head) {
    __list_add(new_node, head->prev, head);
}

// Xóa node khỏi danh sách
static inline void list_del(struct list_head *entry) {
    entry->next->prev = entry->prev;
    entry->prev->next = entry->next;
    entry->next = NULL;
    entry->prev = NULL;
}

// 2. Macro container_of thần thánh của Linux (Dùng __typeof__ chuẩn GCC extension)
#define container_of(ptr, type, member) ({                      \
    const __typeof__( ((type *)0)->member ) *__mptr = (ptr);    \
    (type *)( (char *)__mptr - offsetof(type, member) );})

#define list_entry(ptr, type, member) \
    container_of(ptr, type, member)

#define list_for_each_entry(pos, head, member) \
    for (pos = list_entry((head)->next, struct sensor_device, member); \
         &pos->member != (head); \
         pos = list_entry(pos->member.next, struct sensor_device, member))

// 3. Định nghĩa đối tượng nghiệp vụ (Ví dụ: Thiết bị cảm biến trong Kernel)
struct sensor_device {
    int id;
    char name[32];
    float last_reading;
    struct list_head list_node; // Nhúng trực tiếp list_head vào đây!
};

int main(void) {
    printf("============================================================\n");
    printf("   DEMO 07: LINUX KERNEL INTRUSIVE LINKED LIST & container_of\n");
    printf("============================================================\n\n");

    // Khởi tạo đầu danh sách toàn cục
    LIST_HEAD(g_sensor_list);

    // Tạo các thiết bị cảm biến (cấp phát hoặc tĩnh)
    struct sensor_device dev1 = { .id = 101, .name = "Temperature_BME280", .last_reading = 28.5f };
    struct sensor_device dev2 = { .id = 102, .name = "Pressure_BMP180",    .last_reading = 1013.25f };
    struct sensor_device dev3 = { .id = 103, .name = "Humidity_SHT30",      .last_reading = 65.0f };

    // Thêm các thiết bị vào danh sách liên kết
    list_add_tail(&dev1.list_node, &g_sensor_list);
    list_add_tail(&dev2.list_node, &g_sensor_list);
    list_add_tail(&dev3.list_node, &g_sensor_list);

    printf("[1] Duyet danh sach bang list_for_each_entry():\n");
    struct sensor_device *entry;
    list_for_each_entry(entry, &g_sensor_list, list_node) {
        printf("    -> Sensor [ID: %d] '%s': %.2f (Address: %p, Node Offset: %zu)\n",
               entry->id, entry->name, entry->last_reading,
               (void*)entry, offsetof(struct sensor_device, list_node));
    }

    // Xóa thiết bị thứ 2
    printf("\n[2] Xoa thiet bi dev2 (Pressure_BMP180) khoi danh sach...\n");
    list_del(&dev2.list_node);

    printf("[3] Duyet lai danh sach sau khi xoa:\n");
    list_for_each_entry(entry, &g_sensor_list, list_node) {
        printf("    -> Sensor [ID: %d] '%s': %.2f\n", entry->id, entry->name, entry->last_reading);
    }

    return 0;
}
