#!/bin/bash
gcloud storage rsync -R output/ gs://web.evanchen.cc/
gcloud storage rsync -R css/ gs://web.evanchen.cc/css/
gcloud storage rsync -R js/ gs://web.evanchen.cc/js/
gcloud storage rsync -R elmo/ gs://web.evanchen.cc/elmo/
gcloud storage cp icons/favicon.ico gs://web.evanchen.cc/
gcloud storage rsync -R icons gs://web.evanchen.cc/icons/

echo ""
echo "Gentle reminder: exams, handouts, private, upload directory not sync'ed"

./scripts/thaw.sh
