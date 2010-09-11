from django.conf.urls.defaults import *

from murl.views import *

urlpatterns = patterns('murl.views',
    url(r'', redirect_url, name="redirect_url"),
)
