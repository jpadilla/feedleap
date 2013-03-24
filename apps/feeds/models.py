import datetime

from django.utils.timezone import utc
from django.db import models
from django.conf import settings


class Feed(models.Model):
    feed_url = models.URLField()
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
        return '{} - {}'.format(self.title, self.link)

    def add_to_kipt(self):
        if not self.added_to_kippt:
            user = self.feed.created_by
            kippt = user.kippt_client()

            kippt.addClip(
                self.link,
                user.list_id,
                title=self.title,
                notes=self.summary
            )

            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            self.added_to_kippt = True
            self.date_added_to_kippt = now
            self.save()
