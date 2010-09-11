from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include('api.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^(.*)/', 'murl.urls.redirect_url'),
)
