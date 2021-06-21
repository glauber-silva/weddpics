#!/bin/sh

echo "Waiting for database ..."

while ! nc -z mongodb 27017; do
  sleep 0.1
done

uwsgi --ini ./uwsgi.ini
