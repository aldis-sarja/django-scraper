from django.core.management.base import BaseCommand
from base.models import Article
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = Article.objects.all()

        for article in articles:
            new_article = requests.get(
                'https://hacker-news.firebaseio.com/v0/item/' + str(article.article_id) + '.json').json()
            if article.points != new_article['score']:
                article.points = new_article['score']
                article.save()
