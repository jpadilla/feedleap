import urllib
import feedparser
from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from djpubsubhubbub.models import Subscription, DEFAULT_LEASE_SECONDS
from djpubsubhubbub.signals import verified, updated, subscription_needs_update


@csrf_exempt
def callback(request, pk):
    if request.method == 'GET':
        try:
            mode = request.GET['hub.mode']
            topic = request.GET['hub.topic']
            challenge = request.GET['hub.challenge']
            lease_seconds = request.GET.get(
                'hub.lease_seconds',
                DEFAULT_LEASE_SECONDS,
            )
            verify_token = request.GET.get('hub.verify_token', '')
        except MultiValueDictKeyError:
            # Raise 404 instead of 500 error
            raise Http404

        try:
            subscription = Subscription.objects.get(
                pk=pk,
                topic=topic,
                verify_token=verify_token,
            )
        except Subscription.DoesNotExist:
            # XXX Hack. Hubs may re-encode already encoded 
            # data sent during the initial subscription request.
            # Do one last "unquote" just to be safe:
            topic = urllib.unquote(topic)
            try:
                subscription = Subscription.objects.get(
                    pk=pk,
                    topic=topic,
                    verify_token=verify_token,
                )
            except Subscription.DoesNotExist:
                raise Http404

        if mode == 'subscribe':
            if not verify_token.startswith('subscribe'):
                raise Http404

            subscription.verified = True
            subscription.is_subscribed = True
            subscription.set_expiration(int(lease_seconds))
            verified.send(sender=subscription)
        elif mode == 'unsubscribe':
            if not verify_token.startswith('unsubscribe'):
                raise Http404

            subscription.verified = False
            subscription.is_subscribed = False
            subscription.set_expiration(int(lease_seconds))

        return HttpResponse(challenge, content_type='text/plain')
    elif request.method == 'POST':
        subscription = get_object_or_404(Subscription, pk=pk)
        parsed = feedparser.parse(
            getattr(request, 'body', request.raw_post_data),
        )
        if parsed.feed.links: # single notification
            hub_url = subscription.hub
            self_url = subscription.topic
            for link in parsed.feed.links:
                if link['rel'] == 'hub':
                    hub_url = link['href']
                elif link['rel'] == 'self':
                    self_url = link['href']

            needs_update = False
            if hub_url and subscription.hub != hub_url:
                # hub URL has changed; let's update our subscription
                needs_update = True
            elif self_url != subscription.topic:
                # topic URL has changed
                needs_update = True

            if needs_update:
                subscription_needs_update.send(
                    sender=subscription,
                    hub_url=hub_url,
                    topic_url=self_url,
                )

            updated.send(sender=subscription, update=parsed)
            return HttpResponse('')
    return Http404
