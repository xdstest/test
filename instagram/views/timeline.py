# -*- coding: utf-8 -*-

from django.views.generic import View, TemplateView
from django.views.generic.base import ContextMixin

from instagram.views.user.photo import UploadPhoto


class BaseTimeline(TemplateView):
    template_name = 'timeline/base_timeline.jinja2'

    def get_context_data(self, **kwargs):
        context = super(BaseTimeline, self).get_context_data(**kwargs)
        return context


class UserTimeline(UploadPhoto, BaseTimeline):
    template_name = 'timeline/user_timeline.jinja2'

    def get_context_data(self, **kwargs):
        context = super(BaseTimeline, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context