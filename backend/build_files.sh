echo "BUILD START"

python get-pip.py
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

echo "BUILD END"