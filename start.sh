#!/bin/sh
python3 userinfo.py >> log.txt 2>&1 & echo $! >> log.pid
