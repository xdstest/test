from django.conf.urls import include, url
from django.contrib import admin

from views.user.sign import SignUp, SignOut
from views.timeline import BaseTimeline


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', BaseTimeline.as_view(), {}, 'index'),

    url(r'^login/$', BaseTimeline.as_view(), {}, 'user-sign-in'),
    url(r'^join/$', SignUp.as_view(), {}, 'user-sign-up'),
    url(r'^join/$', SignOut.as_view(), {}, 'user-sign-out'),
]
