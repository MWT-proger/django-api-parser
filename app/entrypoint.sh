#!/bin/bash

set -e

cmd="$*"

>&2 echo "Обновление миграций"
python manage.py migrate

>&2 echo "Обновление статических файлов"
python manage.py collectstatic --noinput

exec $cmd
