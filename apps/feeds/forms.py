from django import forms
from django.conf import settings

import feedparser
from libs.djpubsubhubbub.models import Subscription

from .models import Feed


class FeedCreateForm(forms.ModelForm):

    class Meta:
        model = Feed
        fields = ('feed_url',)

    def clean_feed_url(self):
        feed_url = self.cleaned_data.get('feed_url')

        feed = feedparser.parse(feed_url)

        if feed.bozo:
            raise forms.ValidationError('Invalid Feed URL')

        return feed_url

    def save(self, commit=True):
        feed = super(FeedCreateForm, self).save(commit=False)

        if commit:
            feed.save()

        Subscription.objects.subscribe(
            topic=feed.feed_url,
            hub=settings.SUPERFEEDR_HUB,
            verify='async'
        )

        return feed
