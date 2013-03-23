from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy


from braces.views import LoginRequiredMixin

from .models import KipptUser
from .forms import KipptUserCreationForm, KipptUserSetupForm


class RegisterView(CreateView):
    model = KipptUser
    form_class = KipptUserCreationForm

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'],
                            api_token=form.cleaned_data['api_token'])
        if user is not None:
            login(self.request, user)

        return response


class SetupView(LoginRequiredMixin, UpdateView):
    model = KipptUser
    form_class = KipptUserSetupForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('auth_setup')
