SUMMARY = "Binary deb package recipe for Sensor Telemetry Daemon"
DESCRIPTION = "Example recipe demonstrating how to integrate a pre-built .deb package into Yocto RootFS"
HOMEPAGE = "https://embedded.antigravity.internal"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://sensor-telemetry_1.0.0_amd64.deb;subdir=${BP}"

inherit bin_package update-rc.d systemd

# SysVinit configuration
INITSCRIPT_NAME = "sensor-telemetry"
INITSCRIPT_PARAMS = "defaults 95 10"

# Systemd configuration (if systemd is in DISTRO_FEATURES)
SYSTEMD_SERVICE:${PN} = "sensor-telemetry.service"
SYSTEMD_AUTO_ENABLE = "enable"

# Pre-compiled binaries from external deb are already stripped
INSANE_SKIP:${PN} += "already-stripped"
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INHIBIT_PACKAGE_STRIP = "1"

FILES:${PN} += " \
    ${bindir}/sensor-telemetry \
    ${sysconfdir}/sensor-telemetry/sensor.conf \
    ${sysconfdir}/init.d/sensor-telemetry \
    ${systemd_system_unitdir}/sensor-telemetry.service \
"
