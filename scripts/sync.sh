#!/bin/bash
rclone -v copy output/  web:
rclone -v sync static/  web:static/
rclone -v sync applets/ web:applets/
rclone -v copyto static/icons/favicon.ico web:favicon.ico

echo ""
echo "Gentle reminder: EXTDIRS and handouts directory not sync'ed"
