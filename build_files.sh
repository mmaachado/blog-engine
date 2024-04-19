#!/usr/bin/env bash

echo "building packages. . ."
python3 -m pip install -r requirements.txt

echo "migrating database. . ."
python3 engine/manage.py makemigrations --noinput
python3 engine/manage.py migrate --noinput

echo "collecting static files. . ."
python3 engine/manage.py collectstatic --noinput
