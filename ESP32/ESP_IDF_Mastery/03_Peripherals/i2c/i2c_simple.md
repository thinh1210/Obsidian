# Topic: I2C Master and Slave Operations (i2c_simple)

## 1. Theory & Protocol Overview
I2C (Inter-Integrated Circuit) is a 2-wire serial protocol (SDA, SCL) designed for short-distance communications between ICs.
*   **Command Link (ESP-IDF Specific):** ESP-IDF uses a command link structure to execute multiple operations. First, you build a transaction list in memory, then you command the hardware to transmit it.
*   **Standard & Fast Modes:** ESP32 supports standard mode (100 kbps) and fast mode (400 kbps).

## 2. Configuration Steps
1.  Configure `sda_io_num`, `scl_io_num`, and pull-up configuration using `i2c_config_t`.
2.  Enable settings via `i2c_param_config()`.
3.  Register driver via `i2c_driver_install()`.

## 3. Logic Flowchart (Command Link Execution)
```mermaid
graph TD
    Start[Start I2C Read] --> Link[Step 1 - i2c_cmd_link_create]
    Link --> StartSig[Step 2 - Queue START Signal]
    StartSig --> WriteAddrW[Step 3 - Queue Write - Slave Addr and WRITE bit]
    WriteAddrW --> WriteReg[Step 4 - Queue Write - Register Addr]
    WriteReg --> ReStart[Step 5 - Queue Repeated START]
    ReStart --> WriteAddrR[Step 6 - Queue Write - Slave Addr and READ bit]
    WriteAddrR --> ReadData[Step 7 - Queue Read byte and NACK]
    ReadData --> StopSig[Step 8 - Queue STOP Signal]
    StopSig --> Execute[Step 9 - Exec Cmd Sequence - i2c_master_cmd_begin]
    Execute --> DelLink[Step 10 - Free Link - i2c_cmd_link_delete]
    DelLink --> End[Transaction Complete]
```

### Logic Explanation:
1.  **Command Link:** Command link structure saves system overhead. The I2C engine does not generate traffic on the bus until `i2c_master_cmd_begin()` is invoked.
2.  **Repeated Start:** Re-issues start without releasing the bus, preventing other masters from hijacking control mid-transaction.

*(Reference path: `examples/peripherals/i2c/i2c_simple`)*
