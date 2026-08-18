# Topic: UART Echo (Basic Serial Read/Write)

## 1. Theory & Protocol Overview
UART (Universal Asynchronous Receiver-Transmitter) is a simple, asynchronous serial communication protocol using only two wires:
*   **TX (Transmit):** Sends data.
*   **RX (Receive):** Receives data.
*   *Note:* The Baud rate (communication speed, e.g., 115200bps) must match exactly on both devices since there is no shared clock signal.

## 2. Configuration Steps
To configure UART in ESP-IDF:
1.  Define configuration parameters using `uart_config_t`.
2.  Apply settings using `uart_param_config()`.
3.  Bind TX/RX pins to the hardware controller using `uart_set_pin()`.
4.  Allocate internal memory buffer and install the driver using `uart_driver_install()`.

## 3. Logic Flowchart
The following diagram demonstrates the simple "Echo" loop (any data received on RX is immediately re-sent on TX):

```mermaid
graph TD
    Start([app_main]) --> Config[Step 1 - Cfg Struct - Baud, Data bits, Parity]
    Config --> Param[Step 2 - Apply Cfg - uart_param_config]
    Param --> Pins[Step 3 - Assign Pins - uart_set_pin]
    Pins --> Install[Step 4 - Install Driver and Buffers - uart_driver_install]
    Install --> Loop{Infinite Loop}
    Loop --> Read[Step 5 - Read from RX Buffer - uart_read_bytes]
    Read --> DataCheck{Data Size > 0?}
    DataCheck -->|Yes| Write[Step 6 - Write back to TX Buffer - uart_write_bytes]
    Write --> Loop
    DataCheck -->|No/Timeout| Loop
```

### Logic Explanation:
1.  **Buffer Allocation:** During `uart_driver_install`, we allocate an RX Ring Buffer. Incoming bytes are handled by the hardware UART peripheral and placed into this RAM buffer automatically in the background.
2.  **`uart_read_bytes`:** This function checks the RX Ring Buffer. If it's empty, the calling task blocks (goes to sleep) until new data arrives or the timeout expires, preventing 100% CPU usage.

*(Reference path: `examples/peripherals/uart/uart_echo`)*
