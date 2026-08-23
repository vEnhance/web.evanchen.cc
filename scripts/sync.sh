#!/bin/bash
rclone -v --progress copy output/  web:
rclone -v --progress sync static/  web:static/
rclone -v --progress sync applets/ web:applets/
rclone -v --progress copyto static/icons/favicon.ico web:favicon.ico

echo ""
echo "Gentle reminder: EXTDIRS and handouts directory not sync'ed"
