# -*- coding: utf-8 -*-

import re

from django_jinja import library
from jinja2 import Markup
from jinja2.filters import do_default, escape

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@library.filter
def default(value, default_value=u'', boolean=True):
    """Make the default filter, if used without arguments, behave like Django's own version.
    """
    return do_default(value, default_value, boolean)


@library.filter
def nl2br(value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace(u'\n', u'<br>\n')
                          for p in _paragraph_re.split(unicode(escape(value))))
    return Markup(result)