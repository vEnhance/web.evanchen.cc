#!/bin/bash

set -xeo pipefail

gsutil -m cp output/videos.html gs://web.evanchen.cc/
gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/videos.html
