from django.views.generic import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .models import KipptUser
from .forms import KipptUserConnectForm, KipptUserSetupForm


class ConnectView(CreateView):
    model = KipptUser
    form_class = KipptUserConnectForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse_lazy('feeds_list'))

        return super(ConnectView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        obj, created = form.save()
        user = authenticate(username=obj.username, api_token=obj.api_token)

        if user is not None:
            login(self.request, user)

        if created:
            redirect_to = reverse_lazy('auth_setup')
        else:
            redirect_to = reverse_lazy('feeds_list')

        return redirect(redirect_to)


class SetupView(LoginRequiredMixin, UpdateView):
    model = KipptUser
    form_class = KipptUserSetupForm
    success_url = reverse_lazy('feeds_list')

    def get_object(self):
        return self.request.user
