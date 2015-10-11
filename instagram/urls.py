from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.debug import sensitive_post_parameters

from views.user.sign import SignIn, SignUp, SignOut
from views.timeline import BaseTimeline


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', BaseTimeline.as_view(), {}, 'index'),

    url(r'^login/$', sensitive_post_parameters()(SignIn.as_view()), {}, 'user-sign-in'),
    url(r'^join/$', SignUp.as_view(), {}, 'user-sign-up'),
    url(r'^logout/$', SignOut.as_view(), {}, 'user-sign-out'),
]
