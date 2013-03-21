from django.conf import settings
from libs.djpubsubhubbub.models import Subscription

sub = Subscription.objects.subscribe(
    topic='http://push-pub.appspot.com/feed/',
    hub=settings.SUPERFEEDR_HUB,
    debug=True
)
