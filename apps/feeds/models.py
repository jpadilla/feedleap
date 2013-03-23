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
