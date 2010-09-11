from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from api.handlers import MUrlHandler

auth = HttpBasicAuthentication(realm='MyUrl')
murl = Resource(handler=MUrlHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^url/(?P<murl>[^/]+)/?$', murl),
    url(r'^urls/?$', murl),
    url(r'^$', documentation_view),
)
