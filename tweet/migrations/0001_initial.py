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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('polarity', models.DecimalField(max_digits=25, null=True, blank=True, decimal_places=20)),
                ('subjectivity', models.DecimalField(max_digits=25, null=True, blank=True, decimal_places=20)),
                ('movie', models.ForeignKey(null=True, to='movie.Movie')),
            ],
        ),
    ]
