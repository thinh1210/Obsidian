#!/bin/bash
# Wrapper script for Yocto ARM GCC
YOCTO_NATIVE_BIN="/home/thinh/yocto-bbb/build/tmp/work/cortexa8hf-neon-poky-linux-gnueabi/my-app/1.0/recipe-sysroot-native/usr/bin/arm-poky-linux-gnueabi"
GCC_BIN="${YOCTO_NATIVE_BIN}/arm-poky-linux-gnueabi-gcc"
SYSROOT="/home/thinh/yocto-bbb/build/tmp/work/cortexa8hf-neon-poky-linux-gnueabi/my-app/1.0/recipe-sysroot"

if [ -f "$GCC_BIN" ]; then
    export PATH="${YOCTO_NATIVE_BIN}:${PATH}"
    exec "$GCC_BIN" -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a8 --sysroot="$SYSROOT" "$@"
elif which arm-linux-gnueabihf-gcc >/dev/null 2>&1; then
    exec arm-linux-gnueabihf-gcc "$@"
else
    echo "Error: Cross-compiler arm-gcc not found!" >&2
    exit 1
fi
