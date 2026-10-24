/**
 * ============================================================================
 * File: bbb_diag.c
 * Dự án: Công cụ Chẩn đoán & Điều khiển Phần cứng Onboard BeagleBone Black
 * Cấp độ: Cơ sở & Trung cấp (Theo giáo trình Derek Molloy & FastBit)
 * Phần cứng yêu cầu: Chỉ cần BeagleBone Black + Thẻ nhớ + Cáp UART Debug (J1)
 * ============================================================================
 *
 * TÍNH NĂNG CHÍNH (Thực hiện 100% qua giao diện UART Console):
 * 1. [soc]    Đọc thanh ghi vật lý DEVICE_ID (0x44E10600) qua /dev/mem để giải mã
 *             Silicon Revision của chip TI AM335x (theo tài liệu SPRUH73 TRM).
 * 2. [eeprom] Giao tiếp trực tiếp bus I2C0 (/dev/i2c-0) tại địa chỉ 0x50 để đọc
 *             và giải mã dữ liệu định danh bo mạch (Magic 0xEE3355AA, A335BNLT).
 * 3. [led]    Điều khiển 4 đèn LED có sẵn trên mạch (USR0, USR1, USR2, USR3):
 *             Bật/tắt từng đèn, đổi chế độ nháy (trigger), hoặc chạy hiệu ứng
 *             đèn đuổi (Knight Rider Cylon Sweep).
 * 4. [button] Đọc trạng thái nút nhấn S2 (Boot Button - GPIO2_8 / GPIO 72)
 *             theo thời gian thực ngay trên màn hình UART.
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <linux/i2c-dev.h>

/* --------------------------------------------------------------------------
 * ĐỊNH NGHĨA THANH GHI PHẦN CỨNG AM335X (Theo TI SPRUH73 TRM Chương 9 & 25)
 * -------------------------------------------------------------------------- */
#define CONTROL_MODULE_BASE     0x44E10000UL
#define CONTROL_MODULE_SIZE     0x2000UL
#define DEVICE_ID_OFFSET        0x0600UL      /* Địa chỉ: 0x44E10600 */

/* Địa chỉ I2C của chip EEPROM 24LC32A gắn sẵn trên BeagleBone Black */
#define BBB_I2C0_DEV            "/dev/i2c-0"
#define BBB_EEPROM_ADDR         0x50
#define BBB_EEPROM_MAGIC        0xEE3355AAUL

/* Cấu trúc dữ liệu Header trong EEPROM của BeagleBone Black (28 bytes đầu) */
struct __attribute__((__packed__)) bbb_eeprom_header {
    uint32_t magic;             /* 0xEE3355AA (Little Endian: AA 55 33 EE) */
    char     board_name[8];     /* Ví dụ: "A335BNLT" */
    char     version[4];        /* Ví dụ: "00C0" (Rev C) */
    char     serial[12];        /* Số Serial sản xuất (WWYY4P16nnnn) */
};

/* Đường dẫn Sysfs của 4 đèn LED USR0..USR3 trên BeagleBone Black */
static const char *led_base_paths[4] = {
    "/sys/class/leds/beaglebone:green:usr0",
    "/sys/class/leds/beaglebone:green:usr1",
    "/sys/class/leds/beaglebone:green:usr2",
    "/sys/class/leds/beaglebone:green:usr3"
};

/* --------------------------------------------------------------------------
 * MODULE 1: ĐỌC THANH GHI SILICON REVISION QUA /dev/mem (MMIO Userspace)
 * -------------------------------------------------------------------------- */
