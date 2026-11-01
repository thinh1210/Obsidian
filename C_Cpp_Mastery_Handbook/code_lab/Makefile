CC = gcc
CFLAGS = -Wall -Wextra -Wpedantic -Wno-unused-function -std=c11 -O2

SRCS = 01_packed_vs_aligned.c \
       02_raii_cleanup.c \
       03_branch_predict.c \
       04_generic_macro.c \
       05_strict_aliasing.c \
       06_safe_overflow.c \
       07_linux_kernel_list.c \
       08_redis_sds_packed.c \
       09_linux_read_write_once.c \
       10_systemd_raii_autoptr.c

TARGETS = $(SRCS:.c=)

.PHONY: all clean run

all: $(TARGETS)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

run: all
	@echo "============================================================"
	@echo "    RUNNING ALL 10 C/C++ CODE LAB TEST SUITES"
	@echo "============================================================"
	@for target in $(TARGETS); do \
		echo ""; \
		./$$target; \
	done

clean:
	rm -f $(TARGETS) /tmp/test_raii_dummy.txt
