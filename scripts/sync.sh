#!/bin/bash
gcloud storage rsync -R output/ gs://web.evanchen.cc/
gcloud storage rsync -R static/ gs://web.evanchen.cc/static/
gcloud storage rsync -R data/applets/ gs://web.evanchen.cc/applets/
gcloud storage cp static/icons/favicon.ico gs://web.evanchen.cc/favicon.ico

echo ""
echo "Gentle reminder: EXTDIRS and handouts directory not sync'ed"

./scripts/thaw.sh -a
