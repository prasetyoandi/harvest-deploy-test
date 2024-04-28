echo "Building the project..."
source bin/activate
python3.9 -m pip install -r requirements.txt
echo "Collect stetic.."
python3.9 manage.py collectstatic --noinput --clear