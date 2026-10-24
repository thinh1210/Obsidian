#!/bin/bash
# ============================================================================
# File: prepare_bbb_sdcard.sh
# Mục đích: Kịch bản chuẩn hóa tạo thẻ nhớ MicroSD khởi động cho BeagleBone Black
# Hỗ trợ 2 chế độ:
#   - Chế độ 1 (WIC Image) : Ghi trực tiếp file .wic sinh ra từ Yocto Project
#   - Chế độ 2 (Thủ công)  : Phân vùng MBR (FAT32 Boot + EXT4 RootFS), sao chép
#                            MLO làm file đầu tiên theo đúng yêu cầu ROM Code AM335x
# ============================================================================

set -e

usage() {
    echo "======================================================================"
    echo " CÔNG CỤ TẠO THẺ NHỚ BOOT CHO BEAGLEBONE BLACK (AN TOÀN & CHUẨN XÁC)"
    echo "======================================================================"
    echo "Cách 1 - Flash trực tiếp ảnh đĩa .wic của Yocto:"
    echo "  sudo $0 wic /dev/sdX <duong_dan_file.wic>"
    echo ""
    echo "Cách 2 - Phân vùng và chép từng thành phần (MLO, u-boot.img, rootfs):"
    echo "  sudo $0 manual /dev/sdX <thu_muc_chua_file_deploy>"
    echo "======================================================================"
    exit 1
}

if [ $# -lt 3 ]; then
    usage
fi

MODE="$1"
DISK="$2"
SRC="$3"

# Kiểm tra an toàn tuyệt đối: Không cho phép ghi đè lên ổ cứng hệ điều hành chính
if [[ "$DISK" == "/dev/sda" || "$DISK" == "/dev/nvme0n1" || "$DISK" == "/dev/vda" ]]; then
    echo "[NGUY HIỂM] Thiết bị $DISK có thể là ổ cứng hệ điều hành chính! Đã hủy lệnh để bảo vệ dữ liệu."
    exit 1
fi

if [ ! -b "$DISK" ]; then
    echo "[LỖI] Thiết bị khối $DISK không tồn tại!"
    exit 1
fi

if [ "$MODE" == "wic" ]; then
    echo "[+] Chế độ WIC: Đang ghi ảnh đĩa $SRC vào thẻ nhớ $DISK..."
    umount "${DISK}"* 2>/dev/null || true
    dd if="$SRC" of="$DISK" bs=4M status=progress conv=fsync
    sync
    echo "[HOÀN TẤT] Thẻ nhớ đã sẵn sàng! Hãy cắm vào BBB, giữ nút S2 và cấp nguồn."
    exit 0
fi

if [ "$MODE" == "manual" ]; then
    echo "[1/6] Tháo gắn kết (unmount) các phân vùng cũ trên $DISK..."
    umount "${DISK}"* 2>/dev/null || true

    echo "[2/6] Xóa bảng phân vùng cũ và tạo bảng phân vùng MBR (msdos)..."
    dd if=/dev/zero of="$DISK" bs=1M count=10 status=none
    parted -s "$DISK" mklabel msdos

    echo "[3/6] Tạo Partition 1 (FAT32, 64MB, bật cờ Boot) & Partition 2 (EXT4, phần còn lại)..."
    parted -s "$DISK" mkpart primary fat32 1MiB 65MiB
    parted -s "$DISK" set 1 boot on
    parted -s "$DISK" mkpart primary ext4 65MiB 100%
    partprobe "$DISK"
    sleep 2

    # Xác định tên phân vùng (/dev/sdb1 hay /dev/mmcblk0p1)
    if [[ "$DISK" == *"mmcblk"* || "$DISK" == *"loop"* ]]; then
        PART1="${DISK}p1"
        PART2="${DISK}p2"
    else
        PART1="${DISK}1"
        PART2="${DISK}2"
    fi

    echo "[4/6] Định dạng FAT32 (BOOT) và EXT4 (ROOTFS)..."
    mkfs.vfat -F 32 -n "BOOT" "$PART1"
    mkfs.ext4 -F -L "ROOTFS" "$PART2"

    MNT_BOOT=$(mktemp -d)
    MNT_ROOT=$(mktemp -d)
    mount "$PART1" "$MNT_BOOT"
    mount "$PART2" "$MNT_ROOT"

    echo "[5/6] Sao chép MLO đầu tiên (Quy tắc bắt buộc của AM335x ROM Code)..."
    cp "$SRC/MLO" "$MNT_BOOT/MLO"
    sync
    cp "$SRC/u-boot.img" "$MNT_BOOT/u-boot.img"
    [ -f "$SRC/zImage" ] && cp "$SRC/zImage" "$MNT_BOOT/"
    [ -f "$SRC/am335x-boneblack.dtb" ] && cp "$SRC/am335x-boneblack.dtb" "$MNT_BOOT/"
    [ -f "$SRC/uEnv.txt" ] && cp "$SRC/uEnv.txt" "$MNT_BOOT/"
    sync

    echo "[6/6] Giải nén Root Filesystem vào phân vùng 2 (EXT4)..."
    ROOTFS_TAR=$(ls "$SRC"/*.rootfs.tar.bz2 "$SRC"/*.rootfs.tar.gz 2>/dev/null | head -n 1 || true)
    if [ -n "$ROOTFS_TAR" ]; then
        tar -xf "$ROOTFS_TAR" -C "$MNT_ROOT"
        sync
    fi

    umount "$MNT_BOOT"
    umount "$MNT_ROOT"
    rmdir "$MNT_BOOT" "$MNT_ROOT"
    echo "[HOÀN TẤT] Thẻ nhớ khởi động BeagleBone Black đã được tạo thành công!"
fi
