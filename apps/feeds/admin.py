from django.contrib import admin

from .models import Feed, FeedEntry


class FeedEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'feed', 'feed', 'added_to_kippt')


admin.site.register(Feed)
admin.site.register(FeedEntry, FeedEntryAdmin)
