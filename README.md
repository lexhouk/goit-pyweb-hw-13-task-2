# Quotes

## Development

```bash
$ git clone https://github.com/lexhouk/goit-pyweb-hw-13-task-2.git
$ cd goit-pyweb-hw-13-task-2
$ docker compose up -d
$ django-admin startproject fpq
$ cd fpq
$ python manage.py startapp fpq_core
$ python manage.py startapp fpq_user
$ python manage.py startapp fpq_author
$ python manage.py startapp fpq_quote
$ python manage.py startapp fpq_tag
$ python manage.py startapp fpq_scraper
$ python manage.py makemigrations
```

## Deployment

```bash
$ git clone https://github.com/lexhouk/goit-pyweb-hw-13-task-2.git
$ cd goit-pyweb-hw-13-task-2
$ docker compose up -d
$ poetry install
$ cd fpq
$ python manage.py migrate
$ python -m utils.migration
$ python manage.py createsuperuser
```

## Usage

```bash
$ docker compose up -d
$ poetry shell
$ cd fpq
$ python manage.py runserver
```

Go to http://localhost:8000.
