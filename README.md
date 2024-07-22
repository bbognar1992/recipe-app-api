# recipe-app-api
Recipe API project

flake8 test command:
'''docker-compose run --rm app sh -c "flake8"'''

start django project template:
'''docker-compose run --rm app sh -c "django-admin startproject app ."'''

create the migrations
'''docker-compose run --rm app sh -c "python manage.py makemigrations"'''