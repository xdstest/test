# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.hashers import make_password

from instagram.models import User
from django.contrib.auth.models import Group


class Migration(migrations.Migration):

    def create_admin_user(apps, schema_editor):
        admin = User(
            username='admin',
            password=make_password('admin'),
            is_superuser=True,
            is_staff=True
        )
        admin.save()
        group_moderators = Group.objects.create(name="moderators")
        group_users = Group.objects.create(name="users")
        admin.groups.add(group_moderators)

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
