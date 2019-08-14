#!/bin/sh
python3 pokaztt.py >> log.txt 2>&1 & echo $! >> log.pid
