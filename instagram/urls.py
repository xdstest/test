from django.conf.urls import include, url
from django.contrib import admin

from views.timeline import BaseTimeline


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', BaseTimeline.as_view(), {}, 'index'),

     url(r'^login/$', BaseTimeline.as_view(), {}, 'user-sing-in'),
]
