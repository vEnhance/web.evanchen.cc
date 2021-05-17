#!/bin/bash

if [ $# -eq 0 ]; then
	python3 poole/poole.py -b --base-url=//web.evanchen.cc
elif [ $1 = "-debug" ]; then
	python3 poole/poole.py -b --base-url=https://web.evanchen.cc
elif [ $1 = "-local" ]; then
	python3 poole/poole.py -b --base-url=file:///home/evan/Dropbox/Documents/www/
else
	echo "huh?"
fi
