import os

import dj_database_url

from .base import *


INSTALLED_APPS += (
    'djangosecure',
)

PRODUCTION_MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
)

MIDDLEWARE_CLASSES = PRODUCTION_MIDDLEWARE_CLASSES + MIDDLEWARE_CLASSES

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [DOMAIN]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'assets'))

# django-secure
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 15
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
