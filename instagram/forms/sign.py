# -*- coding: utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from instagram.models import User


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Sign in'))

    class Meta:
        model = User
        fields = ("username",)


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Sign up'))

    class Meta:
        model = User
        fields = ("username",)
