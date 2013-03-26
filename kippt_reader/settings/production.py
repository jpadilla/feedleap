from os import environ

import dj_database_url

from .base import *


# INSTALLED_APPS += (
#     'djangosecure',
# )

# PRODUCTION_MIDDLEWARE_CLASSES = (
#     'djangosecure.middleware.SecurityMiddleware',
# )

# MIDDLEWARE_CLASSES = PRODUCTION_MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [DOMAIN]

# django-secure
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 15
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_FRAME_DENY = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_REDIRECT_EXEMPT = [
#     '^(?!hub/).*'
# ]
