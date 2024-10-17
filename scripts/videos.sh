#!/bin/bash

set -xeo pipefail

gcloud storage cp output/videos.html gs://web.evanchen.cc/
gcloud storage objects update --custom-metadata='Cache-Control="private,max-age=0"' gs://web.evanchen.cc/videos.html
