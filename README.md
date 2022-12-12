# Scraper app backend

Built with Python and Django
This is backend part of the app. For frontend look to [Scraper frontend]()

## Installation

Install pipenv, if You haven't already.

```bash
pipenv install pipenv
```

Pipenv is for the virtual environment. Actually, You can set up everything without pipenv. Then every package will be installed globally.

```bash
git clone https://github.com/aldis-sarja/django-scraper.git
cd django-scraper
pipenv install
```

Rename the file `.env.example` to `.env`, or make a copy:

```bash
cp .env.example .env
```

Configure your MySQL database:

```dosini
DB_NAME=<your-db-name>
DB_USERNAME=<your-db-user-name>
DB_PASSWORD=<your-password>
DB_HOST=localhost
DB_PORT=3306
```

Generate key for app

```bash
pipenv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy generated key in .env file

```dosini
SECRET_KEY=<your-key>
```

Now initialize database and populate with data from news.ycombinator.com:

```bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py first-run
```

You can then update the scores records and add new articles from time to time:

```bash
pipenv run python manage.py update-scores
pipenv run python manage.py update-news
```

## Usage

Run server:

```bash
pipenv python manage.py runserver
```

Install and run frontend part.

## API

- `/api` Get first 10 articles (first page).

```
{
    "total_pages":,
    "articles": [
        {
            "id":,
            "article_id":,
            "title":,
            "url":,
            "points":,
            "created_at":
        },
    ]
}
```

---

- `/api/?page=2` Get the next 10 articles (second page).