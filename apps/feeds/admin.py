from django.contrib import admin

from .models import Feed, FeedEntry


class FeedAdmin(admin.ModelAdmin):
    list_display = ('feed_url', 'created_by')


class FeedEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'feed',
                    'feed_created_by', 'added_to_kippt')

    def feed_created_by(self, obj):
        return obj.feed.created_by
    feed_created_by.short_description = 'Created by'


admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedEntry, FeedEntryAdmin)
