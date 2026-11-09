package main

import (
	"errors"
	"fmt"
	"strings"
)

// Thiết kế Bitmask quyền hạn hệ thống bằng iota kết hợp dịch bit (1 << iota)
type AccessFlag uint8

const (
	FlagRead AccessFlag = 1 << iota // 1 << 0 = 1 (0b0001)
	FlagWrite                       // 1 << 1 = 2 (0b0010)
	FlagExec                        // 1 << 2 = 4 (0b0100)
	FlagSudo                        // 1 << 3 = 8 (0b1000)
)

func (f AccessFlag) String() string {
	var perms []string
	if f&FlagRead != 0 {
		perms = append(perms, "READ")
	}
	if f&FlagWrite != 0 {
		perms = append(perms, "WRITE")
	}
	if f&FlagExec != 0 {
		perms = append(perms, "EXEC")
	}
	if f&FlagSudo != 0 {
		perms = append(perms, "SUDO")
	}
	return "[" + strings.Join(perms, " | ") + "]"
}

// Minh họa defer can thiệp và bọc ngữ cảnh vào Named Return Value (res, err)
func executeTransaction(amount int) (finalAmount int, err error) {
	stage := "START"

	// Đối số 'stage' truyền trực tiếp được đánh giá NGAY TẠI DÒNG NÀY (= "START")
	defer func(capturedAtRegister string) {
		fmt.Printf("  [Defer 1 - Chạy cuối LIFO] Tham số chụp lúc đăng ký = %q, nhưng biến stage hiện tại = %q\n",
			capturedAtRegister, stage)
		if err != nil {
			// Bọc thêm thông tin ngữ cảnh vào biến trả về có tên 'err'
			err = fmt.Errorf("transaction aborted at stage=%s: %w", stage, err)
		} else {
			// Cộng thêm thưởng 10 đơn vị vào biến trả về có tên 'finalAmount'
			finalAmount += 10
		}
	}(stage)

	stage = "VALIDATION"
	defer fmt.Println("  [Defer 2 - Chạy trước LIFO] Đã đi qua bước kiểm tra hợp lệ")

	if amount <= 0 {
		return 0, errors.New("invalid negative or zero amount")
	}
	stage = "COMMIT"
	return amount, nil // Gán finalAmount = amount, sau đó chạy Defer 2 -> Defer 1 -> RET!
}

func main() {
	fmt.Println("=== [LAB 05] CƠ CHẾ DEFER EVALUATION, NAMED RETURN & IOTA BITMASK ===")

	fmt.Println("\n1. Kiểm tra đánh giá đối số Defer & sửa Named Return Value:")
	val, err := executeTransaction(100)
	fmt.Printf("  => Kết quả giao dịch hợp lệ (gốc 100, defer +10): val=%d, err=%v\n\n", val, err)

	_, errFail := executeTransaction(-50)
	fmt.Printf("  => Kết quả giao dịch lỗi (được defer tự bọc lỗi): err=%v\n", errFail)

	fmt.Println("\n2. Kiểm tra toán tử Bitwise với hằng số iota Bitmask:")
	userRole := FlagRead | FlagWrite | FlagExec
	fmt.Printf("  • Quyền ban đầu (0b%04b)       : %s\n", userRole, userRole)
	userRole &^= FlagWrite // Toán tử AND NOT (&^) đặc sản của Go: Xóa bit FlagWrite!
	fmt.Printf("  • Sau khi xóa bit WRITE (&^)   : %s (Có quyền EXEC = %v)\n",
		userRole, userRole&FlagExec != 0)
}
