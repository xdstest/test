# -*- coding: utf-8 -*-

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from instagram.models import Photo


class UploadPhotoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadPhotoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Photo
        fields = ("photo", "caption", "visibility")

