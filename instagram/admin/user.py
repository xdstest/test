# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )


class PermissionAdmin(admin.ModelAdmin):
    list_filter = ('content_type',)
    search_fields = ('name',)