from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'kippt_reader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hub/', include('libs.djpubsubhubbub.urls')),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('feeds_list'))),

    url(r'^auth/', include('apps.auth.urls')),
    url(r'^feeds/', include('apps.feeds.urls')),
)
