#!/usr/bin/env bash
# Packages the must-use plugin for upload to wp-content/mu-plugins/.
# Usage: bash motion-graphics/wp-install/build-zip.sh
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
root="$(dirname "$here")"
tmp="$(mktemp -d)"
mkdir -p "$tmp/emg-motion/partials"
cp "$here/emg-motion-graphics.php" "$tmp/"
cp "$root/emg-motion.css" "$root/emg-motion.js" "$tmp/emg-motion/"
cp "$root"/partials/*.html "$tmp/emg-motion/partials/"
rm -f "$root/emg-motion-graphics.zip"
(cd "$tmp" && zip -qr "$root/emg-motion-graphics.zip" emg-motion-graphics.php emg-motion)
rm -rf "$tmp"
echo "Wrote $root/emg-motion-graphics.zip"
