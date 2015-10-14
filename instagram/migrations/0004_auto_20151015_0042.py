# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_phototag_photo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='height_photo_full',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='width_photo_full',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
