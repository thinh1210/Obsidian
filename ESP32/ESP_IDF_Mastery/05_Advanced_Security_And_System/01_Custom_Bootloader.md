# Deep Dive: Custom Bootloader & Bootloader Hooks

## 1. Deep-Dive Mechanics & Architecture
During the boot phase, the ESP32 operates in a highly constrained **bare-metal environment** (no operating system, no scheduler, and no virtual memory).

### Memory Mapping Constraints (MMU & SRAM)
*   **No MMU Mapping:** The Memory Management Unit (MMU) is not yet fully configured to map external SPI flash to the CPU instruction/data buses (IROM/DROM). Consequently, the CPU can only execute code residing in internal **SRAM** (specifically IRAM for instructions and DRAM for data).
*   **ROM Bootloader (Stage 1):** Code hardcoded inside the ESP32's internal ROM during manufacturing. It runs immediately on power-on or hardware reset. It executes basic clock configuration, initializes the UART0 port for debug output, and reads the physical voltages on **GPIO strap pins** (GPIO 0, GPIO 2, GPIO 5, GPIO 12, GPIO 15) to decide whether to boot into serial download mode (flashing) or SPI boot mode.
*   **2nd Stage Bootloader:** If SPI boot is selected, the ROM bootloader copies the 2nd stage bootloader binary (compiled by ESP-IDF) from external flash address `0x1000` (or `0x0` depending on the chip target) into internal SRAM, and then jumps the PC (Program Counter) register to this address.

### The Role of Bootloader Hooks
Recompiling the entire 2nd stage bootloader source code is risky and complex. ESP-IDF provides **Bootloader Hooks**—weak-link symbols defined in the bootloader framework that can be overridden by user components.
*   `bootloader_before_init()`: Runs immediately after the CPU jumps to the 2nd stage bootloader, before the flash cache, MMU, or eFuse controllers are initialized.
*   `bootloader_after_init()`: Runs after flash cache, MMU, and storage devices are operational, but before the main application binary is verified or loaded into RAM.

---

## 2. Configuration & Toolchain Setup
To integrate a custom bootloader hook into your project:

### Step 1: Create the Component
Create a special directory named `bootloader_components` in the root of your project. The build system automatically checks this folder when compiling the bootloader binary.
```text
my_project/
├── CMakeLists.txt
├── main/
│   └── main.c
└── bootloader_components/
    └── my_boot_hooks/
        ├── CMakeLists.txt
        └── boot_hooks.c
```

### Step 2: Write `bootloader_components/my_boot_hooks/CMakeLists.txt`
This file instructs the bootloader compiler to build your hook code.
```cmake
# Note: Bootloader components use the same idf_component_register API 
# but are compiled with a different toolchain configuration (bootloader subproject)
idf_component_register(SRCS "boot_hooks.c"
                       INCLUDE_DIRS ".")
```

### Step 3: Implement the Hook Code (`boot_hooks.c`)
Overriding the weak-link hooks:
```c
#include "esp_log.h"
#include "gpio_hal.h" // Low-level Hardware Abstraction Layer (HAL)
#include "driver/gpio.h"

static const char *TAG = "BOOT_HOOK";

// Overriding weak function called before bootloader initialization
void bootloader_before_init(void) {
    // 1. Keep it raw: Only low-level HAL calls or direct register modifications are safe.
    // 2. Example: Pull a GPIO pin high immediately on boot to enable a power rail.
    gpio_ll_output_enable(&GPIO, GPIO_NUM_4);
    gpio_ll_set_level(&GPIO, GPIO_NUM_4, 1);
}

void bootloader_after_init(void) {
    // Flash cache is active here, you can read partition tables or print standard log
    ESP_LOGI(TAG, "Bootloader hardware initialization complete!");
}
```

---

## 3. Flowchart & Critical Paths Analysis

