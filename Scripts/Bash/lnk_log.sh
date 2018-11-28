#!/bin/bash

# Simple bash script to map log file
# /var/log/hoist/IP/today
# /var/log/hoist/IP/yesterday

root_dir=/srv/syslog/
lnk_dir=/var/log/hosts

today=$(date +%Y/%m/%d)
yesterday=$(date +%Y/%m/%d -d "yesterday")

for d in $root_dir
	ln -s $root_dir$today $lnk_dir/today"
	ln -s $root_dir$yesterday $lnk_dir/yesterday"
done
