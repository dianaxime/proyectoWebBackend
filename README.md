# proyectoWebBackend
Proyecto de Sistemas y Tecnologías Web (Backend)

1. Clonar el Repositorio
2. Crear virtual environment py -m venv env
3. Activar virtual environment .\venv\Scripts\activate

## LocalHost

pip install -r requirements
python manage.py migrate
python manage.py runserver

## Heroku

heroku ps:scale web=1
