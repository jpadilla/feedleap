from libs.djpubsubhubbub.signals import updated

from .models import Feed


def update_handler(sender, update, **kwargs):
    """
    Process new content being provided from SuperFeedr

    """

    print sender.topic

    users = []
    feeds = Feed.objects.filter(feed_url=sender.topic)

    for feed in feeds:
        if feed.created_by not in users:
            users.append(feed.created_by)

    for user in users:
        kippt = user.kippt_client()

        for entry in update.entries:
            title = entry['title']
            summary = entry['summary']
            link = entry['link']

            kippt.addClip(link, user.list_id, title=title, notes=summary)

updated.connect(update_handler, dispatch_uid='superfeedr')
