/*
 * sensor_telemetry.c - Embedded Telemetry Service Daemon
 * Example program packaged into .deb and deployed onto Yocto Linux image
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>

#define DEFAULT_CONF_PATH "/etc/sensor-telemetry/sensor.conf"
#define DEFAULT_LOG_PATH  "/var/log/sensor-telemetry.log"

static volatile int keep_running = 1;

void handle_signal(int sig) {
    if (sig == SIGINT || sig == SIGTERM) {
        keep_running = 0;
    }
}

void read_system_metrics(float *load1, long *mem_free_kb) {
    *load1 = 0.0f;
    *mem_free_kb = 0;

    FILE *f_load = fopen("/proc/loadavg", "r");
    if (f_load) {
        if (fscanf(f_load, "%f", load1) != 1) {
            *load1 = -1.0f;
        }
        fclose(f_load);
    }

    FILE *f_mem = fopen("/proc/meminfo", "r");
    if (f_mem) {
        char line[128];
        while (fgets(line, sizeof(line), f_mem)) {
            if (strncmp(line, "MemAvailable:", 13) == 0) {
                sscanf(line + 13, "%ld", mem_free_kb);
                break;
            }
        }
        fclose(f_mem);
    }
}

int main(int argc, char *argv[]) {
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);

    int interval_sec = 5;
    char device_id[64] = "yocto-edge-node-01";
    char log_path[128] = DEFAULT_LOG_PATH;

    /* Read config file if present */
    FILE *f_conf = fopen(DEFAULT_CONF_PATH, "r");
    if (f_conf) {
        char key[64], val[64];
        while (fscanf(f_conf, "%63[^=]=%63[^\n]\n", key, val) == 2) {
            if (strcmp(key, "INTERVAL") == 0) {
                interval_sec = atoi(val);
                if (interval_sec <= 0) interval_sec = 5;
            } else if (strcmp(key, "DEVICE_ID") == 0) {
                strncpy(device_id, val, sizeof(device_id) - 1);
            } else if (strcmp(key, "LOG_PATH") == 0) {
                strncpy(log_path, val, sizeof(log_path) - 1);
            }
        }
        fclose(f_conf);
    }

    printf("[SENSOR-TELEMETRY] Starting telemetry service...\n");
    printf("[SENSOR-TELEMETRY] Device ID: %s, Interval: %ds, Log: %s\n", device_id, interval_sec, log_path);

    int cycle = 0;
    while (keep_running) {
        float load1 = 0.0f;
        long mem_free_kb = 0;
        read_system_metrics(&load1, &mem_free_kb);

        time_t now = time(NULL);
        char time_str[64];
        strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S", localtime(&now));

        /* Simulated sensor temperature: base 42.0C with variation */
        float sim_temp = 42.0f + (float)(rand() % 100) / 10.0f;

        char log_entry[256];
        snprintf(log_entry, sizeof(log_entry),
                 "[%s] node=%s cycle=%d load1=%.2f mem_avail_mb=%.1f temp=%.1f C\n",
                 time_str, device_id, ++cycle, load1, (float)mem_free_kb / 1024.0f, sim_temp);

        /* Print to stdout */
        fputs(log_entry, stdout);
        fflush(stdout);

        /* Append to log file */
        FILE *f_log = fopen(log_path, "a");
        if (f_log) {
            fputs(log_entry, f_log);
            fclose(f_log);
        }

        sleep(interval_sec);
    }

    printf("[SENSOR-TELEMETRY] Daemon stopped cleanly.\n");
    return 0;
}
