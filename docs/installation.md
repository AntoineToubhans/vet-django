# Installation

## Prerequisites

- [Docker Compose](https://docs.docker.com/compose/install/)

## Install dependencies

```bash
docker-compose run --rm server pip install -r requirements.txt --user --upgrade
```

You can check that Django is installed by running:

```bash
docker-compose run --rm server python -m django --version
```

## Prepare database

First, you need to run initial migrations:

```bash
docker-compose exec server python manage.py migrate
```

Then, create a root user by running:

```bash
docker-compose exec server python manage.py createsuperuser
```

You'll be prompted for username and password.
If successful, you should be able to connect as root to the admin `http://localhost:8000/admin`.

## Running

Run the following to start Django:

```bash
docker-compose up -d server
```

### Compile SCSS

```bash
docker-compose exec server python manage.py compilescss
```
