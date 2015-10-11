# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Permission

from instagram.models import (User)

from .user import UserAdmin, PermissionAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Permission, PermissionAdmin)