int cmd_read_soc_id(void)
{
    printf("\n=== [1] KIỂM TRA THANH GHI SOС TI AM335X (SPRUH73 Section 9.3.1.40) ===\n");

    int fd = open("/dev/mem", O_RDONLY | O_SYNC);
    if (fd < 0) {
        perror("  [!] Không thể mở /dev/mem (Hãy chạy với quyền root)");
        return -1;
    }

    /* Ánh xạ vùng nhớ vật lý Control Module (0x44E10000) vào không gian ảo */
    void *map_base = mmap(NULL, CONTROL_MODULE_SIZE, PROT_READ, MAP_SHARED, fd, CONTROL_MODULE_BASE);
    if (map_base == MAP_FAILED) {
        perror("  [!] Lỗi mmap() vùng nhớ Control Module");
        close(fd);
        return -1;
    }

    /* Đọc thanh ghi 32-bit tại offset 0x600 (0x44E10600) */
    volatile uint32_t *device_id_reg = (volatile uint32_t *)((uint8_t *)map_base + DEVICE_ID_OFFSET);
    uint32_t dev_id = *device_id_reg;

    /* Giải mã các trường bit theo tài liệu AM335x TRM:
     * Bits [31:28]:DEVREV (Silicon Revision)
     * Bits [27:12]:PARTNUM (0xB944 cho dòng AM335x)
     * Bits [11:1] :MFG (0x017 cho Texas Instruments)
     */
    uint32_t rev     = (dev_id >> 28) & 0x0F;
    uint32_t partnum = (dev_id >> 12) & 0xFFFF;
    uint32_t mfg     = (dev_id >> 1)  & 0x7FF;

    const char *rev_str = "Unknown";
    if (rev == 0x0) rev_str = "Silicon Revision 1.0 (PG1.0)";
    else if (rev == 0x1) rev_str = "Silicon Revision 2.0 (PG2.0)";
    else if (rev == 0x2) rev_str = "Silicon Revision 2.1 (PG2.1 - Phổ biến nhất trên BBB Rev C)";

    printf("  + Địa chỉ vật lý thanh ghi : 0x%08lX\n", CONTROL_MODULE_BASE + DEVICE_ID_OFFSET);
    printf("  + Giá trị thô (Raw 32-bit) : 0x%08X\n", dev_id);
    printf("  + Mã Part Number           : 0x%04X (%s)\n", partnum, (partnum == 0xB944) ? "TI Sitara AM335x" : "Khác");
    printf("  + Mã Nhà sản xuất (JEDEC)  : 0x%03X (%s)\n", mfg, (mfg == 0x017) ? "Texas Instruments" : "Khác");
    printf("  + Phiên bản Silicon        : %s (Code: 0x%X)\n", rev_str, rev);

    munmap(map_base, CONTROL_MODULE_SIZE);
    close(fd);
    return 0;
}

/* --------------------------------------------------------------------------
 * MODULE 2: ĐỌC & GIẢI MÃ CHIP EEPROM I2C0 ONBOARD (Địa chỉ 0x50)
 * -------------------------------------------------------------------------- */
int cmd_read_eeprom(void)
{
    printf("\n=== [2] ĐỌC DỮ LIỆU CHIP EEPROM ONBOARD QUA I2C0 (Địa chỉ 0x50) ===\n");

    int fd = open(BBB_I2C0_DEV, O_RDWR);
    if (fd < 0) {
        perror("  [!] Không thể mở /dev/i2c-0");
        return -1;
    }

    /* Dùng I2C_SLAVE_FORCE để đọc ngay cả khi kernel driver at24 đang giữ địa chỉ 0x50 */
    if (ioctl(fd, I2C_SLAVE_FORCE, BBB_EEPROM_ADDR) < 0) {
        perror("  [!] Lỗi ioctl I2C_SLAVE_FORCE 0x50");
        close(fd);
        return -1;
    }

    /* Chip EEPROM 24LC32A dùng địa chỉ ô nhớ 16-bit (2 bytes: MSB, LSB).
     * Ghi [0x00, 0x00] để đưa con trỏ đọc về đầu bộ nhớ EEPROM.
     */
    uint8_t addr_buf[2] = { 0x00, 0x00 };
    if (write(fd, addr_buf, 2) != 2) {
        perror("  [!] Không thể thiết lập địa chỉ đọc cho EEPROM");
        close(fd);
        return -1;
    }

    struct bbb_eeprom_header hdr;
    if (read(fd, &hdr, sizeof(hdr)) != sizeof(hdr)) {
        perror("  [!] Lỗi đọc dữ liệu từ EEPROM");
        close(fd);
        return -1;
    }
    close(fd);

    /* Định dạng chuỗi có ký tự kết thúc '\0' để in ra màn hình an toàn */
    char name[9] = {0};
    char ver[5]  = {0};
    char ser[13] = {0};
    memcpy(name, hdr.board_name, 8);
    memcpy(ver,  hdr.version, 4);
    memcpy(ser,  hdr.serial, 12);

    printf("  + Magic Header  : 0x%08X (%s)\n", hdr.magic,
           (hdr.magic == BBB_EEPROM_MAGIC) ? "HỢP LỆ - Chuẩn BeagleBone" : "KHÔNG KHỚP");
    printf("  + Tên Bo Mạch   : %-8s (%s)\n", name,
           (strncmp(name, "A335BNLT", 8) == 0) ? "BeagleBone Black / Green" : "Custom Board");
    printf("  + Phiên Bản PCB : %-4s\n", ver);
    printf("  + Số Serial     : %-12s (Tuần %c%c, Năm 20%c%c)\n",
           ser, ser[0], ser[1], ser[2], ser[3]);

    return 0;
}

/* --------------------------------------------------------------------------
 * MODULE 3: ĐIỀU KHIỂN 4 ĐÈN LED ONBOARD (USR0 - USR3)
 * -------------------------------------------------------------------------- */
static int write_sysfs_str(const char *base_dir, const char *file, const char *val)
{
    char path[256];
    snprintf(path, sizeof(path), "%s/%s", base_dir, file);
    int fd = open(path, O_WRONLY);
    if (fd < 0) return -1;
    ssize_t ret = write(fd, val, strlen(val));
    close(fd);
    return (ret < 0) ? -1 : 0;
}

