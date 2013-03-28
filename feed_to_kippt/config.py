import base64

from django.conf import settings


class SubHubConfig(object):
    def get_extra_hub_headers(self, feed_url, hub_url):
        headers = {}
        if hub_url == settings.SUPERFEEDR_HUB:
            headers['Authorization'] = \
                'Basic %s' % base64.b64encode('%s:%s' % (
                    settings.SUPERFEEDR_USER,
                    settings.SUPERFEEDR_PASS,
                ))
        return headers

    def get_default_callback_host(self, feed_url, hub_url):
        return settings.DOMAIN
