#!/bin/bash
gcloud storage rsync -R output/ gs://web.evanchen.cc/
gcloud storage rsync -R static/ gs://web.evanchen.cc/static/
gcloud storage rsync -R applets/ gs://web.evanchen.cc/applets/
gcloud storage rsync -R elmo/ gs://web.evanchen.cc/elmo/
gcloud storage cp static/icons/favicon.ico gs://web.evanchen.cc/favicon.ico

echo ""
echo "Gentle reminder: exams, handouts, private, upload directory not sync'ed"

./scripts/thaw.sh
