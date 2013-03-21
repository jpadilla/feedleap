from os import environ

import dj_database_url

from .base import *


DOMAIN = 'kippt-reader.herokaupp.com'

DATABASES = {'default': dj_database_url.config()}

SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [DOMAIN]
