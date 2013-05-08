from django.db import models
from django.conf import settings


class Feed(models.Model):
    feed_url = models.URLField()
    list_id = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('feed_url', 'created_by')

    def __unicode__(self):
        return self.feed_url


class FeedEntry(models.Model):
    title = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    link = models.URLField()
    feed = models.ForeignKey(Feed)

    added_to_kippt = models.BooleanField(default=False)
    date_added_to_kippt = models.DateTimeField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'feed entries'

    def __unicode__(self):
        return self.title
