echo "BUILD START"

python -m venv dar
dar\Scripts\activate.bat
cd backend
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

echo "BUILD END"