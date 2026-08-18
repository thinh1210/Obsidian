# Topic: Matrix Keyboard (Keypad)

## 1. Theory & Protocol Overview
A matrix keypad connects multiple keys in a grid (rows and columns). Instead of using one GPIO pin per button (which would require 16 pins for a 4x4 keypad), a matrix layout only requires $Rows + Columns$ pins (8 pins for 4x4).
*   **Scanning Mechanism:** The CPU sequentially drives one row LOW (or HIGH) while reading the columns. By detecting which column goes LOW when a specific row is active, the exact coordinates of the pressed key can be calculated.

## 2. Configuration Steps
*   **Driver:** Can be implemented using raw GPIOs or specialized keypad drivers.
*   **Pin Setup:** 
    *   Row Pins: Configured as Outputs.
    *   Column Pins: Configured as Inputs with internal Pull-up resistors.

## 3. Logic Flowchart
```mermaid
graph TD
    Start([Start Scan]) --> SetRow1["Drive Row 1 LOW\nKeep other rows HIGH/Tri-state"]
    SetRow1 --> ReadCols1["Read Columns 1 to 4"]
    ReadCols1 --> CheckPressed1{"Any Col LOW?"}
    CheckPressed1 -->|Yes| Identify["Determine Key: \nRow 1 & Detected Col"]
    CheckPressed1 -->|No| SetRow2["Drive Row 2 LOW\nKeep other rows HIGH/Tri-state"]
    SetRow2 --> ReadCols2["Read Columns 1 to 4"]
    ReadCols2 --> CheckPressed2{"Any Col LOW?"}
    CheckPressed2 -->|Yes| Identify
    CheckPressed2 -->|No| LoopNext["Continue scanning other rows..."]
    LoopNext --> Start
    Identify --> Debounce["Wait for Debounce delay"]
    Debounce --> EndScan([Key Registered])
```

*(Reference path: `examples/peripherals/gpio/matrix_keyboard`)*
