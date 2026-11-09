#!/bin/bash
# Wrapper script for Yocto's arm-poky-linux-gnueabi-gdb
# Sets up necessary native sysroot library paths

YOCTO_SYSROOT_X86="/home/thinh/yocto-bbb/build/tmp/sysroots-components/x86_64"
export LD_LIBRARY_PATH="${YOCTO_SYSROOT_X86}/python3-native/usr/lib:${YOCTO_SYSROOT_X86}/ncurses-native/usr/lib:${LD_LIBRARY_PATH}"

GDB_BIN="${YOCTO_SYSROOT_X86}/gdb-cross-arm/usr/bin/arm-poky-linux-gnueabi/arm-poky-linux-gnueabi-gdb"

if [ -f "$GDB_BIN" ]; then
    exec "$GDB_BIN" "$@"
elif which gdb-multiarch >/dev/null 2>&1; then
    exec gdb-multiarch "$@"
else
    echo "Error: Neither Yocto cross-gdb nor gdb-multiarch found!" >&2
    exit 1
fi
