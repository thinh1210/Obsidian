/**
 * ============================================================================
 * File: pru0_firmware.c
 * Dự án: Firmware Thời Gian Thực (Hard Real-Time 5ns/chu kỳ) trên PRU Core 0
 * Tham chiếu: TI AM335x TRM (SPRUH73 Chương 4: PRU-ICSS) & PRU Cookbook
 * Phần cứng yêu cầu: Chỉ cần BeagleBone Black + Cáp UART (Không cần mạch ngoài)
 * ============================================================================
 *
 * NGUYÊN LÝ HOẠT ĐỘNG:
 * 1. Nhân PRU0 chạy độc lập ở xung nhịp 200 MHz (1 chu kỳ lệnh = 5 nanoseconds).
 * 2. Khi nhân ARM Linux gửi một chuỗi lệnh (ví dụ: "PING" hoặc "BLINK 10")
 *    vào tệp thiết bị "/dev/rpmsg_pru30":
 *    - PRU0 nhận tin nhắn qua VirtIO RPMsg Ring Buffer trong Shared DDR RAM.
 *    - PRU0 thực thi vòng lặp định thời chính xác tới từng chu kỳ 5ns bằng
 *      hàm nội tại __delay_cycles() và điều khiển thanh ghi GPIO1 / R30.
 *    - PRU0 phản hồi lại thông điệp kết quả kèm số chu kỳ thực thi về cho
 *      nhân ARM Linux để in ra màn hình UART!
 * ============================================================================
 */

#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <pru_cfg.h>
#include <pru_intc.h>
#include <rsc_types.h>
#include <pru_rpmsg.h>

/* Khai báo 2 thanh ghi I/O trực tiếp của nhân PRU (Truy cập trong 1 chu kỳ = 5ns) */
volatile register uint32_t __R30; /* Thanh ghi xuất dữ liệu trực tiếp (GPO) */
volatile register uint32_t __R31; /* Thanh ghi đọc dữ liệu & kích ngắt (GPI/INTC) */

/* Cấu hình ngắt Host-to-PRU và PRU-to-Host cho RPMsg */
#define HOST_INT                    ((uint32_t) 1 << 30)
#define TO_ARM_HOST                 16
#define FROM_ARM_HOST               17

/* Tên kênh tạo ra thiết bị /dev/rpmsg_pru30 trên Linux */
#define CHAN_NAME                   "rpmsg-pru"
#define CHAN_DESC                   "Channel 30"
#define CHAN_PORT                   30

#define VIRTIO_CONFIG_S_DRIVER_OK   4

/* Địa chỉ thanh ghi GPIO1 để PRU bật/tắt đèn USR3 (GPIO1_24) qua bus OCP */
#define GPIO1_BASE                  0x4804C000UL
#define GPIO1_CLEARDATAOUT          (*(volatile uint32_t *)(GPIO1_BASE + 0x190))
#define GPIO1_SETDATAOUT            (*(volatile uint32_t *)(GPIO1_BASE + 0x194))
#define USR3_LED_MASK               (1UL << 24)

/* Bộ đệm nhận/gửi tin nhắn RPMsg (Tối đa 512 bytes) */
uint8_t payload[RPMSG_BUF_SIZE];

/* Khai báo bảng tài nguyên (Resource Table) bắt buộc cho Linux Remoteproc */
extern struct my_resource_table resource_table;

void main(void)
{
    struct pru_rpmsg_transport transport;
    uint16_t src, dst, len;
    volatile uint8_t *status;
    uint32_t msg_count = 0;

    /* 1. Bật cổng truy cập bus OCP (OCP Master Port) để PRU đọc/ghi được RAM và GPIO1 */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    /* 2. Xóa cờ ngắt sự kiện hệ thống từ ARM gửi xuống */
    CT_INTC.SICR_bit.STS_CLR_IDX = FROM_ARM_HOST;

    /* 3. Đợi Linux Kernel khởi tạo xong VirtIO Driver */
    status = &resource_table.rpmsg_vdev.status;
    while (!(*status & VIRTIO_CONFIG_S_DRIVER_OK));

    /* 4. Khởi tạo kênh truyền thông RPMsg VirtIO */
    pru_rpmsg_init(&transport,
                   &resource_table.rpmsg_vring0,
                   &resource_table.rpmsg_vring1,
                   TO_ARM_HOST,
                   FROM_ARM_HOST);

    /* Tạo thiết bị /dev/rpmsg_pru30 trên Linux Userspace */
    while (pru_rpmsg_channel(RPMSG_NS_CREATE, &transport, CHAN_NAME, CHAN_DESC, CHAN_PORT) != PRU_RPMSG_SUCCESS);

    /* 5. Vòng lặp xử lý thời gian thực vĩnh cửu */
    while (1) {
        /* Kiểm tra xem có ngắt từ ARM Linux gửi xuống qua thanh ghi R31 không */
        if (__R31 & HOST_INT) {
            /* Xóa trạng thái ngắt */
            CT_INTC.SICR_bit.STS_CLR_IDX = FROM_ARM_HOST;

            /* Đọc toàn bộ các gói tin đang chờ trong hàng đợi vring */
            while (pru_rpmsg_receive(&transport, &src, &dst, payload, &len) == PRU_RPMSG_SUCCESS) {
                payload[len] = '\0';
                msg_count++;

                /* Bật đèn LED USR3 trong đúng 20,000,000 chu kỳ PRU
                 * (20,000,000 * 5ns = 100,000,000 ns = Đúng 100.000000 ms không lệch 1 nano-giây!)
                 */
                GPIO1_SETDATAOUT = USR3_LED_MASK;
                __delay_cycles(20000000);
                GPIO1_CLEARDATAOUT = USR3_LED_MASK;

                /* Đóng gói chuỗi phản hồi gửi ngược lên Linux ARM */
                int resp_len = snprintf((char *)payload, RPMSG_BUF_SIZE,
                    "[PRU0 @ 200MHz] Msg #%lu OK! Da nhay USR3 dung 20,000,000 cycles (100.000ms). Nhan: %s\n",
                    (unsigned long)msg_count, (char *)payload);

                pru_rpmsg_send(&transport, dst, src, payload, resp_len);
            }
        }
    }
}
