# Hướng dẫn tra cứu tài liệu và Config (Ví dụ thực tế với nRF52840 PWM)

Để hiểu cách "truy vết" tài liệu và config trong Zephyr, chúng ta sử dụng một ví dụ thực tế trên con chip **nRF52840**: **Làm sao để dùng khối băm xung (PWM) phần cứng của chip này?** 

Dưới đây là quy trình 4 bước chuẩn để tự tìm hiểu bất kỳ ngoại vi (peripheral) nào.

---

## Bước 1: Tìm xem chip định nghĩa ngoại vi đó như thế nào (DeviceTree)
Mọi tài nguyên phần cứng của con chip đều được nhà sản xuất khai báo sẵn. Bạn không cần tự viết lại mà chỉ cần xem họ viết tên nó là gì.

1. Vào thư mục chứa mô tả chip nRF52840: `zephyr/dts/arm/nordic/`
2. Mở file `nrf52840.dtsi` lên và search từ khóa `pwm`.
3. Bạn sẽ thấy các node được khai báo sẵn như sau:
   ```dts
   pwm0: pwm@4001c000 {
       compatible = "nordic,nrf-pwm";
       reg = <0x4001c000 0x1000>;
       status = "disabled";
   };
   ```
> [!NOTE] Thu hoạch
> - Tên node của thiết bị này là `pwm0`. Trạng thái gốc của nó là `"disabled"` (tắt).
> - **"Từ khóa vàng"** (compatible string) của thiết bị này là **`"nordic,nrf-pwm"`**. Đây là chìa khóa để làm tất cả các bước tiếp theo.

---

## Bước 2: Đọc tài liệu (Doc) để biết cách viết file `.overlay`
Bây giờ bạn biết tên khóa là `"nordic,nrf-pwm"`, nhưng bạn cần biết các thuộc tính cấu hình (ví dụ: chân GPIO).

1. Vào thư mục "từ điển" DeviceTree: `zephyr/dts/bindings/`
2. Vào thư mục con `pwm/` và tìm file có tên giống hệt từ khóa vàng: `zephyr/dts/bindings/pwm/nordic,nrf-pwm.yaml`
3. Mở file `yaml` này ra (hoặc xem bản web [Zephyr Bindings Index](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html)). Đọc phần description và `properties`. 
4. Trong file yaml, nó hướng dẫn rằng bạn cần truyền thuộc tính `pinctrl-0` để chọn chân.

> [!NOTE] Thu hoạch
> Biết cách tự viết file `app.overlay` cho project của bạn như sau:
> ```dts
> &pwm0 {
>     status = "okay";               /* Bật khối PWM này lên */
>     pinctrl-0 = <&pwm0_default>;   /* Chỉ định cấu hình chân GPIO */
>     pinctrl-names = "default";
> };
> ```

---

## Bước 3: Tìm cấu hình phần mềm trong Kconfig
Đã bật phần cứng (DeviceTree), giờ phải bật driver phần mềm để code C biên dịch được.

1. Vào thư mục chứa toàn bộ driver của Zephyr: `zephyr/drivers/`
2. Vào thư mục `pwm/`. Mở các file có tên `Kconfig` (ví dụ `Kconfig.nrfx`) ra và tìm chữ `nrf-pwm`.
3. Bạn sẽ tìm thấy đoạn khai báo:
   ```kconfig
   config PWM_NRFX
       bool "nRF PWM driver"
       default y
       depends on DT_HAS_NORDIC_NRF_PWM_ENABLED
   ```

> [!NOTE] Thu hoạch
> - Biến config là `CONFIG_PWM_NRFX`. 
> - Chú ý dòng `default y depends on DT_HAS_NORDIC_NRF_PWM_ENABLED`. Khi bạn set `status = "okay"` trong file `.overlay`, Zephyr sẽ **tự động bật** biến `CONFIG_PWM_NRFX=y` cho bạn mà không cần gõ vào `prj.conf`. (Tuy nhiên, bạn vẫn cần bật module gốc `CONFIG_PWM=y` trong `prj.conf`).

---

## Bước 4: Xem hàm API để Code và tìm Code mẫu
Phần cứng và config đã xong, bước cuối là code `main.c`.

1. **Tìm API chuẩn:** 
   Vào `zephyr/include/zephyr/drivers/` và mở file `pwm.h`. Đọc các comment API chuẩn. Hàm thường dùng là `pwm_set_dt()`. 
2. **Tìm Code mẫu (Samples):**
   Vào thư mục `zephyr/samples/`. Tìm đến `zephyr/samples/basic/blinky_pwm/`.
3. Mở file `src/main.c` trong đó lên, bạn sẽ thấy cách gọi API chuẩn:
   ```c
   #include <zephyr/drivers/pwm.h> // Include file thư viện chuẩn

   // Lấy con trỏ phần cứng từ DeviceTree
   static const struct pwm_dt_spec pwm_led0 = PWM_DT_SPEC_GET(DT_ALIAS(pwm_led0));
   
   void main(void) {
       // Gọi hàm API chuẩn để đẩy xung PWM ra chân đèn LED
       pwm_set_pulse_dt(&pwm_led0, pulse_width); 
   }
   ```

## 📝 Tổng kết luồng tìm kiếm chuẩn:
1. Xem `.dtsi` của chip -> lấy tên `compatible`.
2. Lấy `compatible` -> tìm file `.yaml` trong `dts/bindings/` để biết luật chơi của phần cứng.
3. Lấy `compatible` -> tìm file `Kconfig` trong thư mục `drivers/` để biết luật chơi của phần mềm (`CONFIG_...`).
4. Tìm trong `include/zephyr/drivers/` để lấy API (file `.h`), và tìm trong `samples/` để chép code mẫu.
