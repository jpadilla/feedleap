from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from .views import RegisterView, SetupView
from .forms import KipptUserAuthForm

urlpatterns = patterns(
    '',

    url(r'^register/$', RegisterView.as_view(), name='auth_register'),
    url(r'^setup/$', SetupView.as_view(), name='auth_setup'),
    url(r'^login/$', auth_views.login, {
        'template_name': 'auth/login_form.html',
        'authentication_form': KipptUserAuthForm
        }, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {
        'next_page': reverse_lazy('auth_login')
        }, name='auth_logout')
)
