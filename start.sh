#!/usr/bin/env bash
set -e

mkdir -p /data/media

python manage.py migrate --noinput
python manage.py collectstatic --noinput

python init_admin.py

exec gunicorn online_shop.wsgi:application \
  --bind 0.0.0.0:80 \
  --workers 1 \
  --access-logfile - \
  --error-logfile -