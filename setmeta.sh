#!/bin/bash
gsutil -m setmeta -R -h 'Cache-Control:public, max-age=300, no-transform' gs://web.evanchen.cc/
