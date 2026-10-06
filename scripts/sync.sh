#!/bin/bash
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)" || exit 1
rclone copy -v --progress output/ web:
rclone sync -v --progress static/ web:static/
rclone sync -v --progress applets/ web:applets/
rclone copyto -v --progress static/icons/favicon.ico web:favicon.ico

echo ""
echo "Gentle reminder: EXTDIRS and handouts directory not sync'ed"
