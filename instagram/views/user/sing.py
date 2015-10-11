# -*- coding: utf-8 -*-

from django.views.generic import View, TemplateView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormView

from instagram.forms.sing import SingUpForm


class SingUp(FormView):
    template_name = 'user/sing_up.jinja2'
    form_class = SingUpForm
    success_url = '/'
