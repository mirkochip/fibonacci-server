#!/bin/bash

python manage.py collectstatic --noinput
python manage.py makemigrations fibonacci
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
