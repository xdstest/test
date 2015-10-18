# -*- coding: utf-8 -*-

import json

from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


from instagram.models import User, Photo
from instagram.views.user.photo import UploadPhoto


class TagTimelineMixin(object):
    def _photos_set(self, **kwargs):
        return Photo.objects.filter(phototag__tag=kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super(TagTimelineMixin, self).get_context_data(**kwargs)
        if not context['photos']:
            raise Http404()
        return context


class BaseTimeline(TemplateView):
    ITEMS_PER_PAGE = 3
    template_name = 'timeline/base_timeline.jinja2'

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('type') == 'api':
            context = self.get_context_data_api(**kwargs)
            return JsonResponse(context)
        else:
            return super(BaseTimeline, self).dispatch(request, *args, **kwargs)

    def _photos_set(self, **kwargs):
        return Photo.objects

    def fill_context_photos_data(self, context, **kwargs):
        context['user_can_edit_photos'] = self.request.user.is_authenticated() and self.request.user.is_moderator
        photos = self._photos_set(**kwargs)
        if not context['user_can_edit_photos']:
            photos = photos.filter(visibility=Photo.VISIBILITY_PUBLIC)
        context['photos'] = photos.order_by('-created')

    def get_context_gallery_json_data(self, context, **kwargs):
        gallery_data = {
            'userCanEditPhotos': context['user_can_edit_photos'],
            'apiEndpoint': '/api' + self.request.path,
            'photos': [photo.as_dict() for photo in context['photos']]
        }
        return json.dumps(gallery_data, ensure_ascii=False)

    def get_context_data(self, **kwargs):
        context = {}
        self.fill_context_photos_data(context, **kwargs)
        context['photos'] = context['photos'][:self.ITEMS_PER_PAGE]
        context['gallery_data'] = self.get_context_gallery_json_data(context, **kwargs)
        return context

    def get_context_data_api(self, **kwargs):
        context = {}
        self.fill_context_photos_data(context, **kwargs)
        try:
            offset = int(self.request.GET.get('offset', 0))
        except (TypeError, ValueError):
            offset = 0
        photos = context['photos'][offset:(offset + self.ITEMS_PER_PAGE)]
        return {
            'photos': [photo.as_dict() for photo in photos]
        }


class TagTimeline(TagTimelineMixin, BaseTimeline):
    pass


class UserTimeline(UploadPhoto, BaseTimeline):
    template_name = 'timeline/user_timeline.jinja2'

    def fill_context_photos_data(self, context, **kwargs):
        context['timeline_user'] = get_object_or_404(User, username=kwargs.get('username'))
        context['user_can_edit_photos'] = self.request.user.is_authenticated() and (
            self.request.user.is_moderator or self.request.user.id == context['timeline_user'].id)
        photos = self._photos_set(**kwargs).filter(user=context['timeline_user'])
        if not context['user_can_edit_photos']:
            photos = photos.exclude(visibility=Photo.VISIBILITY_PRIVATE)
        context['photos'] = photos.order_by('-created')

    def get_context_data(self, **kwargs):
        context = {}
        self.fill_context_photos_data(context, **kwargs)
        context['photos'] = context['photos'][:self.ITEMS_PER_PAGE]
        context['timeline_user_posts'] = Photo.objects.filter(user=context['timeline_user']).count()
        context['form'] = self.get_form()
        context['gallery_data'] = self.get_context_gallery_json_data(context, **kwargs)
        return context


class TagUserTimeline(TagTimelineMixin, UserTimeline):
    pass