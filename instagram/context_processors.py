# -*- coding: utf-8 -*-

from django.conf import settings as django_settings


def settings(request):
    return {
        'settings': django_settings,
    }


def user(request):
    return {
        'user': request.user if request.user.is_authenticated() and request.user.is_active else None,
    }