from django.conf.urls import patterns, url
from .views import RegisterView, SetupView

urlpatterns = patterns(
    '',

    url(r'^register/$', RegisterView.as_view(), name='auth_register'),
    url(r'^setup/$', SetupView.as_view(), name='auth_setup'),
)
