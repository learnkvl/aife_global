#!/bin/bash

# Python setup
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Django setup
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# Create public directory and move static files into it
mkdir -p public/static
cp -r staticfiles/* public/static/
