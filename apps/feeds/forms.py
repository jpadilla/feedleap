from django import forms
from django.conf import settings

import feedparser
from djpubsubhubbub.models import Subscription

from .models import Feed


class FeedCreateForm(forms.ModelForm):
    list_id = forms.ChoiceField(label='List (optional)', required=False)

    class Meta:
        model = Feed
        fields = ('feed_url', 'list_id')

    def __init__(self, user, *args, **kwargs):
        super(FeedCreateForm, self).__init__(*args, **kwargs)

        self.user = user
        kippt = user.kippt_client()
        meta, lists = kippt.lists()

        LIST_CHOICES = [('', 'Choose a list to store feed items')]

        for kippt_list in lists:
            LIST_CHOICES.append((kippt_list['id'], kippt_list['title']))

        self.fields['list_id'].choices = LIST_CHOICES

    def clean_feed_url(self):
        feed_url = self.cleaned_data.get('feed_url')

        feed = feedparser.parse(feed_url)

        if feed.bozo:
            raise forms.ValidationError('Invalid Feed URL')

        if not self.instance.pk:
            feeds = Feed.objects.filter(created_by=self.user,
                                        feed_url=feed_url)

            if feeds.exists():
                raise forms.ValidationError('Already subscribed to this feed')

        return feed_url

    def clean_list_id(self):
        list_id = self.cleaned_data.get('list_id')

        if not list_id or self.user.list_id == int(list_id):
            return None

        return list_id

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