```mermaid
graph TD
    %% Sequence
    PowerOn([Power On / Reset]) --> Stage1[Step 1 - ROM Bootloader Executing]
    Stage1 --> CheckStrap[Step 2 - Check Strap Pins - GPIO 0 and GPIO 2]
    
    CheckStrap -- GPIO0 = LOW --> Flashing[UART Flashing Mode\n*Stops execution*]
    CheckStrap -- GPIO0 = HIGH --> CopyStage2[Step 3 - Copy Stage 2 Bootloader from Flash to SRAM]
    
    subgraph 2nd Stage Bootloader (RAM Context)
        CopyStage2 --> CallHookBefore[Step 4 - Call - bootloader_before_init]
        
        CallHookBefore --> HookBeforeCheck{Is user hook defined?}
        HookBeforeCheck -- Yes --> ExecBefore[Execute Raw C Code\n*No FreeRTOS APIs allowed*]
        HookBeforeCheck -- No --> InitHW[Step 5 - Initialize Cache, MMU, and eFuse]
        ExecBefore --> InitHW
        
        InitHW --> CallHookAfter[Step 6 - Call - bootloader_after_init]
        CallHookAfter --> HookAfterCheck{Is user hook defined?}
        HookAfterCheck -- Yes --> ExecAfter[Execute Post-Init C Code\n*Print logs, read partition tables*]
        HookAfterCheck -- No --> LoadApp[Step 7 - Read Partition Table and Load App]
        ExecAfter --> LoadApp
        
        LoadApp --> VerifyApp{Is App Valid?\nSecure Boot Signature OK?}
        VerifyApp -- No --> HaltBoot([Halt Bootloader\n*Stops boot / safe state*])
        VerifyApp -- Yes --> JumpApp[Step 8 - Jump PC to App Entry point]
    end
    
    JumpApp --> FreeRTOSStart([Initialize FreeRTOS Scheduler\nExecute app_main])
```

### Critical Decisions & Branching:
*   **Strap Pin Branch (`CheckStrap`):** If GPIO0 is held LOW during power-up (usually via a boot button), execution jumps to ROM flashing mode. No bootloader code is loaded.
*   **Hook Before Init (`CallHookBefore`):** This is the earliest entry point for software execution. If your custom code crashes here, the bootloader will fail before logging interfaces are initialized, resulting in a silent boot loop (no serial prints).
*   **App Verification Branch (`VerifyApp`):** If Secure Boot is enabled, the 2nd stage bootloader checks the cryptographic signature of the main application. If verification fails (due to corrupted bits or tampered binary), the bootloader enters an infinite loop (`HaltBoot`), preventing execution.

---

## 4. System Impacts & Warnings

### Performance (Boot Time)
*   Adding heavy code in `bootloader_before_init` or `bootloader_after_init` directly delays the main application boot time.
*   Avoid loops, heavy mathematical computations, or delays (`rom_delay_us`) inside hooks.

### Stack Constraints
*   The 2nd stage bootloader stack size is extremely small (configured via `CONFIG_BOOTLOADER_STACK_SIZE`, default is usually **8KB**).
*   **Warning:** Do not declare large local arrays (e.g., `char buffer[4096]`) inside bootloader hooks. Doing so causes a **stack overflow** which corrupts memory and crashes the CPU before the main program starts.

### API Limitations
*   You cannot call any FreeRTOS API (`vTaskDelay`, `xTaskCreate`, `xSemaphoreTake`).
*   You cannot call driver APIs (`gpio_config`, `uart_write_bytes`) because the standard driver subsystems rely on FreeRTOS features (interrupt registers, queues, mutexes) which are not yet initialized. Use low-level HAL headers (`hal/gpio_hal.h`, `hal/uart_hal.h`) instead.

### Debugging
*   JTAG debugging is supported during the bootloader stage unless permanently disabled by Flash Encryption / Secure Boot eFuses.
*   To trace errors in hooks, set the bootloader log level to Verbose via `menuconfig`: `Bootloader config -> Bootloader log verbosity` -> `Verbose`.
