# -*- coding: utf-8 -*-

import factory

from instagram.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'test_user%d' % n)
