# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0002_about_created_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ('-created_time',)},
        ),
    ]
