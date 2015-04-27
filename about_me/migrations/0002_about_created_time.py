# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 14, 2, 39, 853922), auto_now_add=True),
            preserve_default=False,
        ),
    ]
