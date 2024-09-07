#!/bin/bash
PYTHONWARNINGS="ignore" gsutil -m rsync -R output/ gs://web.evanchen.cc/
PYTHONWARNINGS="ignore" gsutil -m rsync -R css/ gs://web.evanchen.cc/css/
PYTHONWARNINGS="ignore" gsutil -m rsync -R js/ gs://web.evanchen.cc/js/
PYTHONWARNINGS="ignore" gsutil -m rsync -R elmo/ gs://web.evanchen.cc/elmo/
PYTHONWARNINGS="ignore" gsutil -m rsync -R static/ gs://web.evanchen.cc/static/
PYTHONWARNINGS="ignore" gsutil -m cp icons/favicon.ico gs://web.evanchen.cc/
PYTHONWARNINGS="ignore" gsutil -m rsync -R icons gs://web.evanchen.cc/icons/

echo ""
echo "Gentle reminder: exams, handouts, private, upload directory not sync'ed"

./scripts/thaw.sh
