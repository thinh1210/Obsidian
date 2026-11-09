// ============================================================================
// LAB 06: FEARLESS CONCURRENCY (SCOPED THREADS, ATOMICS & MUTEX)
// Biên dịch: rustc -C opt-level=2 --edition=2021 06_fearless_concurrency_atomics.rs
// ============================================================================

use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::sync::Mutex;
use std::thread;

fn main() {
    println!("=== [LAB 06] FEARLESS CONCURRENCY: SCOPED THREADS & ATOMICS ===");

    // 1. std::thread::scope: Chia mảng trên Stack cho 4 luồng xử lý song song mà KHÔNG CẦN Arc hay Vec::clone!
    let mut sensor_samples: [u32; 8] = [1, 2, 3, 4, 5, 6, 7, 8];
    let atomic_total_sum = AtomicUsize::new(0);
    let log_mutex = Mutex::new(Vec::<String>::new());

    thread::scope(|s| {
        // Cắt mảng khả biến trên Stack thành 4 lát cắt độc lập (Disjoint mutable slices)
        for (worker_id, chunk) in sensor_samples.chunks_mut(2).enumerate() {
            let sum_ref = &atomic_total_sum;
            let log_ref = &log_mutex;

            s.spawn(move || {
                // Mỗi luồng nhân đôi phần tử trong lát cắt của riêng mình
                let mut local_sum = 0usize;
                for val in chunk.iter_mut() {
                    *val *= 10;
                    local_sum += *val as usize;
                }

                // Cộng dồn không khóa (Lock-free) bằng AtomicUsize
                sum_ref.fetch_add(local_sum, Ordering::Relaxed);

                // Ghi nhận hoàn thành qua Mutex<Vec<String>>
                log_ref
                    .lock()
                    .unwrap()
                    .push(format!("Worker #{worker_id} processed {chunk:?}"));
            });
        }
    }); // Toàn bộ 4 luồng tự động join tại đây trước khi bước sang dòng tiếp theo!

    println!("1. Mutated stack array in-place across 4 scoped threads: {:?}", sensor_samples);
    println!("2. Lock-free AtomicUsize total sum: {}", atomic_total_sum.load(Ordering::Relaxed));
    assert_eq!(sensor_samples, [10, 20, 30, 40, 50, 60, 70, 80]);
    assert_eq!(atomic_total_sum.load(Ordering::Relaxed), 360);
    assert_eq!(log_mutex.lock().unwrap().len(), 4);

    // 2. Minh họa đồng bộ hóa Producer - Consumer bằng Acquire / Release Memory Ordering
    let mut shared_payload: u64 = 0;
    let ready_flag = AtomicBool::new(false);
    let payload_raw_ptr = (&raw mut shared_payload) as usize;

    thread::scope(|s| {
        let flag_ref = &ready_flag;
        // Producer Thread
        s.spawn(move || {
            unsafe {
                *(payload_raw_ptr as *mut u64) = 0xDEAD_BEEF_CAFE_2026;
            }
            // Release đảm bảo lệnh ghi payload ở trên PHẢI hoàn tất trước khi cờ ready_flag = true!
            flag_ref.store(true, Ordering::Release);
        });

        // Consumer Thread
        let observed = s
            .spawn(move || {
                // Acquire đảm bảo mọi lệnh đọc sau vòng lặp này nhìn thấy toàn bộ dữ liệu trước Release!
                while !flag_ref.load(Ordering::Acquire) {
                    std::hint::spin_loop();
                }
                unsafe { *(payload_raw_ptr as *const u64) }
            })
            .join()
            .unwrap();

        println!(
            "3. Acquire/Release Synchronization verified: Consumer read 0x{:016X}",
            observed
        );
        assert_eq!(observed, 0xDEAD_BEEF_CAFE_2026);
    });
}
