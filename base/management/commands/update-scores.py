from django.core.management.base import BaseCommand
from base.models import Article
import requests
import environ

env = environ.Env()


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = Article.objects.all()

        for article in articles:
            new_article = requests.get(
                env('BASE_URL') + 'item/' + str(article.article_id) + '.json').json()
            if article.points != new_article['score']:
                article.points = new_article['score']
                article.save()
