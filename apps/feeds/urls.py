from django.conf.urls import patterns, url

from .views import FeedCreateView, FeedListView

urlpatterns = patterns(
    '',

    url(r'^$', FeedListView.as_view(), name='feeds_list'),
    url(r'^new/$', FeedCreateView.as_view(), name='feeds_create'),
)
