#!/bin/sh
python3 userid.py >> log.txt 2>&1 & echo $! >> log.pid
