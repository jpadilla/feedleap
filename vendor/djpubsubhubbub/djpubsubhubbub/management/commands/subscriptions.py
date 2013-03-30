from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings
from djpubsubhubbub.models import Subscription


class Command(BaseCommand):
    args = '<topic_url topic_url ...>'
    help = 'Subscribes/Unsubscribes to a topic URL'
    option_list = BaseCommand.option_list + (
        make_option(
            '--unsubscribe',
            action='store_true',
            dest='unsubscribe',
            default=False,
            help='Unsubscribe a topic URL instead of susbscribing to it.'),
    )

    def handle(self, *args, **options):
        for topic_url in args:
            if options.get('unsubscribe', False):
                sub = Subscription.objects.unsubscribe(
                    topic=topic_url,
                    hub=settings.SUPERFEEDR_HUB,
                )

                self.stdout.write('Successfully unsubscribed %s' % sub)
            else:
                sub = Subscription.objects.subscribe(
                    topic=topic_url,
                    hub=settings.SUPERFEEDR_HUB,
                )

                self.stdout.write('Successfully unsubscribed %s' % sub)
