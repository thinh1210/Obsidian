# ============================================================================
# Makefile cho Linux Kernel Module: bbb_mmio_kmod
# Hỗ trợ biên dịch trực tiếp trên BeagleBone, Cross-Compile, và Yocto Project
# ============================================================================

obj-m += bbb_mmio_kmod.o

# Đường dẫn thư mục Kernel build (Mặc định lấy kernel đang chạy hoặc biến KERNEL_SRC từ Yocto)
KERNEL_SRC ?= /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(KERNEL_SRC) M=$(PWD) modules

modules_install:
	$(MAKE) -C $(KERNEL_SRC) M=$(PWD) modules_install

clean:
	$(MAKE) -C $(KERNEL_SRC) M=$(PWD) clean
