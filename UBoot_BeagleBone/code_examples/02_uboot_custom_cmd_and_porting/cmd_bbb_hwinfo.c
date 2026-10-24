/**
 * ============================================================================
 * File: cmd/bbb_hwinfo.c (Đặt trong thư mục cmd/ của mã nguồn U-Boot)
 * Mục đích: Lệnh CLI tùy biến "bbb_hwinfo" chạy trực tiếp tại dấu nhắc U-Boot (=>)
 * Tài liệu tham chiếu: TI AM335x Technical Reference Manual (SPRUH73)
 *   - Chương 9 (Control Module):
 *       + 0x44E10040 (CONTROL_STATUS) : Chứa trạng thái chân SYSBOOT[15:0]
 *       + 0x44E10600 (DEVICE_ID)      : Chứa mã Silicon Revision & Part Number
 *   - Chương 25 (General-Purpose Input/Output - GPIO1 Base: 0x4804C000):
 *       + 0x4804C134 (GPIO_OE)          : Thanh ghi cấu hình hướng (0=Out, 1=In)
 *       + 0x4804C190 (GPIO_CLEARDATAOUT): Ghi 1 để kéo chân xuống mức THẤP (Tắt LED)
 *       + 0x4804C194 (GPIO_SETDATAOUT)  : Ghi 1 để kéo chân lên mức CAO (Bật LED)
 * ============================================================================
 */

#include <common.h>
#include <command.h>
#include <asm/io.h>
#include <linux/delay.h>

/* Địa chỉ các thanh ghi phần cứng AM335x (Memory-Mapped I/O) */
#define AM335X_CTRL_BASE            0x44E10000UL
#define AM335X_CTRL_STATUS_REG      (AM335X_CTRL_BASE + 0x0040UL)
#define AM335X_DEVICE_ID_REG        (AM335X_CTRL_BASE + 0x0600UL)

#define AM335X_GPIO1_BASE           0x4804C000UL
#define AM335X_GPIO_OE              (AM335X_GPIO1_BASE + 0x0134UL)
#define AM335X_GPIO_CLEARDATAOUT    (AM335X_GPIO1_BASE + 0x0190UL)
#define AM335X_GPIO_SETDATAOUT      (AM335X_GPIO1_BASE + 0x0194UL)

/* 4 đèn LED USR0..USR3 nối với GPIO1_21 .. GPIO1_24 */
#define USR_LED_MASK                (0x0FUL << 21)
#define USR_LED_BIT(n)              (1UL << (21 + ((n) & 0x3)))

static void decode_am335x_registers(void)
{
    uint32_t dev_id = readl(AM335X_DEVICE_ID_REG);
    uint32_t ctrl_status = readl(AM335X_CTRL_STATUS_REG);

    uint32_t rev = (dev_id >> 28) & 0x0F;
    uint32_t sysboot_pins = ctrl_status & 0xFFFF;
    uint32_t boot_seq = sysboot_pins & 0x1F; /* SYSBOOT[4:0] quyết định thứ tự Boot */

    printf("\n============================================================\n");
    printf("   CHẨN ĐOÁN PHẦN CỨNG TRỰC TIẾP TRONG U-BOOT (BARE-METAL)\n");
    printf("============================================================\n");
    printf("1. Thanh ghi DEVICE_ID      (0x44E10600) : 0x%08X\n", dev_id);
    printf("   -> Phiên bản chip AM335x              : PG%s (Rev code: 0x%X)\n",
           (rev == 2) ? "2.1" : (rev == 1) ? "2.0" : "1.0", rev);

    printf("2. Thanh ghi CONTROL_STATUS (0x44E10040) : 0x%08X\n", ctrl_status);
    printf("   -> Giá trị chân SYSBOOT[15:0]         : 0x%04X (SYSBOOT[4:0] = 0x%02X)\n",
           sysboot_pins, boot_seq);

    if (boot_seq == 0x1C) {
        /* 11100b: Nút S2 KHÔNG nhấn -> Ưu tiên MMC1 (eMMC) -> MMC0 (SD) -> UART0 -> USB0 */
        printf("   -> Trạng thái nút S2 lúc cấp nguồn    : KHÔNG NHẤN (Boot chuẩn: eMMC -> SD)\n");
    } else if (boot_seq == 0x18) {
        /* 11000b: Nút S2 ĐƯỢC NHẤN -> Ưu tiên SPI0 -> MMC0 (SD) -> USB0 -> UART0 */
        printf("   -> Trạng thái nút S2 lúc cấp nguồn    : ĐANG NHẤN GIỮ (Ép boot từ Thẻ nhớ SD)\n");
    } else {
        printf("   -> Trạng thái SYSBOOT tùy chỉnh       : Mã 0x%02X\n", boot_seq);
    }
    printf("============================================================\n");
}

static void control_usr_leds(const char *action)
{
    /* Cấu hình các chân GPIO1_21..24 làm Output (Xóa các bit 21..24 trong thanh ghi OE về 0) */
    uint32_t oe_val = readl(AM335X_GPIO_OE);
    oe_val &= ~USR_LED_MASK;
    writel(oe_val, AM335X_GPIO_OE);

    if (strcmp(action, "on") == 0) {
        writel(USR_LED_MASK, AM335X_GPIO_SETDATAOUT);
        printf("[U-Boot GPIO] Đã BẬT sáng toàn bộ 4 đèn LED USR0..USR3!\n");
    } else if (strcmp(action, "off") == 0) {
        writel(USR_LED_MASK, AM335X_GPIO_CLEARDATAOUT);
        printf("[U-Boot GPIO] Đã TẮT toàn bộ 4 đèn LED USR0..USR3!\n");
    } else if (strcmp(action, "blink") == 0) {
        printf("[U-Boot GPIO] Chạy hiệu ứng nháy đuổi 4 đèn LED USR0..USR3...\n");
        writel(USR_LED_MASK, AM335X_GPIO_CLEARDATAOUT);
        for (int i = 0; i < 3; i++) {
            for (int led = 0; led < 4; led++) {
                writel(USR_LED_BIT(led), AM335X_GPIO_SETDATAOUT);
                mdelay(120);
                writel(USR_LED_BIT(led), AM335X_GPIO_CLEARDATAOUT);
            }
        }
        printf("[U-Boot GPIO] Hoàn tất hiệu ứng nháy đèn!\n");
    }
}

static int do_bbb_hwinfo(struct cmd_tbl *cmdtp, int flag, int argc, char *const argv[])
{
    if (argc == 1 || strcmp(argv[1], "info") == 0) {
        decode_am335x_registers();
        return CMD_RET_SUCCESS;
    }

    if (strcmp(argv[1], "led") == 0 && argc >= 3) {
        control_usr_leds(argv[2]);
        return CMD_RET_SUCCESS;
    }

    return CMD_RET_USAGE;
}

U_BOOT_CMD(
    bbb_hwinfo, 3, 1, do_bbb_hwinfo,
    "Kiem tra thanh ghi AM335x (SYSBOOT, Silicon Rev) va dieu khien LED USR0..3",
    "info             - Doc thanh ghi DEVICE_ID va SYSBOOT[15:0]\n"
    "bbb_hwinfo led on|off|blink - Dieu khien trực tiếp thanh ghi GPIO1 bật/tắt 4 đèn LED"
);
