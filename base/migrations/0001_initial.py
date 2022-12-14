# Generated by Django 4.1.4 on 2022-12-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.BigIntegerField(unique=True)),
                ('title', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
