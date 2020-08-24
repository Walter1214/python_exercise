# python_exercise

python -m venv env
source env/bin/activate
django-admin startproject tutorial
python manage.py startapp snippets
python manage.py runserver
python manage.py makemigrations snippets
python manage.py migrate

pip freeze > requirements.txt