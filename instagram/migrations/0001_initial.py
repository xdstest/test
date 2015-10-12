# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings
import imagekit.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={b'unique': b'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', b'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], help_text=b'Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name=b'username')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('caption', models.TextField(default=None, null=True, blank=True)),
                ('visibility', models.CharField(default=b'public', max_length=32, db_index=True, choices=[(b'public', b'Show on homepage'), (b'hide_from_homepage', b'Hide from homepage'), (b'private', b'Private')])),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, null=True)),
                ('photo', imagekit.models.fields.ProcessedImageField(max_length=255, upload_to=b'')),
                ('width', models.IntegerField(default=0, blank=True)),
                ('height', models.IntegerField(default=0, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255, db_index=True)),
                ('photo', models.ForeignKey(to='instagram.Photo')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='phototag',
            unique_together=set([('tag', 'photo')]),
        ),
    ]
