from django.conf.urls import patterns, url


urlpatterns = patterns(
    'libs.djpubsubhubbub.views',
    url(r'^(\d+)/$', 'callback', name='pubsubhubbub_callback'),
)
