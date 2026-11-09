#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

/**
 * ============================================================================
 * Dự Án Mẫu: Remote Debugging C Application trên BeagleBone Black qua VS Code
 * Tác giả: Nhúng Linux & Yocto BBB Project
 * Mục đích: Minh họa trực quan các tính năng gỡ lỗi của VS Code:
 *   - Breakpoints (Chấm đỏ dừng thực thi)
 *   - Step Over (F10), Step Into (F11), Step Out (Shift+F11)
 *   - Local & Global Variables Inspection
 *   - Watch Expressions (Theo dõi biến & biểu thức)
 *   - Call Stack (Cây phân cấp gọi hàm)
 *   - Memory Inspection & Pointers
 * ============================================================================
 */

#define LED_USR3_PATH "/sys/class/leds/beaglebone:green:usr3/brightness"

/* Cấu trúc dữ liệu cảm biến đo lường giả lập */
typedef struct {
    int sensor_id;
    char name[32];
    float temperature;
    float voltage;
    unsigned int status_flags;
} SensorData_t;

/* Biến toàn cục để theo dõi trong VS Code Watch Window */
int g_cycle_counter = 0;
SensorData_t g_system_sensor = {
    .sensor_id = 101,
    .name = "TI_AM3358_Internal_ADC",
    .temperature = 36.5f,
    .voltage = 3.30f,
    .status_flags = 0x0001
};

/* Hàm bật/tắt LED USR3 trên bo BeagleBone Black */
static int control_bbb_led(int state) {
    int fd = open(LED_USR3_PATH, O_WRONLY);
    if (fd < 0) {
        /* Nếu chạy mô phỏng không có LED thật, ghi nhận thông báo */
        return -1;
    }
    const char *val = state ? "1" : "0";
    write(fd, val, 1);
    close(fd);
    return 0;
}

/* Hàm tính toán giải thuật - Dùng để test Step Into (F11) & Call Stack */
static float calculate_adjusted_temperature(float raw_temp, float offset, int cycle) {
    float result = raw_temp + (offset * (cycle % 3));
    if (result > 60.0f) {
        printf("[WARN] Nhiệt độ vượt ngưỡng cảnh báo: %.2f *C\n", result);
    }
    return result;
}

/* Hàm cấp phát và xử lý mảng động - Test Memory View và Pointers */
static void process_sensor_buffer(int sample_count) {
    printf("[INFO] Bắt đầu cấp phát bộ nhớ cho %d mẫu dữ liệu...\n", sample_count);
    
    float *samples = (float *)malloc(sample_count * sizeof(float));
    if (!samples) {
        perror("malloc failed");
        return;
    }

    for (int i = 0; i < sample_count; i++) {
        samples[i] = 25.0f + ((float)(i * 7) / 10.0f);
        /* Điểm dừng lý tưởng để kiểm tra giá trị mảng trong Debugger */
    }

    float sum = 0.0f;
    for (int i = 0; i < sample_count; i++) {
        sum += samples[i];
    }
    printf("[INFO] Nhiệt độ trung bình tính được: %.2f *C\n", sum / sample_count);

    /* Giải phóng bộ nhớ */
    free(samples);
}

int main(int argc, char **argv) {
    printf("=====================================================\n");
    printf("  BeagleBone Black Remote Debugging Demo (VS Code)   \n");
    printf("  Target Architecture: ARMv7-A (Cortex-A8)           \n");
    printf("  PID: %d | Host Connected Successfully!            \n", getpid());
    printf("=====================================================\n\n");

    /* Dòng này rất phù hợp để đặt Breakpoint đầu tiên sau khi attach */
    int loop_limit = 5;
    if (argc > 1) {
        loop_limit = atoi(argv[1]);
        if (loop_limit <= 0) loop_limit = 5;
    }

    printf("[INFO] Bắt đầu vòng lặp giám sát thiết bị (%d chu kỳ)...\n", loop_limit);

    for (int i = 1; i <= loop_limit; i++) {
        g_cycle_counter = i;
        g_system_sensor.temperature = calculate_adjusted_temperature(36.5f, 1.25f, i);
        g_system_sensor.voltage = 3.30f - (float)(i * 0.02f);

        printf("--> Chu kỳ #%d: Temp=%.2f *C, Volt=%.2f V\n",
               i, g_system_sensor.temperature, g_system_sensor.voltage);

        /* Nhấp nháy LED USR3 */
        control_bbb_led(1);
        usleep(100000); /* 100ms */
        control_bbb_led(0);

        /* Thử nghiệm hàm cấp phát bộ nhớ */
        if (i == 3) {
            process_sensor_buffer(8);
        }

        sleep(1);
    }

    printf("\n[SUCCESS] Hoàn thành chương trình thực nghiệm gỡ lỗi.\n");
    return 0;
}
