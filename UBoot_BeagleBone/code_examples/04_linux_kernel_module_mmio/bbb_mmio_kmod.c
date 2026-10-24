/**
 * ============================================================================
 * File: bbb_mmio_kmod.c
 * Dự án: Linux Kernel Module điều khiển trực tiếp thanh ghi MMIO AM335x
 * Cấp độ: Chuyên sâu (Kết hợp Linux Kernel Internals & TI SPRUH73 TRM)
 * Phần cứng yêu cầu: Chỉ cần BeagleBone Black + Thẻ nhớ + Cáp UART Debug
 * ============================================================================
 *
 * CƠ CHẾ HOẠT ĐỘNG:
 * 1. Khi nạp module (insmod bbb_mmio_kmod.ko):
 *    - Dùng hàm ioremap() ánh xạ địa chỉ vật lý của khối Control Module
 *      (0x44E10000) và khối GPIO1 (0x4804C000) vào không gian địa chỉ ảo Kernel.
 *    - Tạo tệp tin giao tiếp ảo "/proc/bbb_mmio".
 * 2. Khi người dùng gõ "cat /proc/bbb_mmio" trên màn hình UART:
 *    - Kernel đọc trực tiếp các thanh ghi 32-bit bằng ioread32() và trả về
 *      bảng phân tích trạng thái phần cứng.
 * 3. Khi người dùng gõ lệnh trên UART:
 *    - "echo on > /proc/bbb_mmio"  -> Ghi vào GPIO_SETDATAOUT bật sáng 4 đèn USR0..3
 *    - "echo off > /proc/bbb_mmio" -> Ghi vào GPIO_CLEARDATAOUT tắt 4 đèn USR0..3
 * ============================================================================
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/uaccess.h>
#include <linux/io.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Thinh Embedded Lab");
MODULE_DESCRIPTION("Direct MMIO Register Driver for TI AM335x (BeagleBone Black)");
MODULE_VERSION("1.0");

/* Địa chỉ vật lý theo tài liệu TI AM335x TRM (SPRUH73) */
#define AM335X_CTRL_PHYS_BASE       0x44E10000UL
#define AM335X_CTRL_SIZE            0x1000UL
#define OFFSET_CTRL_STATUS          0x0040UL
#define OFFSET_DEVICE_ID            0x0600UL

#define AM335X_GPIO1_PHYS_BASE      0x4804C000UL
#define AM335X_GPIO1_SIZE           0x1000UL
#define OFFSET_GPIO_SYSSTATUS       0x0114UL
#define OFFSET_GPIO_OE              0x0134UL
#define OFFSET_GPIO_DATAIN          0x0138UL
#define OFFSET_GPIO_DATAOUT         0x013CUL
#define OFFSET_GPIO_CLEARDATAOUT    0x0190UL
#define OFFSET_GPIO_SETDATAOUT      0x0194UL

/* Mặt nạ 4 đèn LED USR0..USR3 (GPIO1_21 đến GPIO1_24) */
#define USR_LEDS_MASK               (0x0FUL << 21)

#define PROC_FILENAME               "bbb_mmio"

static void __iomem *ctrl_base = NULL;
static void __iomem *gpio1_base = NULL;
static struct proc_dir_entry *bbb_proc_entry = NULL;

/* Hàm hiển thị khi người dùng chạy: cat /proc/bbb_mmio */
static int bbb_mmio_proc_show(struct seq_file *m, void *v)
{
    u32 dev_id      = ioread32(ctrl_base + OFFSET_DEVICE_ID);
    u32 ctrl_status = ioread32(ctrl_base + OFFSET_CTRL_STATUS);
    u32 gpio_oe     = ioread32(gpio1_base + OFFSET_GPIO_OE);
    u32 gpio_out    = ioread32(gpio1_base + OFFSET_GPIO_DATAOUT);

    seq_printf(m, "================================================================\n");
    seq_printf(m, " BẢNG TRẠNG THÁI THANH GHI AM335X (ĐỌC TỪ KERNEL SPACE MMIO)\n");
    seq_printf(m, "================================================================\n");
    seq_printf(m, "1. CONTROL_MODULE (Phys: 0x44E10000 -> Virt: %px)\n", ctrl_base);
    seq_printf(m, "   + DEVICE_ID      (Offset 0x600) : 0x%08X (Silicon Rev Code: %u)\n",
               dev_id, (dev_id >> 28) & 0xF);
    seq_printf(m, "   + CONTROL_STATUS (Offset 0x040) : 0x%08X (SYSBOOT[4:0] = 0x%02X)\n",
               ctrl_status, ctrl_status & 0x1F);
    seq_printf(m, "\n");
    seq_printf(m, "2. GPIO1_MODULE   (Phys: 0x4804C000 -> Virt: %px)\n", gpio1_base);
    seq_printf(m, "   + GPIO_OE        (Offset 0x134) : 0x%08X\n", gpio_oe);
    seq_printf(m, "   + GPIO_DATAOUT   (Offset 0x13C) : 0x%08X\n", gpio_out);
    seq_printf(m, "   + Trạng thái 4 đèn LED Onboard  : USR0=[%d] USR1=[%d] USR2=[%d] USR3=[%d]\n",
               (gpio_out >> 21) & 1,
               (gpio_out >> 22) & 1,
               (gpio_out >> 23) & 1,
               (gpio_out >> 24) & 1);
    seq_printf(m, "================================================================\n");
    seq_printf(m, "Hướng dẫn điều khiển từ UART:\n");
    seq_printf(m, "  echo on   > /proc/bbb_mmio   (Bật sáng cả 4 đèn LED USR0..3)\n");
    seq_printf(m, "  echo off  > /proc/bbb_mmio   (Tắt cả 4 đèn LED USR0..3)\n");
    seq_printf(m, "  echo led0 > /proc/bbb_mmio   (Đảo trạng thái đèn USR0)\n");
    seq_printf(m, "================================================================\n");

    return 0;
}

