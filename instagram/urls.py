from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.debug import sensitive_post_parameters

from views.user.sign import SignIn, SignUp, SignOut
from views.timeline import BaseTimeline, UserTimeline, TagTimeline, TagUserTimeline


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', BaseTimeline.as_view(), name='index'),
    url(r'^tag/(?P<tag>[\w]+)/$', TagTimeline.as_view(), name='timeline-tag'),
    url(r'^user/(?P<username>[\w.@+-]+)/$', UserTimeline.as_view(), name='timeline-user'),
    url(r'^user/(?P<username>[\w.@+-]+)/tag/(?P<tag>[\w]+)/$', TagUserTimeline.as_view(), name='timeline-user-tag'),

    url(r'^login/$', sensitive_post_parameters()(SignIn.as_view()), name='user-sign-in'),
    url(r'^join/$', SignUp.as_view(), name='user-sign-up'),
    url(r'^logout/$', SignOut.as_view(), name='user-sign-out'),
]
