#!/bin/sh

cd /Django_app
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput
poetry run python manage.py runserver 0.0.0.0:8000 --insecure