from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hub/', include('djpubsubhubbub.urls')),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('feeds_list'))),

    url(r'^auth/', include('apps.auth.urls')),
    url(r'^feeds/', include('apps.feeds.urls')),
)

# Serve statics during development
urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
)
