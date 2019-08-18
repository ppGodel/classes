#!/bin/sh
# this script is used to boot a Docker container
source venv/bin/activate
flask run > log_$(date +%Y-%m-%d_%H:%M).txt