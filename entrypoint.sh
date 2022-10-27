python manage.py migrate
python manage.py collectstatic --no-input

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
fi
$@

# python manage.py loaddata ./suppliers/database/loaddata.json

gunicorn game.wsgi:application --bind 0.0.0.0:8000
