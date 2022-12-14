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
            new_article = requests.get(
                env('BASE_URL') + 'item/' + str(id) + '.json').json()
            try:
                Article.objects.get(article_id=id)

            except Article.DoesNotExist:
                if 'url' in new_article:
                    url = new_article['url']
                else:
                    url = ''
                Article.objects.create(article_id=id, title=new_article['title'], url=url,
                                       points=new_article['score'], created_at=datetime.fromtimestamp(new_article['time'], tz=timezone.utc))
