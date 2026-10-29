CC ?= gcc
CFLAGS ?= -O2 -Wall -Wextra
TARGET = sensor-telemetry

all: $(TARGET)

$(TARGET): sensor_telemetry.c
	$(CC) $(CFLAGS) -o $(TARGET) sensor_telemetry.c

clean:
	rm -f $(TARGET)

.PHONY: all clean
