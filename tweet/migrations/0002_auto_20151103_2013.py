# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='tweet_sentiment',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_polarity',
            field=models.DecimalField(null=True, max_digits=25, decimal_places=20, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_subjectivity',
            field=models.DecimalField(null=True, max_digits=25, decimal_places=20, blank=True),
        ),
    ]