static int bbb_mmio_proc_open(struct inode *inode, struct file *file)
{
    return single_open(file, bbb_mmio_proc_show, NULL);
}

/* Hàm xử lý khi người dùng chạy: echo "..." > /proc/bbb_mmio */
static ssize_t bbb_mmio_proc_write(struct file *file, const char __user *ubuf,
                                   size_t count, loff_t *ppos)
{
    char kbuf[32];
    u32 oe_reg, out_reg;

    if (count >= sizeof(kbuf))
        return -EINVAL;

    if (copy_from_user(kbuf, ubuf, count))
        return -EFAULT;

    kbuf[count] = '\0';

    /* Đảm bảo các chân GPIO1_21..24 được cấu hình là Output (bit = 0) */
    oe_reg = ioread32(gpio1_base + OFFSET_GPIO_OE);
    oe_reg &= ~USR_LEDS_MASK;
    iowrite32(oe_reg, gpio1_base + OFFSET_GPIO_OE);

    if (strncmp(kbuf, "on", 2) == 0) {
        iowrite32(USR_LEDS_MASK, gpio1_base + OFFSET_GPIO_SETDATAOUT);
        pr_info("bbb_mmio: Da BAT toan bo 4 den LED USR0..3 qua thanh ghi GPIO_SETDATAOUT\n");
    } else if (strncmp(kbuf, "off", 3) == 0) {
        iowrite32(USR_LEDS_MASK, gpio1_base + OFFSET_GPIO_CLEARDATAOUT);
        pr_info("bbb_mmio: Da TAT toan bo 4 den LED USR0..3 qua thanh ghi GPIO_CLEARDATAOUT\n");
    } else if (strncmp(kbuf, "led", 3) == 0 && kbuf[3] >= '0' && kbuf[3] <= '3') {
        int idx = kbuf[3] - '0';
        u32 mask = (1UL << (21 + idx));
        out_reg = ioread32(gpio1_base + OFFSET_GPIO_DATAOUT);
        if (out_reg & mask)
            iowrite32(mask, gpio1_base + OFFSET_GPIO_CLEARDATAOUT);
        else
            iowrite32(mask, gpio1_base + OFFSET_GPIO_SETDATAOUT);
        pr_info("bbb_mmio: Da dao trang thai den USR%d\n", idx);
    } else {
        pr_warn("bbb_mmio: Lenh khong hop le: %s\n", kbuf);
    }

    return count;
}

static const struct proc_ops bbb_mmio_fops = {
    .proc_open    = bbb_mmio_proc_open,
    .proc_read    = seq_read,
    .proc_write   = bbb_mmio_proc_write,
    .proc_lseek   = seq_lseek,
    .proc_release = single_release,
};

static int __init bbb_mmio_init(void)
{
    pr_info("bbb_mmio: Dang khoi tao driver MMIO cho TI AM335x...\n");

    ctrl_base = ioremap(AM335X_CTRL_PHYS_BASE, AM335X_CTRL_SIZE);
    if (!ctrl_base) {
        pr_err("bbb_mmio: Khong the ioremap CONTROL_MODULE!\n");
        return -ENOMEM;
    }

    gpio1_base = ioremap(AM335X_GPIO1_PHYS_BASE, AM335X_GPIO1_SIZE);
    if (!gpio1_base) {
        pr_err("bbb_mmio: Khong the ioremap GPIO1!\n");
        iounmap(ctrl_base);
        return -ENOMEM;
    }

    bbb_proc_entry = proc_create(PROC_FILENAME, 0666, NULL, &bbb_mmio_fops);
    if (!bbb_proc_entry) {
        pr_err("bbb_mmio: Khong the tao /proc/%s\n", PROC_FILENAME);
        iounmap(gpio1_base);
        iounmap(ctrl_base);
        return -ENOMEM;
    }

    pr_info("bbb_mmio: Khoi tao thanh cong! Hay dung lenh 'cat /proc/bbb_mmio'\n");
    return 0;
}

static void __exit bbb_mmio_exit(void)
{
    proc_remove(bbb_proc_entry);
    if (gpio1_base)
        iounmap(gpio1_base);
    if (ctrl_base)
        iounmap(ctrl_base);
    pr_info("bbb_mmio: Da go bo driver MMIO an toan.\n");
}

module_init(bbb_mmio_init);
module_exit(bbb_mmio_exit);
