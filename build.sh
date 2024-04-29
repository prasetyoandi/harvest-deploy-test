#!/bin/bash

# python3.9 -m virtualenv venv

pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py makemigrations calculate --noinput
python manage.py migrate --noinput

python manage.py collectstatic --noinput
