# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView

from instagram.views.user import LoginRequiredMixin
from instagram.forms.photo import UploadPhotoForm


class UploadPhoto(LoginRequiredMixin, FormView):
    success_url = '/'
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