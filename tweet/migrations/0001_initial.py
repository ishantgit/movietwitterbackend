# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_sentiment', models.DecimalField(null=True, max_digits=5, decimal_places=5, blank=True)),
                ('tweet_text', models.ForeignKey(to='movie.Movie')),
            ],
        ),
    ]
