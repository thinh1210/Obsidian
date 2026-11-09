// ============================================================================
// LAB 03: #[repr(packed)] SAFE UNALIGNED ACCESS (&raw const) & VOLATILE MMIO
// Biên dịch: rustc -C opt-level=2 --edition=2021 03_repr_packed_and_volatile.rs
// ============================================================================

use std::mem::{align_of, size_of};
use std::ptr::{read_volatile, write_volatile};

// Khung truyền giao thức cảm biến công nghiệp (Không có byte đệm Padding)
#[repr(C, packed)]
pub struct SensorFramePacked {
    pub start_byte: u8,     // Offset 0 (1 byte)
    pub timestamp_ms: u32,  // Offset 1 (4 bytes - LỆCH BIÊN TỰ NHIÊN!)
    pub measurement: u64,   // Offset 5 (8 bytes - LỆCH BIÊN TỰ NHIÊN!)
    pub crc8: u8,           // Offset 13 (1 byte)
}

// Mô phỏng cụm thanh ghi ngoại vi phần cứng (Memory-Mapped I/O - MMIO)
#[repr(C, align(4))]
pub struct SimulatedTimerMmio {
    pub cr: u32,  // Offset 0x00: Control Register
    pub sr: u32,  // Offset 0x04: Status Register
    pub cnt: u32, // Offset 0x08: Counter Register
}

fn main() {
    println!("=== [LAB 03] #[repr(packed)] (&raw const) & VOLATILE MMIO ===");

    // 1. Kiểm chứng kích thước và độ căn chỉnh của #[repr(C, packed)]
    println!(
        "1. SensorFramePacked: size = {} bytes (1+4+8+1), align = {} byte",
        size_of::<SensorFramePacked>(),
        align_of::<SensorFramePacked>()
    );
    assert_eq!(size_of::<SensorFramePacked>(), 14);
    assert_eq!(align_of::<SensorFramePacked>(), 1);

    let mut frame = SensorFramePacked {
        start_byte: 0xAA,
        timestamp_ms: 0x1234_5678,
        measurement: 0xCAFE_BABE_DEAD_BEEF,
        crc8: 0x55,
    };

    // CẢNH BÁO: Viết `let r = &frame.timestamp_ms;` sẽ gây lỗi biên dịch E0793 (UB do unaligned reference)!
    // Giải pháp chuẩn Rust hiện đại: Dùng `&raw const` và `&raw mut` kết hợp `read_unaligned` / `write_unaligned`
    let ts_ptr: *const u32 = &raw const frame.timestamp_ms;
    let meas_ptr: *mut u64 = &raw mut frame.measurement;

    let ts_val = unsafe { ts_ptr.read_unaligned() };
    unsafe {
        meas_ptr.write_unaligned(0x0102_0304_0506_0708);
    }
    let updated_meas = frame.measurement; // Copy trực tiếp ra biến cục bộ cũng hoàn toàn an toàn!

    println!(
        "2. Unaligned access via &raw const/mut: timestamp = 0x{:08X}, updated_meas = 0x{:016X}",
        ts_val, updated_meas
    );
    assert_eq!(ts_val, 0x1234_5678);
    assert_eq!(updated_meas, 0x0102_0304_0506_0708);

    // 2. Mô phỏng truy cập thanh ghi phần cứng bằng read_volatile / write_volatile
    let mut hw_memory = SimulatedTimerMmio {
        cr: 0,
        sr: 0,
        cnt: 0,
    };
    let mmio_base: *mut SimulatedTimerMmio = &raw mut hw_memory;

    unsafe {
        // Bật bit EN (bit 0) vào thanh ghi điều khiển CR
        write_volatile(&raw mut (*mmio_base).cr, 1 << 0);
        // Phần cứng giả lập cập nhật giá trị bộ đếm CNT và cờ SR
        write_volatile(&raw mut (*mmio_base).cnt, 42_000);
        write_volatile(&raw mut (*mmio_base).sr, 1 << 1); // UIF (Update Interrupt Flag)

        let status = read_volatile(&raw const (*mmio_base).sr);
        let counter = read_volatile(&raw const (*mmio_base).cnt);

        println!(
            "3. Volatile MMIO Register Access: CR = 0x{:02X}, SR = 0x{:02X}, CNT = {}",
            read_volatile(&raw const (*mmio_base).cr),
            status,
            counter
        );
        assert_eq!(status, 2);
        assert_eq!(counter, 42_000);
    }
}
