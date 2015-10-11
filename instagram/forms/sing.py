# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SingUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Sing up'))
