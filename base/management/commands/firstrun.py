from django.core.management.base import BaseCommand
from base.models import Article
from datetime import datetime
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        articlesIds = requests.get(
            'https://hacker-news.firebaseio.com/v0/topstories.json').json()
        for id in articlesIds:
            article = requests.get(
                'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json').json()
            if 'url' in article:
                url = article['url']
            else:
                url = ''
            Article.objects.create(article_id=id, title=article['title'], url=url,
                                   points=article['score'], created_at=datetime.fromtimestamp(article['time']))
