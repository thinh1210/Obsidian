// ============================================================================
// LAB 01: MEMORY LAYOUT (#[repr(Rust)] vs #[repr(C)]) & NICHE OPTIMIZATION
// Biên dịch: rustc -C opt-level=2 --edition=2021 01_memory_layout_and_niche.rs
// ============================================================================

use std::mem::{align_of, offset_of, size_of};
use std::num::NonZeroU32;
use std::ptr::NonNull;

// 1. Struct theo chuẩn C: Giữ nguyên thứ tự trường -> Tốn 24 bytes vì Padding
#[repr(C)]
pub struct CLayoutStruct {
    pub a: u8,  // 1B + 7B padding
    pub b: u64, // 8B
    pub c: u8,  // 1B + 1B padding
    pub d: u16, // 2B
    pub e: u32, // 4B
}

// 2. Struct mặc định của Rust (#[repr(Rust)]): Tự động đảo thứ tự trường tối ưu!
pub struct RustLayoutStruct {
    pub a: u8,
    pub b: u64,
    pub c: u8,
    pub d: u16,
    pub e: u32,
}

// 3. Zero-Sized Type (ZST)
pub struct ZeroSizedMarker;

fn main() {
    println!("=== [LAB 01] MEMORY LAYOUT & NICHE OPTIMIZATION ===");

    println!(
        "1. #[repr(C)] Struct    : size = {:2} bytes, align = {} bytes",
        size_of::<CLayoutStruct>(),
        align_of::<CLayoutStruct>()
    );
    println!(
        "   Offsets in #[repr(C)]: a={}, b={}, c={}, d={}, e={}",
        offset_of!(CLayoutStruct, a),
        offset_of!(CLayoutStruct, b),
        offset_of!(CLayoutStruct, c),
        offset_of!(CLayoutStruct, d),
        offset_of!(CLayoutStruct, e)
    );

    println!(
        "2. #[repr(Rust)] Struct : size = {:2} bytes, align = {} bytes (Saved 8 bytes of padding!)",
        size_of::<RustLayoutStruct>(),
        align_of::<RustLayoutStruct>()
    );
    println!(
        "   Offsets in #[repr(Rust)]: a={}, b={}, c={}, d={}, e={}",
        offset_of!(RustLayoutStruct, a),
        offset_of!(RustLayoutStruct, b),
        offset_of!(RustLayoutStruct, c),
        offset_of!(RustLayoutStruct, d),
        offset_of!(RustLayoutStruct, e)
    );

    assert_eq!(size_of::<CLayoutStruct>(), 24);
    assert_eq!(size_of::<RustLayoutStruct>(), 16);

    // Kiểm chứng Zero-Sized Types (ZST)
    assert_eq!(size_of::<ZeroSizedMarker>(), 0);
    assert_eq!(size_of::<[ZeroSizedMarker; 10_000]>(), 0);
    println!(
        "3. Zero-Sized Type (ZST): size_of::<[ZeroSizedMarker; 10_000]>() = {} bytes",
        size_of::<[ZeroSizedMarker; 10_000]>()
    );

    // Kiểm chứng Niche Optimization (Tối ưu hóa hốc trống)
    println!("4. Niche Optimization Verification:");
    println!(
        "   - size_of::<&u32>()               = {} bytes | size_of::<Option<&u32>>()               = {} bytes",
        size_of::<&u32>(),
        size_of::<Option<&u32>>()
    );
    println!(
        "   - size_of::<Box<u64>>()           = {} bytes | size_of::<Option<Box<u64>>>()           = {} bytes",
        size_of::<Box<u64>>(),
        size_of::<Option<Box<u64>>>()
    );
    println!(
        "   - size_of::<NonNull<u8>>()        = {} bytes | size_of::<Option<NonNull<u8>>>()        = {} bytes",
        size_of::<NonNull<u8>>(),
        size_of::<Option<NonNull<u8>>>()
    );
    println!(
        "   - size_of::<NonZeroU32>()         = {} bytes | size_of::<Option<NonZeroU32>>()         = {} bytes",
        size_of::<NonZeroU32>(),
        size_of::<Option<NonZeroU32>>()
    );
    println!(
        "   - size_of::<u32>() (No niche)     = {} bytes | size_of::<Option<u32>>() (Needs tag)    = {} bytes",
        size_of::<u32>(),
        size_of::<Option<u32>>()
    );
    println!(
        "   - size_of::<String>()             = {} bytes | size_of::<Option<String>>()             = {} bytes",
        size_of::<String>(),
        size_of::<Option<String>>()
    );

    assert_eq!(size_of::<Option<&u32>>(), size_of::<&u32>());
    assert_eq!(size_of::<Option<Box<u64>>>(), size_of::<Box<u64>>());
    assert_eq!(size_of::<Option<NonZeroU32>>(), size_of::<NonZeroU32>());
    assert_eq!(size_of::<Option<String>>(), size_of::<String>());
    assert_eq!(size_of::<Option<bool>>(), 1);
    println!("   -> [PASS] Niche Optimization verified with 0 bytes overhead!");
}
