from django.db import models

# Create your models here.


class Article(models.Model):
    article_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    points = models.IntegerField()
    created_at = models.DateTimeField()
