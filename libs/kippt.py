import json
import inspect
import urllib

import requests


API_ENDPOINT = 'https://kippt.com/api'


class Kippt(object):

    def __init__(self, username, api_token=None, password=None):
        self.username = username
        self.api_token = api_token

        headers = {
            'X-Kippt-Username': username,
            'X-Kippt-API-Token': api_token,
            'X-Kippt-Client': 'Kippt-Python,jose@jpadilla.com,jpadilla.com',
            'content-type': 'application/json'
        }

        self.session = requests.session()

        if api_token:
            default_headers = self.session.headers
            self.session.headers = dict(default_headers.items() + headers.items())
        elif password:
            self.session.auth = (username, password)

        # Dynamically enable endpoints
        self._attach_endpoints()

    def _attach_endpoints(self):
        """Dynamically attach endpoint callables to this client"""
        for name, endpoint in inspect.getmembers(self):
            is_class = inspect.isclass(endpoint)
            is_subclass = is_class and issubclass(endpoint, self.Endpoint)
            not_endpoint = endpoint is not self.Endpoint

            if is_subclass and not_endpoint:
                endpoint_instance = endpoint(self.session)
                setattr(self, name.lower(), endpoint_instance)

    class Endpoint(object):

        def __init__(self, session):
            self.session = session
            self.endpoint = self.__class__.__name__.lower()

        def _expanded_path(self, path=None):
            if path:
                path = (self.endpoint, str(path))
            else:
                path = (self.endpoint, )

            return '/{expanded_path}'.format(
                expanded_path='/'.join(p for p in path if p)
            )

        def _generate_url(self, path, params):
            if params:
                return '{API_ENDPOINT}{path}/?{params}'.format(
                    API_ENDPOINT=API_ENDPOINT,
                    path=self._expanded_path(path),
                    params=urllib.urlencode(params)
                )
            else:
                return '{API_ENDPOINT}{path}/'.format(
                    API_ENDPOINT=API_ENDPOINT,
                    path=self._expanded_path(path)
                )

        def _process_request(self, request):
            try:
                return request.json()
            except ValueError:
                return request.raise_for_status()

        def _request(self, method, url, payload=None):
            request = self.session.request(method, url, data=json.dumps(payload))
            return self._process_request(request)

        def get(self, path=None, params={}):
            url = self._generate_url(path, params)
            return self._request(method='get', url=url)

        def post(self, path=None, params={}):
            url = self._generate_url(path, None)
            return self._request(method='post', url=url, payload=params)

        def put(self, path=None, params={}):
            url = self._generate_url(path, params)
            return self._request(method='put', url=url, payload=params)

        def delete(self, path=None):
            url = self._generate_url(path, None)
            return self._request(method='delete', url=url)

    class ApiResource(Endpoint):
        def __call__(self, identifier=None, params={}):
            return self.get(path=identifier, params=params)

        def create(self, params={}):
            return self.post(params=params)

        def update(self, identifier, params={}):
            return self.put(path=identifier, params=params)

        def delete(self, identifier):
            return super(Kippt.ApiResource, self).delete(path=identifier)

    class Account(ApiResource):
        pass

    class Lists(ApiResource):
        def __call__(self, limit=0, offset=0):
            params = {
                'limit': limit,
                'offset': offset
            }

            data = self.get(path=None, params=params)

            return data['meta'], data['objects']

    class Clips(ApiResource):
        def create(self, url, list_id=None, title=None, starred=None, notes=None):
            clip_data = {
                'url': url,
            }

            if list_id:
                clip_data['list'] = '/api/lists/{}'.format(list_id)

            if title:
                clip_data['title'] = title

            if starred:
                clip_data['is_starred'] = starred

            if notes:
                clip_data['notes'] = notes

            return super(Kippt.Clips, self).create(params=clip_data)
