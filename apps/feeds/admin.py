from django.contrib import admin

from .models import Feed, FeedEntry

admin.site.register(Feed)
admin.site.register(FeedEntry)
