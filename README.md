# Artifica - A personal OS-like portfolio.

> Artifica is a work in progress and a personal project.

Artifica is an OS-like Personal Web Portfolio designed following the [Fluent Design System](https://www.microsoft.com/design/fluent/) made by Microsoft for the Windows operating system. It was inspired by the awesome [MAD](https://mad.ac/) Studio's page.

![Light mode screenshot](./assets/screenshot-light.png)
![Dark mode screenshot](./assets/screenshot-dark.png)

## Features

- Powered by Django.
- Wagtail as the CMS.
- Modern Front-End workflow.
- Easy to add JS & CSS libraries.
- Ready to deploy with Docker.
- Developed following the [the 12-factor methodoly](https://www.12factor.net/).
- Support for light/dark mode.
- _Almost_ functional "applets".
- Ready to deploy.

## Stack

- Django
- Wagtail
- Docker
- Tailwind CSS & Flowbite
- ESbuild
- SQLite/PostgreSQL
- Memcached/Redis.

## Why?

I have always liked my portfolios to present information about me and my stack, as well as my expertise. And Artifica is not an exception to that.

Artifica's design is my way of breaking down the multiple areas in which I have been developing professionally throughout my career as a software developer. But, by dividing these areas into "applets" rather than sections, I am trying to show how all these areas are interrelated.

## What are applets?

Applets are the keystone on which the idea and the development of Artifica is based. Basically, they are small components that try to fulfill different functions. For example, some applets are just links to other sites or sections while others pretend to have functionality and work as a full application.

The list of applets and their functionality is a work in progress but the list of applets that can be used right now is:

- Button.
- Contact.
- Social links.
- Notes.
- Pomodoro.
- Textual applet.
- To Do.

> You can create and manage these applets using the Wagtail admin page.

## Installation

The best way to start working with Artifica is to clone this respositoy:

```bash
git clone https://github.com/daniarlert/artifica
```

Setup a Python's virtual environment and install the dependencies. I personally prefer to use [poetry](https://python-poetry.org/) but since the requirements are listed in a plain `requirements.txt` you can use any tool you want.

```bash
poetry install

# Or

python -m pip install -r requirements
```

Since Artifica uses modern Front-End libraries like Tailwind CSS and some npm modules, you would also need to have installed Node.js in your development setup. To install the necessary dependencies just run:

```bash
cd artifica/frontend && npm install
```

This project also has setup some git hooks focused on the maintenance of the dependencies and the code format. To activate them, run with the virtual environment activated the following command:

```bash
pre-commit install
```

## Development setup

> TODO:

### Front-End

> TODO:

## `ENV` variables

For development, the only `env` variable that you'll need is `DEBUG` whose value does not really matter as long as it has one:

```plain
DEBUG=on
```

> If instead of using `manage.py runserver` you want to use the `entrypoint.sh` you'll need to also specify a `PORT` `env` variable.

For production is recommended to set the below `env` variables.

```plain
DJANGO_ALLOWED_HOSTS=
DJANGO_CSRF_TRUSTED_ORIGINS=
DJANGO_SECRET_KEY=
DJANGO_LOG_LEVEL=
DJANGO_LOG_BASIC_FILE=
DJANGO_LOG_DETAILED_FILE=

DATABASE_ENGINE=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=

CACHE_ENGINE=
CACHE_URL=
```

Other `env` variables may be needed depending on your deployment pipeline. For example, for render you will need to add the `RENDER_EXTERNAL_HOSTNAME` variable.

> Note that if you are using the `docker-compose.yaml` file it expects an `.env.prod` file.

## Logging

> TODO:

## Cache

Artifica comes with [redis-py](https://pypi.org/project/redis/) and [hiredis](https://pypi.org/project/hiredis/). To start using Redis add the following `env` variables to your `.env` file:

```env
CACHE_ENGINE=django.core.cache.backends.redis.RedisCache
CACHE_URL=redis://127.0.0.1:6379
```

If the `CACHE_ENGINE` and `CACHE_URL` `env` variables are not setup. It will use [dummy caching](https://docs.djangoproject.com/en/4.1/topics/cache/#dummy-caching-for-development).

## Database

### SQLite

> TODO:

### PostgreSQL

> TODO:

## Deploy

### render

If you're going to deploy this project to [render](render.com) It's recommended to check first their [quickstart guide](https://render.com/docs/deploy-django).

Although this project contains a `render.yaml` file, unless you modify it, the deployment will need to be manual as specified in the guide mentioned above.

### Railway

To deploy this project on [Railway](https://railway.app/) first create a new project with a Redis and a PostgreSQL services. Then, connect your cloned Artifica repository to Railway and it will pick up automatically the `Dockerfile`. Now set all the necessary `env` variables and you'll be good to go.

For more information about Railway just go to their [documentation](https://docs.railway.app/).

## Docker

### Docker image

> I decided to use a `slim` base Docker image instead of an `alpine` one. If you want to learn more about the "why" please, read [this article](https://pythonspeed.com/articles/alpine-docker-python/).

> TODO:

### Docker compose

> TODO:

## Work in progress

Artifica is a work in progress and a personal project. By this I mean that there will be certain features that I will not implement and others that I will work on at my own discretion.

If you are someone who wants to contribute to the code of this project please open an issue first.

## Contributions

This project follows the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. If a contribution does not follow this specification, it will not be accepted. Code with bad formatting will also not be accepted.
