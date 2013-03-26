from libs.djpubsubhubbub.signals import updated

from .models import Feed, FeedEntry


def update_handler(sender, update, **kwargs):
    """
    Process new content being provided from SuperFeedr

    """

    feeds = Feed.objects.filter(feed_url=sender.topic)

    for feed in feeds:
        for entry in update.entries:
            feed_entry = FeedEntry.objects.create(
                title=entry['title'],
                summary=entry['summary'],
                link=entry['link'],
                feed=feed
            )

            feed_entry.add_to_kipt()

updated.connect(update_handler, dispatch_uid='superfeedr')
