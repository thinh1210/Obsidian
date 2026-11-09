package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

// Biểu diễn cấu trúc nội tạng 16-byte của runtime.iface để quan sát trực tiếp
type runtimeIface struct {
	tab  uintptr
	data uintptr
}

type CustomError struct {
	Code    int
	Message string
}

func (e *CustomError) Error() string {
	if e == nil {
		return "<nil CustomError pointer>"
	}
	return fmt.Sprintf("code=%d: %s", e.Code, e.Message)
}

// BẪY KINH ĐIỂN: Trả về biến con trỏ cụ thể (*CustomError)(nil) qua kiểu interface 'error'
func validateBad(input int) error {
	var err *CustomError = nil
	if input < 0 {
		err = &CustomError{Code: 400, Message: "input must be non-negative"}
	}
	return err // Boxing (*CustomError, nil) vào runtime.iface -> tab != 0!
}

// CHUẨN SẢN XUẤT: Trả về trực tiếp untyped 'nil' khi không có lỗi
func validateGood(input int) error {
	if input < 0 {
		return &CustomError{Code: 400, Message: "input must be non-negative"}
	}
	return nil // Cả tab == 0 và data == 0
}

// Hàm kiểm tra an toàn cả nil interface lẫn typed nil pointer bên trong interface
func isEffectivelyNil(v any) bool {
	if v == nil {
		return true
	}
	rv := reflect.ValueOf(v)
	switch rv.Kind() {
	case reflect.Ptr, reflect.Map, reflect.Slice, reflect.Chan, reflect.Func, reflect.UnsafePointer:
		return rv.IsNil()
	}
	return false
}

func inspectError(label string, err error) {
	raw := *(*runtimeIface)(unsafe.Pointer(&err))
	fmt.Printf("  [%s]\n", label)
	fmt.Printf("    • err == nil             : %v\n", err == nil)
	fmt.Printf("    • isEffectivelyNil(err)  : %v\n", isEffectivelyNil(err))
	fmt.Printf("    • runtime.iface layout   : tab=0x%x, data=0x%x\n", raw.tab, raw.data)
}

func main() {
	fmt.Println("=== [LAB 01] GIẢI PHẪU BẪY TYPED NIL INTERFACE != NIL ===")

	errBad := validateBad(100)   // input=100 hợp lệ nhưng trả về typed nil
	errGood := validateGood(100) // input=100 hợp lệ và trả về nil chuẩn

	inspectError("validateBad(100)  -> return (*CustomError)(nil)", errBad)
	inspectError("validateGood(100) -> return nil", errGood)
}
