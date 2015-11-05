# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_movie_poster'),
        ('tweet', '0002_auto_20151103_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_movie',
            field=models.ForeignKey(to='movie.Movie', null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
