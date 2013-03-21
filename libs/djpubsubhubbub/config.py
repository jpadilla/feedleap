from easyconfig import EasyConfig


class Config(object):
    ''' Base config class to easily pass headers, etc.
    '''
    config = EasyConfig('djpubsubhubbub.Config', 'PUBSUBHUBBUB_CONFIG')

    def get_extra_hub_headers(self, feed_url, hub_url):
        return self.config.get_object(
            'get_extra_hub_headers',
            {},
            *(feed_url, hub_url)
        )

    def get_default_callback_host(self, feed_url, hub_url):
        return self.config.get_object(
            'get_default_callback_host',
            {},
            *(feed_url, hub_url)
        )
