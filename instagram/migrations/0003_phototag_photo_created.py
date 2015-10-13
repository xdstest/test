# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='phototag',
            name='photo_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 2, 44, 50, 753987), db_index=True),
            preserve_default=False,
        ),
    ]
