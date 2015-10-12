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


def webpack_dev(request):
    return {
        # поддержка webpack
        'webpack_dev': True if django_settings.DEBUG and 'PhantomJS' not in request.META.get('HTTP_USER_AGENT') \
            else False
    }