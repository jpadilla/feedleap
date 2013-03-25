from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from .views import ConnectView, SetupView

urlpatterns = patterns(
    '',

    url(r'^connect/$', ConnectView.as_view(), name='auth_connect'),
    url(r'^setup/$', SetupView.as_view(), name='auth_setup'),
    url(r'^logout/$', auth_views.logout, {
        'next_page': reverse_lazy('auth_connect')
        }, name='auth_logout')
)
