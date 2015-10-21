# -*- coding: utf-8 -*-

import re
from pilkit.lib import Image

from django.core.urlresolvers import reverse
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
    tag_re = ur'#([\w]+)'
    tag_re_with_hash = ur'(#([\w]+))'

    VISIBILITY_PUBLIC = 'public'
    VISIBILITY_HIDE_FROM_HOMEPAGE = 'hide_from_homepage'
    VISIBILITY_PRIVATE = 'private'
    VISIBILITY_CHOICES = (
        (VISIBILITY_PUBLIC, 'Show on homepage'),
        (VISIBILITY_HIDE_FROM_HOMEPAGE, 'Hide from homepage'),
        (VISIBILITY_PRIVATE, 'Private'),
    )

    id = models.AutoField(primary_key=True)
    caption = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(User)
    visibility = models.CharField(max_length=32, choices=VISIBILITY_CHOICES, default=VISIBILITY_PUBLIC, db_index=True)
    created = models.DateTimeField(blank=True, null=True, db_index=True, auto_now_add=True)

    photo = ProcessedImageField([Transpose(), ResizeToFit(5120, 4096, upscale=False)], format='JPEG',
                                options={'quality': 100, 'progressive': True}, max_length=255)
    width = models.IntegerField(blank=True, default=0)
    height = models.IntegerField(blank=True, default=0)
    width_photo_full = models.IntegerField(blank=True, default=0)
    height_photo_full = models.IntegerField(blank=True, default=0)

    photo_full = ImageSpecField(source='photo',
                                processors=[ResizeToFit(1200, 1200, upscale=False)],
                                format='JPEG',
                                options={
                                    'quality': 70,
                                    'progressive': True
                                },
                                cachefile_strategy='imagekit.cachefiles.strategies.Optimistic')
    photo_timeline = ImageSpecField(source='photo',
                                    processors=[ResizeToFill(300, 300, upscale=False)],
                                    format='JPEG',
                                    options={
                                        'quality': 70,
                                        'progressive': True
                                    },
                                    cachefile_strategy='imagekit.cachefiles.strategies.Optimistic')
    photo_timeline_2x = ImageSpecField(source='photo',
                                       processors=[ResizeToFit(600, 600, upscale=False)],
                                       format='JPEG',
                                       options={
                                           'quality': 70,
                                           'progressive': True
                                       },
                                       cachefile_strategy='imagekit.cachefiles.strategies.Optimistic')

    def __unicode__(self):
        return self.photo.name

    def delete(self, *args, **kwargs):
        # TODO: replace with django-storages
        # media_root_dir = os.path.realpath(settings.MEDIA_ROOT)
        # for spec in ['small']:
        #     field = getattr(self, '_'.join(('photo', spec)))
        #     if field.name:
        #         name = os.path.join(media_root_dir, field.name)
        #         if os.path.isfile(name) and os.path.exists(name):
        #             os.remove(name)
        # if self.photo:
        #     self.photo.delete(save=False)
        super(Photo, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        if not all([self.width, self.height]) and self.photo:
            self.width = self.photo.width
            self.height = self.photo.height
            self.width_photo_full = self.photo_full.width
            self.height_photo_full = self.photo_full.height
            super(Photo, self).save(*args, **kwargs)

    @classmethod
    def _parse_tags_from_caption(cls, caption):
        return set(re.findall(cls.tag_re, caption, re.I + re.U))

    def update_tags(self):
        old_tags = {item.tag: item.id for item in self.phototag_set.all()}
        existed_tags = []
        new_tags = self._parse_tags_from_caption(self.caption)

        # delete old tags
        ids = []
        for tag, tag_id in old_tags.iteritems():
            if tag not in new_tags:
                ids.append(tag_id)
            else:
                existed_tags.append(tag)
        if ids:
            self.phototag_set.filter(pk__in=ids).delete()

        for tag in new_tags:
            if tag not in existed_tags:
                obj = PhotoTag(photo=self, tag=tag)
                self.phototag_set.add(obj)

    def as_dict(self):
        return {
            'id': self.id,
            'caption': self.caption,
            'visibility': self.visibility,
            'photo_full_url': self.photo_full.url,
            'width_photo_full': self.width_photo_full,
            'height_photo_full': self.height_photo_full,
            'photo_timeline_url': self.photo_timeline.url,
            'photo_timeline_2x_url': self.photo_timeline_2x.url,
            'user_username': self.user.username,
            'user_url': reverse('timeline-user', kwargs={'username': self.user.username}),
        }


class PhotoTag(models.Model):
    tag = models.CharField(max_length=255, db_index=True)
    photo = models.ForeignKey(Photo)

    class Meta:
        unique_together = (('tag', 'photo'),)
