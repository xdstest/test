# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20151015_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phototag',
            name='photo_created',
        ),
    ]
