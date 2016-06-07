#!/bin/sh
sleep 5
python manage.py migrate
# python manage.py runserver 0.0.0.0:5000
python manage.py collectstatic --noinput
/usr/local/bin/gunicorn torchmed.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/code