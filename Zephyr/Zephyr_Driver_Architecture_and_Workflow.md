# Kiến trúc Driver và Quy trình làm việc trong Zephyr RTOS

Trong Zephyr, một thiết bị/driver luôn được quản lý qua 3 lớp chính: **DeviceTree** (Phần cứng), **Kconfig** (Cấu hình phần mềm), và **C Code** (Logic thực thi).

---

## 1. Lớp DeviceTree (Mô tả phần cứng)
DeviceTree (các file `.dts`, `.dtsi`, `.overlay`) cho Zephyr biết phần cứng của bạn có những gì, nối vào chân nào.

- **Cách code/tinh chỉnh**: Ở mức ứng dụng, bạn không sửa trực tiếp file của Zephyr mà tạo một file `<board>.overlay` hoặc `app.overlay` trong thư mục code của bạn. Bạn sẽ định nghĩa các node mới hoặc ghi đè thông tin cũ.
- **Cần tìm thông tin ở đâu?**
  - **Yaml Bindings**: Mọi node trong DeviceTree đều cần một thuộc tính `compatible = "tên-hãng,tên-chip"`. Để biết phải điền các thuộc tính nào (ví dụ chân GPIO, địa chỉ I2C), hãy tìm kiếm thư mục `zephyr/dts/bindings/`. Các file `.yaml` trong này chính là "từ điển" hướng dẫn bạn viết file overlay cho thiết bị đó.
  - **Cấu trúc board**: Tìm trong `zephyr/boards/<kiến_trúc>/<tên_board>/` để xem board của bạn đang cấu hình sẵn những gì (ví dụ chân I2C đang ở pin nào).

## 2. Lớp Kconfig (Cấu hình tính năng phần mềm)
Kconfig quản lý việc module code nào được phép biên dịch, tính năng nào được bật/tắt (như `CONFIG_I2C=y`, `CONFIG_SENSOR=y`).

- **Cách code/tinh chỉnh**: Trong thư mục ứng dụng của bạn, chỉnh sửa file `prj.conf`. Bạn chỉ cần thêm `CONFIG_TÊN_TÍNH_NĂNG=y`.
- **Cần tìm thông tin ở đâu?**
  - Nếu bạn muốn dùng một driver (VD: cảm biến nhiệt độ), hãy vào thư mục chứa code của driver đó trong mã nguồn Zephyr (VD: `zephyr/drivers/sensor/`). Mở file `Kconfig` trong thư mục đó lên. Bạn sẽ thấy tên biến cấu hình cần bật để driver đó hoạt động (VD: `config SENSOR_BME280`, suy ra bạn cần `CONFIG_SENSOR_BME280=y`).
  - Hoặc bạn có thể chạy lệnh `west build -t menuconfig` trên terminal. Nó sẽ hiện ra giao diện UI để bạn search phím `/` và bật/tắt các config một cách trực quan.

## 3. Lớp C Code (API và Logic thực thi)
Zephyr thiết kế hệ thống driver rất đồng nhất. App của bạn sẽ không bao giờ gọi trực tiếp hàm của chip (như `bme280_read_temp()`) mà sẽ gọi qua API tiêu chuẩn chung của hệ thống (như `sensor_sample_fetch()`). 

- **Cách code**:
  - Trong code ứng dụng, bạn lấy "con trỏ" điều khiển thiết bị bằng macro từ DeviceTree: `const struct device *dev = DEVICE_DT_GET(DT_NODELABEL(my_sensor));`
  - Sau đó gọi các API chuẩn: `sensor_channel_get(dev, ...)`.
- **Cần tìm thông tin ở đâu?**
  - **Tìm API chuẩn**: Hãy vào `zephyr/include/zephyr/drivers/`. Đây là nơi chứa tất cả các header API (như `gpio.h`, `i2c.h`, `sensor.h`). Mở các file này ra đọc comment, bạn sẽ biết Zephyr cung cấp những hàm gì để giao tiếp với class thiết bị đó.
  - **Xem code driver gốc**: Nếu bạn muốn tự viết một driver mới, hãy copy một file driver có sẵn cùng loại trong `zephyr/drivers/<thư_mục_loại_thiết_bị>/`. Mỗi driver trong thư mục này thực chất là việc "đắp thịt" (implement) cho các API chuẩn ở trên và dùng macro `DEVICE_DT_DEFINE()` để đăng ký driver đó với Zephyr lúc khởi động hệ thống.
  - **Code mẫu (Sample)**: Luôn tham khảo thư mục `zephyr/samples/` (ví dụ `samples/sensor/`) hoặc `zephyr/tests/drivers/` để xem một driver cụ thể được gọi và cấu hình `prj.conf`, `.overlay` như thế nào.

---

## Tóm tắt Quy trình xử lý khi làm việc với Driver mới (Workflow chuẩn)

1. **Tìm tương thích (DeviceTree)**: 
   - Search xem mã nguồn có sẵn không bằng cách dò trong `zephyr/dts/bindings/` hoặc search code Zephyr xem có chữ nào giống tên chip của bạn không.
   - Viết file `app.overlay` để khai báo nó nối vào I2C/SPI hay GPIO nào, và set `compatible` tương ứng.
2. **Bật cấu hình (Kconfig)**:
   - Thêm `CONFIG_...=y` tương ứng vào `prj.conf`.
3. **Gọi trong Code (C API)**:
   - Include header chuẩn: `#include <zephyr/drivers/tên_lớp.h>`
   - Lấy struct device: `DEVICE_DT_GET()`
   - Gọi hàm thực thi.
4. **Debug (Nếu lỗi)**:
   - Nếu Code IDE (VS Code) báo đỏ lỗi chưa define thiết bị, hãy build lại bằng lệnh `west build ... -DCMAKE_EXPORT_COMPILE_COMMANDS=ON` để IDE cập nhật lại các Macro được generate ra từ file overlay.
   - Nếu IDE vẫn báo `#include` lỗi hoặc biến không tồn tại, tức là bước `prj.conf` bạn chưa bật đúng Config, khiến Zephyr đã loại bỏ driver đó ra khỏi quá trình biên dịch.
