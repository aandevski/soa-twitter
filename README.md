# Microservice Twitter

Project for the service oriented architectures subject. A simple implementation of a Twitter REST backend using Flask, Kong and Consul.

## Running with docker-compose

To start the services use `docker-compose build && docker-compose up -d`.

To take the services down, use `docker-compose down`.

### Applying migrations to databases

You will need to do this for every microservice:

```
docker exec -it microservice_<name> /bin/bash
python manage.py db upgrade
```

For example, for the tweets microservice:
```
docker exec -it microservice_tweets /bin/bash
python manage.py db upgrade
```

Last, you need to register the endpoints with Kong using `sh install.sh`.

## Running a single service for development

If you want to develop a particular service, you will need to host your own Postgres server.
To start a development server, use `DATABASE_URL=postgresql://<db_username>:<db_password>@<db_host>/<db_database> python app.py`

To apply migrations to the database, first erase the database, then use the following commands
```
rm -r migrations
DATABASE_URL=postgresql://<db_username>:<db_password>@<db_host>/<db_database> python manage.py db init
DATABASE_URL=postgresql://<db_username>:<db_password>@<db_host>/<db_database> python manage.py db migrate
DATABASE_URL=postgresql://<db_username>:<db_password>@<db_host>/<db_database> python manage.py db upgrade
```
We always have to erase the database and delete the migrations folder since flask-sqlalchemy can't detect renames and type changes.