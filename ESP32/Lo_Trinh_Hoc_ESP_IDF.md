# Sổ Tay Lộ Trình Học Lập Trình ESP-IDF (Cơ bản đến Nâng cao)

Tài liệu này được biên soạn để cung cấp một quy trình học tập logic, đi từ tổng quan cấu trúc thư mục đến chi tiết logic từng dòng code và các file cấu hình quan trọng trong hệ sinh thái ESP-IDF.

---

## Phần 1: Quy Trình Các Thư Mục Lớn (Bản đồ học tập)

Thay vì đi lang thang trong hàng trăm ví dụ của ESP-IDF, bạn hãy đi theo quy trình 6 bước dưới đây (tương ứng với các thư mục trong `esp-idf/examples/`):

1. **`get-started` (Bắt đầu):** Nơi học cách một project sống sót. (Ví dụ: `hello_world`, `blink`).
2. **`peripherals` (Ngoại vi):** Làm chủ phần cứng cơ bản. Không có giao tiếp ngoài (Mạng) nào chạy tốt nếu không hiểu phần cứng. (Ví dụ: `gpio`, `uart`, `i2c`, `adc`).
3. **`system` (Hệ thống & Đa nhiệm):** Hiểu cách FreeRTOS hoạt động, cấp phát bộ nhớ, xử lý ngắt và lỗi. (Ví dụ: `freertos`, `ota`).
4. **`storage` (Lưu trữ):** Cách giữ lại dữ liệu khi mất điện. (Ví dụ: `nvs_rw_blob`, `spiffs`).
5. **`protocols` & `wifi` (Giao thức & Mạng):** Kết nối thiết bị ra thế giới IoT. (Ví dụ: `mqtt/tcp`, `http_client`, `wifi/getting_started`).
6. **`bluetooth` (Tùy chọn):** Kết nối gần, tiêu thụ ít năng lượng (BLE).

---

## Phần 2: Phân Tích Logic Code & Ví Dụ Cốt Lõi

Chúng ta sẽ đi sâu vào 2 ví dụ nền tảng nhất: **Blink LED** (Đại diện cho Get-Started) và **Generic GPIO** (Đại diện cho Peripherals / Interrupt).

### Ví dụ 1: Blink LED (Nháy đèn)
**Đường dẫn tham khảo:** `/home/thinh/esp/esp-idf/examples/get-started/blink`

**Cấu trúc Logic Code:**

```c
// 1. INCLUDE HEADERS
#include <stdio.h>
#include "freertos/FreeRTOS.h" // Thư viện lõi của hệ điều hành thời gian thực
#include "freertos/task.h"     // Thư viện xử lý Task (luồng)
#include "driver/gpio.h"       // Thư viện điều khiển GPIO phần cứng
#include "esp_log.h"           // Thư viện in log ra màn hình console

// 2. DEFINES & MACROS
static const char *TAG = "example";
#define BLINK_GPIO 2 // Chân kết nối LED (Tùy board)

// 3. HÀM MAIN CỦA ESP-IDF (Entry point)
void app_main(void)
{
    // Bước A: Khởi tạo phần cứng (Initialization)
    // Xóa cấu hình cũ và thiết lập chân BLINK_GPIO làm Output
    gpio_reset_pin(BLINK_GPIO);
    gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);

    int s_led_state = 0; // Trạng thái LED ban đầu

    // Bước B: Vòng lặp chính (Main Loop - Tương tự loop() trong Arduino)
    while (1) {
        ESP_LOGI(TAG, "Turning the LED %s!", s_led_state == true ? "ON" : "OFF");
        
        // Cập nhật mức điện áp ra chân GPIO (1 = HIGH, 0 = LOW)
        gpio_set_level(BLINK_GPIO, s_led_state);
        
        // Đảo trạng thái cho lần tiếp theo
        s_led_state = !s_led_state;
        
        // YÊU CẦU BẮT BUỘC TRONG FREERTOS: Trả lại quyền điều khiển cho CPU (Delay)
        // Nếu không có hàm này, Watchdog Timer sẽ reset chip vì tưởng chip bị treo.
        vTaskDelay(1000 / portTICK_PERIOD_MS); // Delay 1000 mili-giây
    }
}
```

**Note Logic Quan Trọng:**
*   Trong ESP-IDF, chương trình bắt đầu tại `app_main()`, không phải `main()`.
*   Khác với Arduino, trong vòng lặp `while(1)`, bạn BẮT BUỘC phải có `vTaskDelay`. Nếu không, task này sẽ chiếm 100% CPU và gây lỗi Task Watchdog.

### Ví dụ 2: Generic GPIO & Ngắt (Interrupt)
**Đường dẫn tham khảo:** `/home/thinh/esp/esp-idf/examples/peripherals/gpio/generic_gpio`

**Cấu trúc Logic Code:**

