# GAS STATION

[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

<br/>

## Requirements

- Python - 3.10
- Django - 4.0.4
- Django REST Framework - 3.13.1
- Psycopg2 - 2.9.3
- Django-environ - 0.8.1

<br/>

## Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command

```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running

```
pip install -r requirements.txt
```

Now you need to enable postgresql in docker with docker-compose command. If you don't know docker you
can get more info [here](https://docs.docker.com/)

```
cd .docker

docker-compose up -d
```

<br/>

## Env Variables And Run Server

After enabling docker to activate the database, now you need to configure the environment variables. For this, create an .env file in the CORE layer and put the same data as in the .env.example file

```shell
DATABASE_NAME=gas_station
DATABASE_USER=root
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Now, you can activate the server:

```shell
python manager.py runserver
```

<br/>

## Enabling Migrations

Now you need to enable migrations to create all database entities and relations. Use this command on gas_station_api directory:

```shell
python manager.py migrate
```
