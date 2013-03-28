from django.conf.urls.defaults import *


urlpatterns = patterns('djpubsubhubbub.views',
    url(r'^(\d+)/$',
        'callback',
        name='pubsubhubbub_callback'),
)
