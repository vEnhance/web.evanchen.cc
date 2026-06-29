#!/bin/bash

set -euxo pipefail

if [ "$USER" != "evan" ]; then
  echo "This script is not meant to be used by outsiders."
  echo "You should probably not be running it."
  exit 1
fi

rclone sync -v ~/Freezer/youtube-tex/ web:twitch/ --include 'Ep[0-9][0-9][0-9]-*-Solution.{pdf,tex}'
