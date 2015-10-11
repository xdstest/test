# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper


class SingUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
