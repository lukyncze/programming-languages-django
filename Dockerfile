FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=programming_languages.wsgi
