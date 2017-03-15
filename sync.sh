#!/bin/bash
gsutil -m rsync -R css gs://www.evanchen.cc/css/
gsutil -m rsync -R elmo gs://www.evanchen.cc/elmo/
gsutil -m rsync -R static gs://www.evanchen.cc/static/
gsutil -m rsync -R output gs://www.evanchen.cc/

echo "exams, upload directory not sync'ed"
