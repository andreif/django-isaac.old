web: bin/python django_isaac/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT django_isaac/settings.py 
