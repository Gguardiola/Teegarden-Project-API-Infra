#!/bin/bash

echo "Starting cron..."
cron
touch /var/log/cron.log
tail -f /var/log/cron.log &

echo "Starting FastAPI with uvicorn..."
fastapi run app/main.py --port 2080
