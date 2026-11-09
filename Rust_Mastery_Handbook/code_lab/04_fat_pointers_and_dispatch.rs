// ============================================================================
// LAB 04: FAT POINTERS (16 BYTES) & STATIC VS DYNAMIC DISPATCH
// Biên dịch: rustc -C opt-level=2 --edition=2021 04_fat_pointers_and_dispatch.rs
// ============================================================================

use std::mem::{ size_of, transmute };

pub trait BusDriver {
    fn bus_name(&self) -> &'static str;
    fn transfer_rate_kbps(&self) -> u32;
}

pub struct SpiBus {
    pub clock_mhz: u32,
}

impl BusDriver for SpiBus {
    fn bus_name(&self) -> &'static str {
        "SPI_MASTER_DMA"
    }
    fn transfer_rate_kbps(&self) -> u32 {
        self.clock_mhz * 1000
    }
}

pub struct I2cBus {
    pub fast_mode_plus: bool,
}

impl BusDriver for I2cBus {
    fn bus_name(&self) -> &'static str {
        "I2C_TWI_BUS"
    }
    fn transfer_rate_kbps(&self) -> u32 {
        if self.fast_mode_plus { 1000 } else { 400 }
    }
}

// 1. Static Dispatch (Monomorphization): Thin pointer (8 bytes), Inlined!
#[inline(always)]
pub fn query_bus_static<B: BusDriver>(bus: &B) -> u32 {
    bus.transfer_rate_kbps()
}

// 2. Dynamic Dispatch (Trait Object): Fat pointer (16 bytes: data_ptr + vtable_ptr)
#[inline(never)]
pub fn query_bus_dynamic(bus: &dyn BusDriver) -> u32 {
    bus.transfer_rate_kbps()
}

fn main() {
    println!("=== [LAB 04] FAT POINTERS (16-BYTE) & DISPATCH MECHANISMS ===");

    // 1. So sánh kích thước Thin Pointers (8B) và Fat Pointers (16B) trên kiến trúc 64-bit
    println!("1. Pointer Size Comparison (64-bit Architecture):");
    println!("   - Thin Pointer (&u8 / &SpiBus)   : {:2} bytes", size_of::<&SpiBus>());
    println!("   - Slice Fat Pointer (&[u8])      : {:2} bytes (data_ptr + len)", size_of::<&[u8]>());
    println!("   - String Slice Fat Pointer (&str): {:2} bytes (data_ptr + len)", size_of::<&str>());
    println!("   - Trait Object (&dyn BusDriver)  : {:2} bytes (data_ptr + vtable_ptr)", size_of::<&dyn BusDriver>());

    assert_eq!(size_of::<&SpiBus>(), 8);
    assert_eq!(size_of::<&[u8]>(), 16);
    assert_eq!(size_of::<&str>(), 16);
    assert_eq!(size_of::<&dyn BusDriver>(), 16);

    // 2. Giải phẫu cấu trúc bên trong của Slice Fat Pointer `&[u8]`
    let buffer: [u8; 5] = [10, 20, 30, 40, 50];
    let slice_ref: &[u8] = &buffer[1..4]; // Gồm 3 phần tử: [20, 30, 40]
    let (raw_data_ptr, raw_len): (usize, usize) = unsafe { transmute(slice_ref) };
    println!(
        "2. Dissecting Slice `&buffer[1..4]`: data_ptr = 0x{:X}, len = {} elements",
        raw_data_ptr, raw_len
    );
    assert_eq!(raw_data_ptr, (&raw const buffer[1]) as usize);
    assert_eq!(raw_len, 3);

    // 3. Giải phẫu cấu trúc bên trong của Trait Object `&dyn BusDriver`
    let spi = SpiBus { clock_mhz: 48 };
    let i2c = I2cBus { fast_mode_plus: true };

    let dyn_spi: &dyn BusDriver = &spi;
    let (spi_data_ptr, spi_vtable_ptr): (usize, usize) = unsafe { transmute(dyn_spi) };

    // Cấu trúc chuẩn của vtable ở đầu luôn là: [drop_in_place, size, align, ...]
    let vtable_header = spi_vtable_ptr as *const usize;
    let recorded_size = unsafe { *vtable_header.add(1) };
    let recorded_align = unsafe { *vtable_header.add(2) };
    println!(
        "3. Dissecting `&dyn BusDriver`: data_ptr = 0x{:X}, vtable_ptr = 0x{:X} (vtable records size={}B, align={}B)",
        spi_data_ptr, spi_vtable_ptr, recorded_size, recorded_align
    );
    assert_eq!(spi_data_ptr, (&raw const spi) as usize);
    assert_eq!(recorded_size, size_of::<SpiBus>());
    assert_eq!(recorded_align, std::mem::align_of::<SpiBus>());

    // 4. Thực thi Static Dispatch vs Dynamic Dispatch trên mảng hỗn hợp
    let static_rate = query_bus_static(&spi) + query_bus_static(&i2c);
    let buses: [&dyn BusDriver; 2] = [&spi, &i2c];
    let mut dynamic_rate = 0;
    for b in buses {
        println!("   -> Dynamic call on [{}]: {} kbps", b.bus_name(), query_bus_dynamic(b));
        dynamic_rate += query_bus_dynamic(b);
    }
    assert_eq!(static_rate, dynamic_rate);
    assert_eq!(dynamic_rate, 49_000);
}
