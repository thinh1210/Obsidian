# Outline: Advanced UART Examples

Here is a summary of other advanced UART concepts available in your ESP-IDF directory:

## 1. `uart_async_rxtxtasks`
*   **Concept:** Separates Transmitting (TX) and Receiving (RX) logic into two concurrent FreeRTOS tasks to achieve non-blocking full-duplex communication.
*   **Logic:**
    ```text
    Task 1 (RX) -> Blocks waiting for RX bytes. When received, logs to Console.
    Task 2 (TX) -> Periodically sends status/heartbeat commands.
    ```

## 2. `uart_select`
*   **Concept:** Uses the POSIX `select()` API on top of the UART virtual file system (VFS) driver.
*   **Use Case:** Multi-device event multiplexing (monitoring multiple UART ports or sockets simultaneously from a single thread).

## 3. `uart_echo_rs485`
*   **Concept:** Configures UART for half-duplex RS485 communication.
*   **Logic:** The driver automatically toggles a hardware RTS (Request to Send) pin to switch the transceiver between Send and Receive modes.

*(Reference path: `/home/thinh/esp/esp-idf/examples/peripherals/uart/`)*
