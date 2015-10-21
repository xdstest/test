# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.views.generic.edit import FormView

from instagram.models import Photo
from instagram.views.user import LoginRequiredMixin
from instagram.forms.photo import UploadPhotoForm, EditPhotoForm


class UploadPhoto(LoginRequiredMixin, FormView):
    form_class = UploadPhotoForm

    def get_success_url(self):
        return reverse('timeline-user', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        photo.update_tags()
        if self.request.is_ajax():
            return HttpResponse(status=204)
        return super(UploadPhoto, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return super(UploadPhoto, self).form_invalid(form)


class EditPhoto(LoginRequiredMixin, FormView):
    template_name = 'user/photo/edit.jinja2'
    form_class = EditPhotoForm

    def get_success_url(self):
        return reverse('timeline-user', kwargs={'username': self.request.user.username})

    def get_form_kwargs(self):
        kwargs = super(EditPhoto, self).get_form_kwargs()
        user = self.request.user
        if user.is_moderator:
            kwargs['instance'] = get_object_or_404(Photo, id=self.kwargs['photo_id'])
        else:
            kwargs['instance'] = get_object_or_404(Photo, id=self.kwargs['photo_id'], user=user)
        return kwargs

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.save()
        photo.update_tags()
        if self.request.is_ajax():
            return HttpResponse(status=204)
        return super(EditPhoto, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return super(EditPhoto, self).form_invalid(form)


class DeletePhoto(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        photo = None
        try:
            if user.is_moderator:
                photo = Photo.objects.get(id=self.kwargs['photo_id'])
            else:
                photo = Photo.objects.get(id=self.kwargs['photo_id'], user=user)
        except Photo.DoesNotExist:
            pass
        else:
            photo.delete()
        return '/'