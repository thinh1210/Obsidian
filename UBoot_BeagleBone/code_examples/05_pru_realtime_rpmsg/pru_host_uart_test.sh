#!/bin/bash
# ============================================================================
# File: pru_host_uart_test.sh
# Mục đích: Kịch bản điều khiển nhân thời gian thực PRU0 từ giao diện UART Linux
# ============================================================================

set -e

PRU0_RPROC="/sys/class/remoteproc/remoteproc1"
FW_NAME="am335x-pru0-fw"
RPMSG_DEV="/dev/rpmsg_pru30"

echo "================================================================="
echo " KIỂM TRA & GIAO TIẾP VỚI NHÂN THỜI GIAN THỰC PRU0 (200MHz RISC)"
echo "================================================================="

if [ ! -d "$PRU0_RPROC" ]; then
    echo "[!] Không tìm thấy $PRU0_RPROC. Hãy chắc chắn đã bật PRU Overlay trong uEnv.txt!"
    exit 1
fi

echo "[1/4] Dừng nhân PRU0 (nếu đang chạy)..."
echo "stop" > "$PRU0_RPROC/state" 2>/dev/null || true

echo "[2/4] Thiết lập tệp firmware ($FW_NAME) cho PRU0..."
echo "$FW_NAME" > "$PRU0_RPROC/firmware"

echo "[3/4] Khởi chạy nhân PRU0 (start)..."
echo "start" > "$PRU0_RPROC/state"
echo "      -> Trạng thái PRU0 hiện tại: $(cat $PRU0_RPROC/state)"

sleep 1

if [ -c "$RPMSG_DEV" ]; then
    echo "[4/4] Kênh VirtIO RPMsg ($RPMSG_DEV) đã sẵn sàng! Gửi thử 3 gói tin:"
    for i in 1 2 3; do
        echo "Hello_PRU_Packet_$i" > "$RPMSG_DEV"
        head -n 1 "$RPMSG_DEV"
    done
else
    echo "[i] Đã khởi động PRU0 thành công! (Nếu firmware dùng RPMsg, thiết bị $RPMSG_DEV sẽ xuất hiện)."
fi
