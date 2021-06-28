#!/bin/bash
gsutil -m rsync -R static/ gs://web.evanchen.cc/static/
./scripts/thaw.sh -s