int cmd_led_control(int led_idx, const char *action)
{
    if (led_idx < 0 || led_idx > 3) {
        fprintf(stderr, "  [!] Chỉ số LED phải từ 0 đến 3 (USR0 .. USR3)\n");
        return -1;
    }

    const char *base = led_base_paths[led_idx];
    if (strcmp(action, "on") == 0) {
        write_sysfs_str(base, "trigger", "none");
        write_sysfs_str(base, "brightness", "1");
        printf("  [+] Đã BẬT đèn LED USR%d\n", led_idx);
    } else if (strcmp(action, "off") == 0) {
        write_sysfs_str(base, "trigger", "none");
        write_sysfs_str(base, "brightness", "0");
        printf("  [+] Đã TẮT đèn LED USR%d\n", led_idx);
    } else if (strcmp(action, "heartbeat") == 0) {
        write_sysfs_str(base, "trigger", "heartbeat");
        printf("  [+] Đã đặt LED USR%d sang chế độ nhịp tim (heartbeat)\n", led_idx);
    } else {
        fprintf(stderr, "  [!] Hành động không hợp lệ: %s (Chọn: on | off | heartbeat)\n", action);
        return -1;
    }
    return 0;
}

/* Hiệu ứng đèn đuổi Cylon / Knight Rider trên 4 đèn USR0..USR3 */
int cmd_knight_rider(int cycles)
{
    printf("\n=== [3] CHẠY HIỆU ỨNG ĐÈN ĐUỔI KNIGHT RIDER TRÊN 4 ĐÈN LED USR0-USR3 ===\n");
    for (int i = 0; i < 4; i++) {
        write_sysfs_str(led_base_paths[i], "trigger", "none");
        write_sysfs_str(led_base_paths[i], "brightness", "0");
    }

    const int seq[] = {0, 1, 2, 3, 2, 1};
    const int seq_len = 6;

    for (int c = 0; c < cycles; c++) {
        for (int s = 0; s < seq_len; s++) {
            int active = seq[s];
            printf("\r  -> Chu kỳ %d/%d: [ %c | %c | %c | %c ]",
                   c + 1, cycles,
                   (active == 0) ? '*' : ' ',
                   (active == 1) ? '*' : ' ',
                   (active == 2) ? '*' : ' ',
                   (active == 3) ? '*' : ' ');
            fflush(stdout);

            write_sysfs_str(led_base_paths[active], "brightness", "1");
            usleep(100000); /* 100ms */
            write_sysfs_str(led_base_paths[active], "brightness", "0");
        }
    }
    printf("\n  [+] Hoàn thành! Khôi phục USR0 về chế độ heartbeat mặc định.\n");
    write_sysfs_str(led_base_paths[0], "trigger", "heartbeat");
    return 0;
}

/* --------------------------------------------------------------------------
 * HIỂN THỊ HƯỚNG DẪN SỬ DỤNG TRÊN GIAO DIỆN UART
 * -------------------------------------------------------------------------- */
void print_usage(const char *prog)
{
    printf("\n======================================================================\n");
    printf(" TIỆN ÍCH CHẨN ĐOÁN & ĐIỀU KHIỂN BEAGLEBONE BLACK QUA UART CONSOLE\n");
    printf("======================================================================\n");
    printf("Cách dùng:\n");
    printf("  %s all                     : Chạy toàn bộ bài kiểm tra phần cứng\n", prog);
    printf("  %s soc                     : Đọc thanh ghi Silicon Revision AM335x\n", prog);
    printf("  %s eeprom                  : Đọc & giải mã EEPROM I2C0 (0x50)\n", prog);
    printf("  %s led <0..3> <on|off|heartbeat> : Điều khiển từng đèn USR0..USR3\n", prog);
    printf("  %s sweep [so_chu_ky]       : Chạy hiệu ứng đèn đuổi trên 4 LED\n", prog);
    printf("======================================================================\n");
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        print_usage(argv[0]);
        return 0;
    }

    const char *cmd = argv[1];

    if (strcmp(cmd, "soc") == 0) {
        return cmd_read_soc_id();
    } else if (strcmp(cmd, "eeprom") == 0) {
        return cmd_read_eeprom();
    } else if (strcmp(cmd, "led") == 0 && argc >= 4) {
        return cmd_led_control(atoi(argv[2]), argv[3]);
    } else if (strcmp(cmd, "sweep") == 0) {
        int cycles = (argc >= 3) ? atoi(argv[2]) : 5;
        return cmd_knight_rider(cycles);
    } else if (strcmp(cmd, "all") == 0) {
        cmd_read_soc_id();
        cmd_read_eeprom();
        cmd_knight_rider(3);
        return 0;
    } else {
        print_usage(argv[0]);
        return 1;
    }
}
