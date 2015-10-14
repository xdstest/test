# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import View, TemplateView
from django.views.generic.base import ContextMixin


from instagram.models import User, Photo
from instagram.views.user.photo import UploadPhoto


class BaseTimeline(TemplateView):
    ITEMS_PER_PAGE = 9
    template_name = 'timeline/base_timeline.jinja2'

    def get_context_data(self, **kwargs):
        context = {}
        context['user_can_edit_photos'] = self.request.user.is_authenticated() and self.request.user.is_moderator
        photos = Photo.objects.order_by('-created')
        if not context['user_can_edit_photos']:
            photos = photos.filter(visibility=Photo.VISIBILITY_PUBLIC)
        context['photos'] = photos[:self.ITEMS_PER_PAGE]
        return context


class UserTimeline(UploadPhoto, BaseTimeline):
    template_name = 'timeline/user_timeline.jinja2'

    def get_context_data(self, **kwargs):
        context = {}
        context['timeline_user'] = get_object_or_404(User, username=kwargs.get('username'))
        context['user_can_edit_photos'] = self.request.user.is_authenticated() and \
                            (self.request.user.is_moderator or self.request.user.id == context['timeline_user'].id)
        photos = Photo.objects.filter(user=context['timeline_user']).order_by('-created')
        if not context['user_can_edit_photos']:
            photos = photos.exclude(visibility=Photo.VISIBILITY_PRIVATE)
        context['timeline_user_posts'] = Photo.objects.filter(user=context['timeline_user']).count()
        context['photos'] = photos[:self.ITEMS_PER_PAGE]
        context['form'] = self.get_form()
        return context