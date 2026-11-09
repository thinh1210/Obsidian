package main

import (
	"fmt"
	"unsafe"
)

type sliceHeader struct {
	Data uintptr
	Len  int
	Cap  int
}

func inspectSlice(name string, s []int) {
	h := (*sliceHeader)(unsafe.Pointer(&s))
	fmt.Printf("  %-24s: val=%-18v | len=%d, cap=%d | backing_array=0x%x\n",
		name, s, h.Len, h.Cap, h.Data)
}

func main() {
	fmt.Println("=== [LAB 02] SLICE BACKING ARRAY & FULL SLICE EXPRESSION a[low:high:max] ===")

	// 1. Minh họa tai nạn ghi đè mảng nền khi cắt 2 chỉ số thông thường a[low:high]
	fmt.Println("\n1. Cắt 2 chỉ số thông thường (parent[0:2]) -> Ghi đè ngoài ý muốn:")
	parent1 := []int{10, 20, 30, 40}
	childNormal := parent1[0:2] // len=2, nhưng cap vẫn = 4!
	inspectSlice("parent1 (trước)", parent1)
	inspectSlice("childNormal := p[0:2]", childNormal)

	childNormal = append(childNormal, 999) // Ghi đè thẳng vào parent1[2]!
	inspectSlice("childNormal (sau append)", childNormal)
	inspectSlice("parent1 (BỊ GHI ĐÈ!)", parent1)

	// 2. Giải pháp cô lập vùng nhớ bằng Full Slice Expression a[low:high:max]
	fmt.Println("\n2. Cắt 3 chỉ số Full Slice (parent2[0:2:2]) -> Khóa cap=2, tự tách mảng mới:")
	parent2 := []int{10, 20, 30, 40}
	childSafe := parent2[0:2:2] // len=2, cap=2 (khóa chặt cap == len)
	inspectSlice("parent2 (trước)", parent2)
	inspectSlice("childSafe := p[0:2:2]", childSafe)

	childSafe = append(childSafe, 888) // Vì len==cap (2==2), buộc cấp phát mảng nền mới!
	inspectSlice("childSafe (mảng mới)", childSafe)
	inspectSlice("parent2 (AN TOÀN 100%)", parent2)
}
