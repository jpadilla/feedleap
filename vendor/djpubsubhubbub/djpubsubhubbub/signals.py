from django.dispatch import Signal


pre_subscribe = Signal(providing_args=['created'])
verified = Signal()
updated = Signal(providing_args=['update'])
subscription_needs_update = Signal(providing_args=['hub_url', 'topic_url'])
