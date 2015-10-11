# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView

from instagram.forms.sign import SignUpForm


class SignUp(FormView):
    template_name = 'user/sign_up.jinja2'
    form_class = SignUpForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_active:
            return HttpResponseRedirect(self.get_success_url())
        return super(SignUp, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        auth.login(self.request, user)
        return super(SignUp, self).form_valid(form)


class SignOut(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        HttpResponseRedirect('/')