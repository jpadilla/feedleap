from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from braces.views import LoginRequiredMixin

from .models import Feed
from .forms import FeedCreateForm


class FeedListView(LoginRequiredMixin, ListView):
    model = Feed

    def get_queryset(self):
        return Feed.objects.filter(created_by=self.request.user)


class FeedCreateView(LoginRequiredMixin, CreateView):
    model = Feed
    form_class = FeedCreateForm
    success_url = reverse_lazy('feeds_list')

    def get_initial(self):
        source = self.request.GET.get('source')
        feed = self.request.GET.get('feed')

        if source == 'subtome' and feed:
            return {
                'feed_url': feed
            }

    def get_form_kwargs(self, **kwargs):
        kwargs = super(FeedCreateView, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(FeedCreateView, self).form_valid(form)


class FeedUpdateView(LoginRequiredMixin, UpdateView):
    model = Feed
    form_class = FeedCreateForm
    success_url = '/feeds/edit/%(id)s/'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(FeedUpdateView, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        obj = super(FeedUpdateView, self).get_object()

        if obj.created_by == self.request.user:
            return obj

    def get(self, request, *args, **kwargs):
        response = super(FeedUpdateView, self).get(request, *args, **kwargs)

        if not self.object:
            return redirect(reverse_lazy('feeds_list'))

        return response


class FeedDeleteView(LoginRequiredMixin, DeleteView):
    model = Feed
    success_url = reverse_lazy('feeds_list')

    def get_object(self, queryset=None):
        obj = super(FeedDeleteView, self).get_object()

        if obj.created_by == self.request.user:
            return obj
