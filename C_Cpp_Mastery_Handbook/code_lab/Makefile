CC = gcc
CXX = g++
CFLAGS = -Wall -Wextra -Wpedantic -Wno-unused-function -std=c11 -O2
CXXFLAGS = -Wall -Wextra -std=c++20 -O2

C_SRCS = 01_packed_vs_aligned.c \
         02_raii_cleanup.c \
         03_branch_predict.c \
         04_generic_macro.c \
         05_strict_aliasing.c \
         06_safe_overflow.c \
         07_linux_kernel_list.c \
         08_redis_sds_packed.c \
         09_linux_read_write_once.c \
         10_systemd_raii_autoptr.c

CPP_SRCS = 11_cpp_embedded_keywords.cpp

C_TARGETS = $(C_SRCS:.c=)
CPP_TARGETS = $(CPP_SRCS:.cpp=)
ALL_TARGETS = $(C_TARGETS) $(CPP_TARGETS)

.PHONY: all clean run

all: $(ALL_TARGETS)

$(C_TARGETS): %: %.c
	$(CC) $(CFLAGS) $< -o $@

$(CPP_TARGETS): %: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

run: all
	@echo "============================================================"
	@echo "    RUNNING ALL 11 C/C++ CODE LAB TEST SUITES"
	@echo "============================================================"
	@for target in $(ALL_TARGETS); do \
		echo ""; \
		./$$target; \
	done

clean:
	rm -f $(ALL_TARGETS) /tmp/test_raii_dummy.txt
