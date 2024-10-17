#!/bin/bash

gcloud storage rsync -R static/ gs://web.evanchen.cc/static/
./scripts/thaw.sh -s
