#!/usr/bin/env bash
set -euo pipefail

python manage.py migrate --noinput
python init_admin.py

exec gunicorn online_shop.wsgi:application \
  --bind "0.0.0.0:${PORT:-10000}" \
  --workers 1 \
  --access-logfile - \
  --error-logfile -