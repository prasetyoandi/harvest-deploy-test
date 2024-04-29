#!/bin/bash

# python3.9 -m virtualenv venv

python3.9 -m pip3 install -r requirements.txt

python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations calculate --noinput
python3.9 manage.py migrate --noinput

python3.9 manage.py collectstatic --noinput
