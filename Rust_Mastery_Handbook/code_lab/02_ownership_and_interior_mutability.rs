// ============================================================================
// LAB 02: OWNERSHIP, BORROW CHECKER, CELL, REFCELL & RC / ARC
// Biên dịch: rustc -C opt-level=2 --edition=2021 02_ownership_and_interior_mutability.rs
// ============================================================================

use std::cell::{Cell, RefCell};
use std::mem::size_of;
use std::rc::Rc;
use std::sync::Arc;

pub struct TelemetryNode {
    pub id: u32,
    // Cell<T>: Đột biến nội tại tốn 0 byte phụ phí cho kiểu Copy
    pub packet_count: Cell<u32>,
    // RefCell<T>: Kiểm tra quy tắc Aliasing XOR Mutability tại Runtime
    pub error_logs: RefCell<Vec<String>>,
}

impl TelemetryNode {
    pub fn new(id: u32) -> Self {
        Self {
            id,
            packet_count: Cell::new(0),
            error_logs: RefCell::new(Vec::new()),
        }
    }

    // Lưu ý: Hàm này chỉ nhận tham chiếu bất biến `&self`, nhưng vẫn cập nhật được trạng thái!
    pub fn record_event(&self, maybe_err: Option<&str>) {
        self.packet_count.set(self.packet_count.get() + 1);
        if let Some(err_msg) = maybe_err {
            self.error_logs.borrow_mut().push(err_msg.to_string());
        }
    }
}

fn main() {
    println!("=== [LAB 02] OWNERSHIP, BORROWING & INTERIOR MUTABILITY ===");

    // 1. Kiểm chứng Cell<T> có kích thước đúng bằng T (Zero space overhead)
    assert_eq!(size_of::<Cell<u32>>(), size_of::<u32>());
    println!(
        "1. Cell<u32> overhead check: size_of::<Cell<u32>>() = {} bytes (Zero overhead!)",
        size_of::<Cell<u32>>()
    );

    // 2. Chia sẻ quyền sở hữu trong cùng 1 thread bằng Rc<TelemetryNode>
    let shared_node = Rc::new(TelemetryNode::new(101));
    let observer_a = Rc::clone(&shared_node);
    let observer_b = Rc::clone(&shared_node);

    println!(
        "2. Rc strong_count after 2 clones: {}",
        Rc::strong_count(&shared_node)
    );
    assert_eq!(Rc::strong_count(&shared_node), 3);

    // Cả 2 observer cùng cập nhật dữ liệu thông qua tham chiếu chia sẻ `&TelemetryNode`
    observer_a.record_event(None);
    observer_b.record_event(Some("CRC_MISMATCH_0x2A"));
    observer_a.record_event(Some("TIMEOUT_UART1"));

    println!(
        "3. Interior Mutability via &self: packet_count = {}, logs = {:?}",
        shared_node.packet_count.get(),
        shared_node.error_logs.borrow()
    );
    assert_eq!(shared_node.packet_count.get(), 3);
    assert_eq!(shared_node.error_logs.borrow().len(), 2);

    // 3. Kiểm chứng Runtime Borrow Checker của RefCell bằng try_borrow_mut()
    {
        let _active_reader = shared_node.error_logs.borrow();
        // Khi đang có người đọc (_active_reader), việc mượn ghi (try_borrow_mut) sẽ bị từ chối an toàn:
        let try_writer = shared_node.error_logs.try_borrow_mut();
        println!(
            "4. RefCell runtime safety check while shared borrow is active: try_borrow_mut().is_err() = {}",
            try_writer.is_err()
        );
        assert!(try_writer.is_err());
    } // _active_reader kết thúc tại đây (Drop Ref)

    // Bây giờ mượn ghi lại thành công!
    assert!(shared_node.error_logs.try_borrow_mut().is_ok());

    // 4. Kiểm chứng Arc<T> cho chia sẻ đa luồng
    let arc_config = Arc::new(vec![115_200u32, 921_600u32]);
    let arc_clone = Arc::clone(&arc_config);
    let handle = std::thread::spawn(move || arc_clone[1]);
    let high_baud = handle.join().unwrap();
    println!("5. Arc<T> shared across OS thread successfully: baudrate = {high_baud}");
    assert_eq!(high_baud, 921_600);
}
