# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('movie_genre', models.CharField(default=b'n/a', max_length=200, null=True)),
                ('movie_langage', models.CharField(default=b'n/a', max_length=200, null=True)),
                ('movie_imdbRating', models.CharField(default=b'n,a', max_length=200, null=True)),
                ('movie_plot', models.TextField(default=b'n/a', null=True)),
                ('movie_actor', models.CharField(default=b'n/a', max_length=200, null=True)),
                ('movie_writer', models.CharField(default=b'n/a', max_length=200, null=True)),
                ('movie_director', models.CharField(default=b'n/a', max_length=200, null=True)),
            ],
        ),
    ]
