package main

import (
	"fmt"
	"unsafe"
)

// CÁCH SẮP XẾP TỆ: Đan xen kiểu 1-byte và 8-byte gây lãng phí Padding
type BadStruct struct {
	FlagA   bool  // 1B + 7B padding
	Counter int64 // 8B
	FlagB   byte  // 1B + 3B padding
	Code    int32 // 4B
} // Tổng: 24 bytes

// CÁCH SẮP XẾP TỐI ƯU: Xếp giảm dần theo kích thước (8B -> 4B -> 1B -> 1B)
type GoodStruct struct {
	Counter int64 // 8B
	Code    int32 // 4B
	FlagA   bool  // 1B
	FlagB   byte  // 1B + 2B tail padding
} // Tổng: 16 bytes (Tiết kiệm 33.3% bộ nhớ!)

// Chuyển đổi Zero-Copy từ []byte sang string (Chuẩn Go 1.20+ như trong strings.Builder)
func BytesToStringZeroCopy(b []byte) string {
	if len(b) == 0 {
		return ""
	}
	return unsafe.String(unsafe.SliceData(b), len(b))
}

// Chuyển đổi Zero-Copy từ string sang []byte (CHỈ ĐỌC - Read-Only!)
func StringToBytesZeroCopy(s string) []byte {
	if s == "" {
		return nil
	}
	return unsafe.Slice(unsafe.StringData(s), len(s))
}

func main() {
	fmt.Println("=== [LAB 03] STRUCT PADDING ALIGNMENT & UNSAFE ZERO-COPY ===")

	var bad BadStruct
	var good GoodStruct

	fmt.Printf("1. Khảo sát Struct Padding & Alignment:\n")
	fmt.Printf("  • BadStruct  : Sizeof=%2d bytes, Alignof=%d | Offsets: FlagA=%d, Counter=%d, FlagB=%d, Code=%d\n",
		unsafe.Sizeof(bad), unsafe.Alignof(bad),
		unsafe.Offsetof(bad.FlagA), unsafe.Offsetof(bad.Counter),
		unsafe.Offsetof(bad.FlagB), unsafe.Offsetof(bad.Code))

	fmt.Printf("  • GoodStruct : Sizeof=%2d bytes, Alignof=%d | Offsets: Counter=%d, Code=%d, FlagA=%d, FlagB=%d\n",
		unsafe.Sizeof(good), unsafe.Alignof(good),
		unsafe.Offsetof(good.Counter), unsafe.Offsetof(good.Code),
		unsafe.Offsetof(good.FlagA), unsafe.Offsetof(good.FlagB))

	fmt.Printf("\n2. Kiểm chứng Zero-Copy []byte <-> string (Cùng địa chỉ vật lý):\n")
	rawBytes := []byte("High-Performance Go Runtime")
	zeroStr := BytesToStringZeroCopy(rawBytes)
	backToBytes := StringToBytesZeroCopy(zeroStr)

	ptrOrig := unsafe.SliceData(rawBytes)
	ptrStr := unsafe.StringData(zeroStr)
	ptrBack := unsafe.SliceData(backToBytes)

	fmt.Printf("  • Địa chỉ mảng gốc []byte     : %p\n", ptrOrig)
	fmt.Printf("  • Địa chỉ vùng nhớ string     : %p (Zero-Copy = %v)\n", ptrStr, ptrOrig == ptrStr)
	fmt.Printf("  • Địa chỉ []byte đọc ngược lại: %p (Zero-Copy = %v)\n", ptrBack, ptrOrig == ptrBack)
}
