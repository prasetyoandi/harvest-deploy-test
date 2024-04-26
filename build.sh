# !/bin/bash

# python3.9 -m virtualenv venv

# build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt
python3.9 managepy collectstatic

echo "Make migrations... "
python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations calculate --noinput
python3.9 manage.py migrate --noinput

echo "Collect stetic.."
python3.9 manage.py collectstatic --noinput --clear