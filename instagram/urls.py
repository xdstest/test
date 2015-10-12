from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.debug import sensitive_post_parameters

from views.user.sign import SignIn, SignUp, SignOut
from views.timeline import BaseTimeline, UserTimeline


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', BaseTimeline.as_view(), name='index'),
    url(r'^user/(?P<username>[\w.@+-]+)/$', UserTimeline.as_view(), name='timeline-user'),

    url(r'^login/$', sensitive_post_parameters()(SignIn.as_view()), name='user-sign-in'),
    url(r'^join/$', SignUp.as_view(), name='user-sign-up'),
    url(r'^logout/$', SignOut.as_view(), name='user-sign-out'),
]
