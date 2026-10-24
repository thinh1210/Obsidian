# ============================================================================
# Makefile cho ứng dụng chẩn đoán BeagleBone Black (bbb_diag)
# Hỗ trợ cả biên dịch trực tiếp trên BBB, Cross-Compile trên PC, và Yocto BitBake
# ============================================================================

CC ?= gcc
CFLAGS ?= -Wall -Wextra -O2

TARGET = bbb_diag
SRCS = bbb_diag.c
OBJS = $(SRCS:.c=.o)

.PHONY: all clean install

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

install: $(TARGET)
	install -d $(DESTDIR)/usr/bin
	install -m 0755 $(TARGET) $(DESTDIR)/usr/bin/$(TARGET)

clean:
	rm -f $(TARGET) $(OBJS)
