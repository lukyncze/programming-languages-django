# Django - programming languages project

You can visit site [here](https://lukyncze-programming-languages-django.netlify.app/).

## Project installation:

Clone repository + go to project directory. Continue with Docker or without Docker.

```sh
git clone https://github.com/lukyncze/programming-languages-django
cd programming-languages-django
```

### 1) Docker:

```sh
docker compose build app
docker compose run app python manage.py migrate
docker compose up -d
```

### 2) Without Docker:

Start with creating virtual environment and activating it. Then install requirements and run development server.

#### Linux:

```sh
virtualenv -p python3 .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

#### Windows:

```sh
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver
```

