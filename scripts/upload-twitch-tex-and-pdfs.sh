#!/bin/bash

set -euxo pipefail

if [ "$USER" != "evan" ]; then
  echo "This script is not meant to be used by outsiders."
  echo "You should probably not be running it."
  exit 1
fi

mkdir -p /tmp/twitch/
cp ~/youtube-tex/Ep*Solution.tex /tmp/twitch/
cp ~/youtube-tex/Ep*Solution.pdf /tmp/twitch/

gcloud storage rsync /tmp/twitch/ gs://web.evanchen.cc/twitch/
