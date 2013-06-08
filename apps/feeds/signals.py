import requests
from djpubsubhubbub.signals import updated

from .models import Feed


def update_handler(sender, update, **kwargs):
    """
    Process new content being provided from SuperFeedr.
    Check if there is no existing clip for that URL
    before trying to create it.

    """

    feeds = Feed.objects.filter(feed_url=sender.topic)

    for feed in feeds:
        for entry in update.entries:
            r = requests.get(entry['link'])

            kippt = feed.created_by.kippt_client()

            clip = kippt.clips(params={'url': r.url})

            if clip['meta']['total_count'] == 0:
                if feed.list_id:
                    list_id = feed.list_id
                else:
                    list_id = feed.created_by.list_id

                kippt.clips.create(
                    r.url,
                    list_id,
                    title=entry['title'],
                    notes=entry['summary']
                )

updated.connect(update_handler, dispatch_uid='superfeedr')
