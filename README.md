# SW API GraphQL - Prueba Técnica

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Prerequisitos
Es necesario tener instalado docker y docker-compose

* [Docker](https://www.docker.com/get-started)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Instalación
Ejecutar en la raiz del proyecto

Compilar y levantar el contenedor
```
$ docker-compose build
$ docker-compose up -d
```

Una vez ejecutado, se procede a ejecutar las migraciones, load fixtures y crear un superusuario
```
$ sudo docker-compose exec web bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py load_fixtures
$ python manage.py createsuperuser
```

If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

## Test
Unitest
```
python manage.py test
```

Pytest
```
pytest
```