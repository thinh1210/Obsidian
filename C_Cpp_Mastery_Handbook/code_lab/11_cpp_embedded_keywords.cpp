/**
 * 11_cpp_embedded_keywords.cpp - Thực nghiệm toàn bộ từ khóa C++ đặc biệt cho kỹ sư C
 * Biên dịch: g++ -std=c++20 -Wall -Wextra 11_cpp_embedded_keywords.cpp -o 11_cpp_embedded_keywords
 */

#include <iostream>
#include <concepts>
#include <cstdint>

// 1. explicit: Ngăn ngừa ép kiểu ngầm định
class SafeBuffer {
private:
    size_t m_size;
public:
    explicit SafeBuffer(size_t size) : m_size(size) {}
    size_t get_size() const { return m_size; }
};

// 2. mutable: Cho phép chỉnh sửa biến bên trong hàm const
class SensorDevice {
private:
    float m_temperature{25.4f};
    mutable uint32_t m_read_count{0}; // Biến đếm có thể sửa trong hàm const
public:
    float get_temperature() const {
        m_read_count++; // Hoàn toàn hợp lệ nhờ 'mutable'!
        return m_temperature;
    }
    uint32_t get_read_count() const { return m_read_count; }
};

// 3. constexpr & consteval (C++20)
constexpr uint32_t calculate_baud_divisor(uint32_t clock, uint32_t baud) {
    return clock / (16 * baud);
}

consteval uint32_t compile_time_hash(const char* str) {
    uint32_t hash = 5381;
    while (*str) hash = ((hash << 5) + hash) + static_cast<uint8_t>(*str++);
    return hash;
}

// 4. constinit (C++20): Cam kết khởi tạo tĩnh lúc nạp chương trình
constinit uint32_t g_default_baud_div = calculate_baud_divisor(84000000, 115200);

// 5. C++20 Concepts & requires: Ràng buộc kiểu dữ liệu cho Template
template<typename T>
concept OutputDevice = requires(T dev, uint8_t byte) {
    { dev.write_byte(byte) } -> std::same_as<void>;
};

struct MockUart {
    void write_byte(uint8_t b) {
        std::cout << "    [MockUart Hardware] Ghi byte: 0x" << std::hex << (int)b << std::dec << "\n";
    }
};

template<OutputDevice T>
void send_packet(T& device, uint8_t byte) noexcept {
    device.write_byte(byte);
}

// 6. const_cast demo
void legacy_c_api(char* s) {
    std::cout << "    [Legacy C API] Chuoi: " << s << "\n";
}

int main() {
    std::cout << "============================================================\n";
    std::cout << "   DEMO 11: MODERN C++20 EMBEDDED KEYWORDS IN ACTION\n";
    std::cout << "============================================================\n\n";

    // 1. Test explicit
    SafeBuffer buf(256);
    // SafeBuffer bad_buf = 256; // LỖI BIÊN DỊCH nếu bỏ comment!
    std::cout << "[1] explicit: Khoi tao SafeBuffer(" << buf.get_size() << " bytes) an toan.\n\n";

    // 2. Test mutable
    const SensorDevice sensor;
    std::cout << "[2] mutable: Doc cam bien qua con tro const:\n";
    std::cout << "    Lan 1: Temp = " << sensor.get_temperature() << "C (Count = " << sensor.get_read_count() << ")\n";
    std::cout << "    Lan 2: Temp = " << sensor.get_temperature() << "C (Count = " << sensor.get_read_count() << ")\n\n";

    // 3. Test constexpr & consteval
    constexpr auto baud_div = calculate_baud_divisor(16000000, 9600);
    constexpr auto tag_hash = compile_time_hash("SYS_WATCHDOG");
    std::cout << "[3] Compile-time Metaprogramming:\n";
    std::cout << "    constexpr baud divisor: " << baud_div << " (Tinh san luc bien dich)\n";
    std::cout << "    consteval tag hash:     0x" << std::hex << tag_hash << std::dec << "\n";
    std::cout << "    constinit static var:   " << g_default_baud_div << "\n\n";

    // 4. Test reinterpret_cast
    uintptr_t fake_reg_addr = 0x40020000;
    volatile uint32_t* p_reg = reinterpret_cast<volatile uint32_t*>(fake_reg_addr);
    std::cout << "[4] reinterpret_cast: Anh xa dia chi 0x" << std::hex << fake_reg_addr 
              << " sang con tro thanh ghi: " << (void*)p_reg << std::dec << "\n\n";

    // 5. Test const_cast
    const char* message = "Firmware v2.0 Ready";
    std::cout << "[5] const_cast: Goi ham C legacy can tham so char*:\n";
    legacy_c_api(const_cast<char*>(message));

    // 6. Test C++20 Concepts
    std::cout << "\n[6] C++20 concept & requires:\n";
    MockUart uart;
    send_packet(uart, 0xA5);

    return 0;
}
