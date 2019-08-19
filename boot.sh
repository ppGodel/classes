#!/bin/sh
# this script is used to boot a Docker container
waitress-serve --call 'waitress_serve:app' --port=5000