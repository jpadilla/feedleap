from os import environ

import dj_database_url

from .base import *


DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [DOMAIN]
