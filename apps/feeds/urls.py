from django.conf.urls import patterns, url

from .views import FeedCreateView, FeedListView, FeedDeleteView

urlpatterns = patterns(
    '',

    url(r'^$', FeedListView.as_view(), name='feeds_list'),
    url(r'^new/$', FeedCreateView.as_view(), name='feeds_create'),
    url(r'^delete/(?P<pk>[\w]+)/$', FeedDeleteView.as_view(), name='feeds_delete'),
)
