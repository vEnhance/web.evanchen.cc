#!/bin/bash

set -xeo pipefail

gcloud storage cp output/videos.html gs://web.evanchen.cc/ --cache-control="private,max-age=0"
