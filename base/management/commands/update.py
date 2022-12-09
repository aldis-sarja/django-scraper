from django.core.management.base import BaseCommand
from base.models import Article
from datetime import datetime
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        articlesIds = requests.get(
            'https://hacker-news.firebaseio.com/v0/topstories.json').json()
        for id in articlesIds:
            newArticle = requests.get(
                'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json').json()
            try:
                article = Article.objects.get(article_id=id)

                if (article.points != newArticle['score']):
                    article.points = newArticle['score']
                    article.save()

            except Article.DoesNotExist:
                if 'url' in newArticle:
                    url = newArticle['url']
                else:
                    url = ''
                Article.objects.create(article_id=id, title=newArticle['title'], url=url,
                                    points=newArticle['score'], created_at=datetime.fromtimestamp(newArticle['time']))
