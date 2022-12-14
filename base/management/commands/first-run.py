from django.core.management.base import BaseCommand
from base.models import Article
from datetime import datetime
from django.utils import timezone
import requests
import environ

env = environ.Env()


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles_ids = requests.get(
            env('BASE_URL') + 'topstories.json').json()
        for id in articles_ids:
            article = requests.get(
                env('BASE_URL') + 'item/' + str(id) + '.json').json()
            if 'url' in article:
                url = article['url']
            else:
                url = ''
            Article.objects.create(article_id=id, title=article['title'], url=url,
                                   points=article['score'], created_at=datetime
                                   .fromtimestamp(article['time'], tz=timezone.utc))
