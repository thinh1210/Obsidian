CC = gcc
CFLAGS = -Wall -Wextra -Wpedantic -Wno-unused-function -std=c11 -O2

SRCS = 01_packed_vs_aligned.c \
       02_raii_cleanup.c \
       03_branch_predict.c \
       04_generic_macro.c \
       05_strict_aliasing.c \
       06_safe_overflow.c

TARGETS = $(SRCS:.c=)

.PHONY: all clean run

all: $(TARGETS)

%: %.c
	$(CC) $(CFLAGS) $< -o $@

run: all
	@echo "============================================================"
	@echo "    RUNNING ALL C/C++ CODE LAB TEST SUITES"
	@echo "============================================================"
	@for target in $(TARGETS); do \
		echo ""; \
		./$$target; \
	done

clean:
	rm -f $(TARGETS) /tmp/test_raii_dummy.txt
