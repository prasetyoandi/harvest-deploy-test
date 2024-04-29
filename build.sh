#!/bin/bash

# python3.9 -m virtualenv venv

pip3.9 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt

python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations calculate --noinput
python3.9 manage.py migrate --noinput

python3.9 manage.py collectstatic --noinput
