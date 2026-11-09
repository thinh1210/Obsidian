// ============================================================================
// LAB 05: MAYBEUNINIT<T> SAFE INITIALIZATION & EXTERN "C" FFI ABI
// Biên dịch: rustc -C opt-level=2 --edition=2021 05_maybe_uninit_and_unsafe_ffi.rs
// ============================================================================

use std::mem::MaybeUninit;

// 1. Hàm viết theo chuẩn ABI của C (có thể được gọi từ C/C++ hoặc truyền làm callback)
#[no_mangle]
pub unsafe extern "C" fn c_abi_fill_dma_buffer(
    dst_ptr: *mut u32,
    count: usize,
    seed: u32,
) -> i32 {
    if dst_ptr.is_null() || count == 0 {
        return -1;
    }
    for i in 0..count {
        // Ghi trực tiếp vào vùng nhớ chưa khởi tạo mà KHÔNG giải tham chiếu tạo `&mut u32`!
        unsafe {
            dst_ptr.add(i).write(seed + (i as u32) * 10);
        }
    }
    0
}

// 2. Sử dụng MaybeUninit<T> để khởi tạo bộ đệm không tốn chi phí gán 0 thừa
pub fn receive_dma_burst<const N: usize>(seed: u32) -> Result<[u32; N], i32> {
    // Tạo mảng N phần tử chưa khởi tạo trên Stack (Tốn 0 chu kỳ CPU!)
    let mut uninit_buf: [MaybeUninit<u32>; N] = [const { MaybeUninit::uninit() }; N];

    // Lấy con trỏ thô *mut u32 truyền xuống hàm chuẩn C FFI
    let first_elem_ptr = uninit_buf.as_mut_ptr() as *mut u32;
    let status = unsafe { c_abi_fill_dma_buffer(first_elem_ptr, N, seed) };
    if status != 0 {
        return Err(status);
    }

    // Chuyển đổi an toàn sang mảng [u32; N] sau khi C FFI đã điền đủ N phần tử
    // SAFETY: `c_abi_fill_dma_buffer` trả về 0 đảm bảo toàn bộ N phần tử đã được ghi hợp lệ.
    let initialized: [u32; N] = unsafe {
        (&raw const uninit_buf as *const [u32; N]).read()
    };
    Ok(initialized)
}

fn main() {
    println!("=== [LAB 05] MAYBEUNINIT<T> & EXTERN \"C\" FFI INTEROP ===");

    // 1. Kiểm chứng khởi tạo đơn lẻ bằng MaybeUninit
    let mut single_slot: MaybeUninit<String> = MaybeUninit::uninit();
    single_slot.write(String::from("Zero-Cost Safe Init!"));
    // SAFETY: Vừa gọi `.write()` ở dòng trên.
    let valid_str: String = unsafe { single_slot.assume_init() };
    println!("1. Single MaybeUninit<String> initialized: \"{valid_str}\"");
    assert_eq!(valid_str, "Zero-Cost Safe Init!");

    // 2. Kiểm chứng khởi tạo mảng qua hàm extern "C" FFI
    let dma_data: [u32; 6] = receive_dma_burst::<6>(100).expect("DMA transfer failed");
    println!("2. Array initialized via extern \"C\" FFI & MaybeUninit: {:?}", dma_data);
    assert_eq!(dma_data, [100, 110, 120, 130, 140, 150]);

    // 3. Kiểm tra xử lý lỗi con trỏ NULL qua FFI
    let err_code = unsafe { c_abi_fill_dma_buffer(std::ptr::null_mut(), 6, 100) };
    println!("3. Null pointer guard in extern \"C\" fn returned: {err_code}");
    assert_eq!(err_code, -1);
}
