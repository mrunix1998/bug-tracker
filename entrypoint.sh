# This file is automatically created by 'no-headache-django' project.
# Please star me on github: http://github.com/mrsaemir/no-headache-django
#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn bug_tracker.wsgi:application -w 2 -b :8000 --daemon
python manage.py runserver 0.0.0.0:7070
