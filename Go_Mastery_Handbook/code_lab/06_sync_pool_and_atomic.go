package main

import (
	"bytes"
	"fmt"
	"sync"
	"sync/atomic"
)

const maxPooledBufferCap = 64 * 1024 // Chốt chặn 64KB chống Pool Memory Bloat

var byteBufferPool = sync.Pool{
	New: func() any {
		// Luôn trả về con trỏ *bytes.Buffer để tránh cấp phát Interface Boxing
		return bytes.NewBuffer(make([]byte, 0, 1024))
	},
}

func acquireBuffer() *bytes.Buffer {
	buf := byteBufferPool.Get().(*bytes.Buffer)
	buf.Reset() // Luôn xóa sạch dữ liệu cũ trước khi bàn giao
	return buf
}

func releaseBuffer(buf *bytes.Buffer) {
	// Không đưa các buffer phình quá lớn (>64KB) trở lại Pool (Chuẩn fmt/print.go)
	if buf.Cap() <= maxPooledBufferCap {
		buf.Reset()
		byteBufferPool.Put(buf)
	}
}

func main() {
	fmt.Println("=== [LAB 06] TỐI ƯU HÓA BỘ ĐỆM SYNC.POOL & LOCK-FREE ATOMIC.INT64 ===")

	var totalProcessedBytes atomic.Int64
	var totalRequests atomic.Int64
	var wg sync.WaitGroup

	const numGoroutines = 50
	const loopsPerGoroutine = 200

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func(workerID int) {
			defer wg.Done()
			for j := 0; j < loopsPerGoroutine; j++ {
				buf := acquireBuffer()
				fmt.Fprintf(buf, "worker=%02d_seq=%04d_payload=ok", workerID, j)

				totalProcessedBytes.Add(int64(buf.Len()))
				totalRequests.Add(1)

				releaseBuffer(buf)
			}
		}(i)
	}

	wg.Wait()
	fmt.Printf("  • Tổng số tác vụ đồng thời hoàn tất (atomic.Int64): %d requests\n", totalRequests.Load())
	fmt.Printf("  • Tổng dung lượng xử lý qua sync.Pool             : %d bytes\n", totalProcessedBytes.Load())
}
