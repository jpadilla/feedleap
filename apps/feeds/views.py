from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .models import Feed
from .forms import FeedCreateForm


class FeedCreateView(LoginRequiredMixin, CreateView):
    model = Feed
    form_class = FeedCreateForm
    success_url = reverse_lazy('feeds_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(FeedCreateView, self).form_valid(form)


class FeedListView(LoginRequiredMixin, ListView):
    model = Feed

    def get_queryset(self):
        return Feed.objects.filter(created_by=self.request.user)
