# Basic and Full-text Search with Django and Postgres

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-search/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Apply the migrations and seed the database:

```sh
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py add_quotes
```

Navigate to [http://127.0.0.1:8011/quotes/](http://127.0.0.1:8011/quotes/).

## Basic vs Full-text Search

You can see examples of both basic and full-text search in *quotes/views.py*.
