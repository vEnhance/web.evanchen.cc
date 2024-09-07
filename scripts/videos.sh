#!/bin/bash

set -xeo pipefail

PYTHONWARNINGS="ignore" gsutil -m cp output/videos.html gs://web.evanchen.cc/
PYTHONWARNINGS="ignore" gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/videos.html
