# -*- coding: utf-8 -*-

from django_jinja import library
from jinja2.filters import do_default

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form


@library.filter
def crispy(form):
    return as_crispy_form(form, label_class=form.helper.label_class, field_class=form.helper.field_class)


@library.filter
def default(value, default_value=u'', boolean=True):
    """Make the default filter, if used without arguments, behave like Django's own version.
    """
    return do_default(value, default_value, boolean)