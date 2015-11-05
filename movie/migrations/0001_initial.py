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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(max_length=200, null=True)),
                ('langage', models.CharField(max_length=200, null=True)),
                ('imdbRating', models.CharField(max_length=200, null=True)),
                ('plot', models.TextField(null=True)),
                ('actor', models.CharField(max_length=200, null=True)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('director', models.CharField(max_length=200, null=True)),
                ('poster', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
