#!/bin/bash
echo "Starting old-file-delete at:"
date
echo "Running once without cron"
python3 /usr/local/app/src/delete.py > /var/log/cron.log
cron
tail -f /var/log/cron.log