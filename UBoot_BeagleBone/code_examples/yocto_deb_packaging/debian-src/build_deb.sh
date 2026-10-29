#!/usr/bin/env bash
set -e

PKG_NAME="sensor-telemetry"
PKG_VER="1.0.0"
PKG_ARCH="amd64"
PKG_DIR="${PKG_NAME}_${PKG_VER}_${PKG_ARCH}"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Building ${PKG_NAME} binary ==="
gcc -static -O2 "${SRC_DIR}/sensor_telemetry.c" -o "${SRC_DIR}/sensor-telemetry"
strip --strip-unneeded "${SRC_DIR}/sensor-telemetry"

echo "=== Creating Debian package directory tree: ${PKG_DIR} ==="
rm -rf "${SRC_DIR}/${PKG_DIR}"
mkdir -p "${SRC_DIR}/${PKG_DIR}/DEBIAN"
mkdir -p "${SRC_DIR}/${PKG_DIR}/usr/bin"
mkdir -p "${SRC_DIR}/${PKG_DIR}/etc/sensor-telemetry"
mkdir -p "${SRC_DIR}/${PKG_DIR}/etc/init.d"
mkdir -p "${SRC_DIR}/${PKG_DIR}/lib/systemd/system"

# Copy binary, configs, init script, and systemd service
cp -f "${SRC_DIR}/sensor-telemetry" "${SRC_DIR}/${PKG_DIR}/usr/bin/"
chmod 755 "${SRC_DIR}/${PKG_DIR}/usr/bin/sensor-telemetry"

cp -f "${SRC_DIR}/sensor.conf" "${SRC_DIR}/${PKG_DIR}/etc/sensor-telemetry/"
chmod 644 "${SRC_DIR}/${PKG_DIR}/etc/sensor-telemetry/sensor.conf"

cp -f "${SRC_DIR}/sensor-telemetry.init" "${SRC_DIR}/${PKG_DIR}/etc/init.d/sensor-telemetry"
chmod 755 "${SRC_DIR}/${PKG_DIR}/etc/init.d/sensor-telemetry"

cp -f "${SRC_DIR}/sensor-telemetry.service" "${SRC_DIR}/${PKG_DIR}/lib/systemd/system/"
chmod 644 "${SRC_DIR}/${PKG_DIR}/lib/systemd/system/sensor-telemetry.service"

# Create DEBIAN/control
cat << 'EOF' > "${SRC_DIR}/${PKG_DIR}/DEBIAN/control"
Package: sensor-telemetry
Version: 1.0.0
Architecture: amd64
Maintainer: Embedded Dev Team <dev@embedded.local>
Section: utils
Priority: optional
Description: IoT Sensor Telemetry Daemon for Yocto Embedded Linux
 A lightweight telemetry logging daemon designed for edge gateways.
EOF

# Create DEBIAN/postinst
cat << 'EOF' > "${SRC_DIR}/${PKG_DIR}/DEBIAN/postinst"
#!/bin/sh
set -e
echo "[DEB-POSTINST] Configuring sensor-telemetry permissions..."
chmod 755 /usr/bin/sensor-telemetry
chmod 644 /etc/sensor-telemetry/sensor.conf
chmod 644 /lib/systemd/system/sensor-telemetry.service
mkdir -p /var/log
echo "[DEB-POSTINST] Completed."
exit 0
EOF
chmod 755 "${SRC_DIR}/${PKG_DIR}/DEBIAN/postinst"

# Create DEBIAN/prerm
cat << 'EOF' > "${SRC_DIR}/${PKG_DIR}/DEBIAN/prerm"
#!/bin/sh
set -e
echo "[DEB-PRERM] Preparing to remove sensor-telemetry..."
exit 0
EOF
chmod 755 "${SRC_DIR}/${PKG_DIR}/DEBIAN/prerm"

echo "=== Building .deb file with dpkg-deb ==="
dpkg-deb --build --root-owner-group "${SRC_DIR}/${PKG_DIR}" "${SRC_DIR}/${PKG_DIR}.deb"

echo "=== Package successfully created: ${SRC_DIR}/${PKG_DIR}.deb ==="
dpkg-deb -I "${SRC_DIR}/${PKG_DIR}.deb"
echo "=== Package Contents ==="
dpkg-deb -c "${SRC_DIR}/${PKG_DIR}.deb"
