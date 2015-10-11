# -*- coding: utf-8 -*-

from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    """
    Based on django.contrib.auth.models.AbstractUser
    """
    username = models.CharField('username', max_length=30, unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      'Enter a valid username. '
                                      'This value may contain only letters, numbers '
                                      'and @/./+/-/_ characters.'), 'invalid',
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        })
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

