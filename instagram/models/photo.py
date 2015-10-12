# -*- coding: utf-8 -*-

import os
from pilkit.lib import Image

from django.conf import settings
from django.db import models

from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from instagram.models.user import User


class Transpose(object):
    """
    Rotates or flips the image.
    """
    AUTO = 'auto'
    FLIP_HORIZONTAL = Image.FLIP_LEFT_RIGHT
    FLIP_VERTICAL = Image.FLIP_TOP_BOTTOM
    ROTATE_90 = Image.ROTATE_90
    ROTATE_180 = Image.ROTATE_180
    ROTATE_270 = Image.ROTATE_270

    methods = [AUTO]
    _EXIF_ORIENTATION_STEPS = {
        1: [],
        2: [FLIP_HORIZONTAL],
        3: [ROTATE_180],
        4: [FLIP_VERTICAL],
        5: [ROTATE_270, FLIP_HORIZONTAL],
        6: [ROTATE_270],
        7: [ROTATE_90, FLIP_HORIZONTAL],
        8: [ROTATE_90],
    }

    def __init__(self, *args):
        super(Transpose, self).__init__()
        if args:
            self.methods = args

    def process(self, img):
        if self.AUTO in self.methods:
            ops = []
            try:
                orientation = None
                try:
                    orientation = img._getexif()[0x0112]
                except OverflowError:
                    pass
                if orientation:
                    ops = self._EXIF_ORIENTATION_STEPS[orientation]
            except (KeyError, TypeError, AttributeError):
                pass
        else:
            ops = self.methods
        for method in ops:
            img = img.transpose(method)
        return img


class Photo(models.Model):
    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_HIDE_FROM_HOMEPAGE = 'hide_from_homepage'
    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_CHOICES = (
        (VISIBILITY_PUBLIC, 'Show on homepage'),
        (VISIBILITY_HIDE_FROM_HOMEPAGE, 'Hide from homepage'),
        (VISIBILITY_PRIVATE, 'Private'),
    )

    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=1024, blank=True, null=True, default='')
    user = models.ForeignKey(User)
    visibility = models.CharField(max_length=32, choices=VISIBILITY_CHOICES, default=VISIBILITY_PUBLIC, db_index=True)
    created = models.DateTimeField(blank=True, null=True, db_index=True, auto_now_add=True)

    photo = ProcessedImageField([Transpose(), ResizeToFit(5120, 4096, upscale=False)], format='JPEG',
                                options={'quality': 100, 'progressive': True}, max_length=255)
    width = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    photo_timeline = ImageSpecField(source='photo',
                                    processors=[ResizeToFit(600, 600, upscale=False)],
                                    format='JPEG',
                                    options={
                                        'quality': 70,
                                        'progressive': True
                                    },
                                    cachefile_strategy='imagekit.cachefiles.strategies.Optimistic')
    photo_timeline_2x = ImageSpecField(source='photo',
                                       processors=[ResizeToFit(1200, 1200, upscale=False)],
                                       format='JPEG',
                                       options={
                                           'quality': 70,
                                           'progressive': True
                                       },
                                       cachefile_strategy='imagekit.cachefiles.strategies.Optimistic')

    def __unicode__(self):
        return self.photo.name

    def delete(self, *args, **kwargs):
        media_root_dir = os.path.realpath(settings.MEDIA_ROOT)
        for spec in ['small']:
            field = getattr(self, '_'.join(('photo', spec)))
            if field.name:
                name = os.path.join(media_root_dir, field.name)
                if os.path.isfile(name) and os.path.exists(name):
                    os.remove(name)
        if self.photo:
            self.photo.delete(save=False)
        super(Photo, self).delete(*args, **kwargs)


class PhotoHashTags(models.Model):
    tag = models.CharField(max_length=255, db_index=True)
    photo = models.ForeignKey(Photo)
