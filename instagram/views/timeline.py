# -*- coding: utf-8 -*-

from django.views.generic import View, TemplateView
from django.views.generic.base import ContextMixin


class BaseTimeline(TemplateView):
    template_name = 'timeline/base_timeline.jinja2'

    def get_context_data(self, **kwargs):
        super(BaseTimeline, self).get_context_data(**kwargs)
        return kwargs