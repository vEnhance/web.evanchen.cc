#!/bin/bash
gsutil -m rsync -R output/ gs://web.evanchen.cc/
gsutil -m rsync -R css/ gs://web.evanchen.cc/css/
gsutil -m rsync -R elmo/ gs://web.evanchen.cc/elmo/
gsutil -m rsync -R static/ gs://web.evanchen.cc/web/
gsutil -m cp icons/favicon.ico gs://web.evanchen.cc/
gsutil -m rsync -R icons gs://web.evanchen.cc/icons/

echo ""
echo "Gentle reminder: exams, handouts, private, upload directory not sync'ed"

./setmeta.sh
