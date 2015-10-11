# -*- coding: utf-8 -*-

from crispy_forms.utils import render_crispy_form
from django_jinja import library
from jinja2 import contextfunction
from jinja2.filters import do_default


@contextfunction
@library.global_function
def crispy(context, form):
    return render_crispy_form(form, context=context)


@library.filter
def default(value, default_value=u'', boolean=True):
    """Make the default filter, if used without arguments, behave like Django's own version.
    """
    return do_default(value, default_value, boolean)