# ==============================================================================
# Makefile: Biên dịch ứng dụng C gỡ lỗi từ xa cho BeagleBone Black (ARM Cortex-A8)
# Hỗ trợ tự động kết nối Yocto Native Toolchain hoặc System Cross Compiler
# ==============================================================================

TARGET = hello_debug
SRCS   = src/hello_debug.c

# Cấu hình IP và thư mục nạp mã trên BeagleBone Black qua USB RNDIS (192.168.7.2)
TARGET_IP  ?= 192.168.7.2
TARGET_DIR ?= /home/root

# Đường dẫn Toolchain tích hợp từ Yocto Build System
YOCTO_NATIVE_BIN = /home/thinh/yocto-bbb/build/tmp/work/cortexa8hf-neon-poky-linux-gnueabi/my-app/1.0/recipe-sysroot-native/usr/bin/arm-poky-linux-gnueabi
YOCTO_GCC        = $(YOCTO_NATIVE_BIN)/arm-poky-linux-gnueabi-gcc
YOCTO_SYSROOT    = /home/thinh/yocto-bbb/build/tmp/work/cortexa8hf-neon-poky-linux-gnueabi/my-app/1.0/recipe-sysroot

ifneq ($(wildcard $(YOCTO_GCC)),)
    # 1. Ưu tiên: Dùng chính xác GCC từ Yocto Scarthgap (tương thích 100% Glibc 2.39)
    export PATH := $(YOCTO_NATIVE_BIN):$(PATH)
    CC           = $(YOCTO_GCC)
    CFLAGS       = -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a8 \
                   --sysroot=$(YOCTO_SYSROOT) \
                   -Wall -Wextra -g -O0
else
    # 2. Dự phòng: Dùng arm-linux-gnueabihf-gcc cài trên máy chủ Ubuntu
    CROSS_COMPILE ?= arm-linux-gnueabihf-
    CC             = $(CROSS_COMPILE)gcc
    CFLAGS         = -Wall -Wextra -g -O0
endif

.PHONY: all clean deploy debug_symbols run_local_check

all: $(TARGET)

$(TARGET): $(SRCS)
	@echo "==> [CC] Biên dịch $< sang ARM ELF có ký hiệu gỡ lỗi (-g -O0)..."
	$(CC) $(CFLAGS) $< -o $@
	@echo "==> [OK] Đã tạo thành công binary: $@"
	@file $@

debug_symbols: $(TARGET)
	@echo "==> [DEBUG SYMBOLS] Kiểm tra các Section DWARF trong file ELF:"
	@readelf -S $(TARGET) | grep -E "debug_info|debug_line|debug_str" || echo "Không có debug info!"

deploy: $(TARGET)
	@echo "==> [SCP] Sao chép $(TARGET) sang BeagleBone Black ($(TARGET_IP):$(TARGET_DIR))..."
	scp -o StrictHostKeyChecking=no $(TARGET) root@$(TARGET_IP):$(TARGET_DIR)/
	@ssh -o StrictHostKeyChecking=no root@$(TARGET_IP) "chmod +x $(TARGET_DIR)/$(TARGET)"
	@echo "==> [OK] Đã nạp file và cấp quyền thực thi trên target!"

clean:
	rm -f $(TARGET)