```c
// ... (Includes giống phần trên) ...
#include "freertos/queue.h"

#define GPIO_INPUT_IO_0     4
#define GPIO_OUTPUT_IO_0    18

// Queue để truyền dữ liệu từ hàm Ngắt (ISR) sang Task xử lý chính
static QueueHandle_t gpio_evt_queue = NULL;

// 1. HÀM XỬ LÝ NGẮT (ISR - Interrupt Service Routine)
// Chú ý: IRAM_ATTR bắt buộc hàm này phải được nạp vào RAM (thay vì Flash) để chạy cực nhanh
static void IRAM_ATTR gpio_isr_handler(void* arg)
{
    uint32_t gpio_num = (uint32_t) arg;
    // Gửi số thứ tự chân GPIO vào Queue, không được phép xử lý logic nặng tại đây!
    xQueueSendFromISR(gpio_evt_queue, &gpio_num, NULL);
}

// 2. TASK XỬ LÝ SỰ KIỆN NÚT NHẤN
static void gpio_task_example(void* arg)
{
    uint32_t io_num;
    for(;;) {
        // Đợi đến khi có tín hiệu từ Queue (gửi từ hàm ngắt)
        // portMAX_DELAY nghĩa là chờ vô hạn, CPU không bị block, task đi ngủ.
        if(xQueueReceive(gpio_evt_queue, &io_num, portMAX_DELAY)) {
            printf("GPIO[%lu] intr, val: %d\n", io_num, gpio_get_level(io_num));
        }
    }
}

void app_main(void)
{
    // Cấu hình Input & Output bằng struct (chuyên nghiệp hơn dùng lệnh rời rạc)
    gpio_config_t io_conf = {};
    io_conf.intr_type = GPIO_INTR_ANYEDGE; // Ngắt khi có thay đổi trạng thái (Lên hoặc Xuống)
    io_conf.pin_bit_mask = (1ULL<<GPIO_INPUT_IO_0); // Chọn chân
    io_conf.mode = GPIO_MODE_INPUT; // Chế độ Input
    io_conf.pull_up_en = 1; // Bật điện trở kéo lên
    gpio_config(&io_conf); // Áp dụng cấu hình

    // Tạo Queue (Nhận tối đa 10 phần tử, mỗi phần tử kích thước 32-bit)
    gpio_evt_queue = xQueueCreate(10, sizeof(uint32_t));
    
    // Tạo Task chạy ngầm
    xTaskCreate(gpio_task_example, "gpio_task_example", 2048, NULL, 10, NULL);

    // Cài đặt dịch vụ Ngắt toàn cục
    gpio_install_isr_service(0);
    // Gắn hàm ngắt vào chân Input cụ thể
    gpio_isr_handler_add(GPIO_INPUT_IO_0, gpio_isr_handler, (void*) GPIO_INPUT_IO_0);
}
```

**Note Logic Quan Trọng:**
*   Hàm ngắt (`gpio_isr_handler`) phải rất ngắn gọn. Không dùng `printf()` hay delay trong hàm ngắt.
*   Cơ chế: Ngắt xảy ra -> Đẩy ID vào Queue -> Task (`gpio_task_example`) đang ngủ chờ Queue sẽ thức dậy xử lý -> Xử lý xong quay lại ngủ tiếp. (Kiến trúc chuẩn của hệ thống nhúng).

---

## Phần 3: Quản Lý File Cấu Hình Dự Án (Config)

Trong ESP-IDF, code C không tự nhiên mà chạy. Nó bị chi phối bởi Hệ thống Build (CMake) và Hệ thống Cấu hình (Kconfig).

### 1. File `CMakeLists.txt` (Hệ thống Build)
Có 2 loại file CMakeLists.txt trong 1 dự án:
*   **Project level `CMakeLists.txt` (Nằm ở thư mục gốc):**
    ```cmake
    cmake_minimum_required(VERSION 3.16)
    include($ENV{IDF_PATH}/tools/cmake/project.cmake)
    project(my_esp_project)
    ```
    *Logic:* Yêu cầu bắt buộc để khai báo đây là một dự án ESP-IDF. Hàm `project()` định nghĩa tên ứng dụng cuối cùng.
*   **Component level `main/CMakeLists.txt` (Nằm trong thư mục `main`):**
    ```cmake
    idf_component_register(SRCS "main.c" "wifi_module.c"
                           INCLUDE_DIRS "."
                           REQUIRES "nvs_flash" "mqtt")
    ```
    *Logic:* Khai báo những file `.c` nào cần biên dịch (`SRCS`), thư mục chứa file `.h` (`INCLUDE_DIRS`), và dự án này CẦN dùng thêm thư viện nào của ESP-IDF (`REQUIRES`). Nếu bạn dùng MQTT mà quên thêm `"mqtt"` vào `REQUIRES`, quá trình biên dịch sẽ báo lỗi *undefined reference*.

### 2. Các file Cấu hình Môi trường (Kconfig & sdkconfig)
ESP-IDF sử dụng một công cụ gọi là Menuconfig (chạy lệnh `idf.py menuconfig`) để bật/tắt các tính năng hệ thống mà không cần sửa code.
*   **`Kconfig.projbuild` (Nếu có):** Nơi bạn tự định nghĩa các menu cấu hình riêng cho project của mình (Ví dụ: Ô nhập mật khẩu Wi-Fi mặc định).
*   **`sdkconfig` (File tự động tạo):** Sau khi bạn lưu cài đặt trong `menuconfig`, toàn bộ sẽ ghi vào file này dưới dạng các định nghĩa (Ví dụ: `CONFIG_ESP_WIFI_SSID="my_wifi"`). File này quản lý tần số CPU, kích thước bộ nhớ Flash, và độ phân giải Log hệ thống. Cực kỳ quan trọng khi bạn muốn đổi chip (ví dụ từ esp32 sang esp32s3).

### 3. File Phân Vùng (`partitions.csv` - Tùy chọn)
Khi project lớn lên, bạn muốn chia bộ nhớ Flash 4MB thành các vùng: Vùng chứa Code (App), vùng chứa dữ liệu NVS, vùng chứa OTA (để update phần mềm từ xa). Khai báo trong file này và kích hoạt nó qua `menuconfig`.
