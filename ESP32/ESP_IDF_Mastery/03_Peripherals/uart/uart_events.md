# Topic: UART Events & Pattern Detection

## 1. Theory & Protocol Overview
Instead of actively polling for bytes using `uart_read_bytes`, a more advanced and robust way is to use **UART Events**. The driver uses an OS queue to notify the application of different hardware-level events:
*   **`UART_DATA`:** Normal data bytes received.
*   **`UART_FIFO_OVF` / `UART_BUFFER_FULL`:** Buffer overflow warnings.
*   **`UART_PATTERN_DET`:** Pattern matching (e.g., detecting `\r\n` or `+++` in command lines).

## 2. Configuration Steps
1.  Configure UART parameters as usual.
2.  During `uart_driver_install`, provide a pointer to a `QueueHandle_t` to receive driver events.
3.  Configure pattern detection using `uart_enable_pattern_det_baud_intr()`.

## 3. Logic Flowchart
```mermaid
graph TD
    Start([app_main]) --> InitUART["Configure & Install UART Driver"]
    InitUART --> GetQueue["Save Event Queue pointer from Driver"]
    GetQueue --> PatternDet["Set Up Pattern: e.g., '+' character"]
    PatternDet --> CreateTask["Create Event Handler Task: xTaskCreate"]
    
    subgraph Event Handler Task
        TaskLoop{Loop} --> WaitQueue["xQueueReceive: wait for UART Event"]
        WaitQueue -->|UART_DATA| ProcData["Read data buffer & process"]
        WaitQueue -->|UART_PATTERN_DET| ProcPattern["Query pattern position\nRead command command strings"]
        WaitQueue -->|UART_FIFO_OVF| ProcOvf["Reset RX buffer / Log warning"]
        ProcData --> TaskLoop
        ProcPattern --> TaskLoop
        ProcOvf --> TaskLoop
    end
    
    TriggerEvent((UART Hardware Event)) -.->|Sends Event Struct| WaitQueue
```

### Logic Explanation:
1.  **Event Queue:** When the hardware UART peripheral detects an event (like receiving bytes or matching a pattern), it writes a `uart_event_t` struct directly to the queue.
2.  **`UART_PATTERN_DET`:** Extremely useful for AT command parsing. The hardware automatically identifies the target sequence and gives you the exact buffer index, eliminating the need to write complex string parser logic.

*(Reference path: `examples/peripherals/uart/uart_events`)*
