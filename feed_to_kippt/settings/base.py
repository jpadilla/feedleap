import os
import site
import sys
"""
Django settings for feed_to_kippt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.5/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.5/ref/settings/
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(BASE_DIR)
SITE_NAME = os.path.basename(BASE_DIR)

prev_sys_path = list(sys.path)

site.addsitedir(os.path.join(SITE_ROOT, 'libs'))
site.addsitedir(os.path.join(SITE_ROOT, 'vendor'))

# Move the new items to the front of sys.path.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5wkx-h4q+php!%#w1+jj#p_$5!3-3651_7ssc0&f+t3+vx59-1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'south',
    'gunicorn',
    'widget_tweaks',

    'djpubsubhubbub',

    'apps.auth',
    'apps.feeds',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

ROOT_URLCONF = 'feed_to_kippt.urls'

WSGI_APPLICATION = 'feed_to_kippt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

MEDIA_URL = '/media/'

# Templates

TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(SITE_ROOT, 'templates')),
)

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# Project specifics

AUTH_USER_MODEL = 'auth.KipptUser'
LOGIN_URL = '/auth/connect/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.auth.backends.KipptUserBackend',
)

DOMAIN = os.getenv('DOMAIN')

# SuperFeedr
SUPERFEEDR_HUB = os.getenv('SUPERFEEDR_HUB')
SUPERFEEDR_USER = os.getenv('SUPERFEEDR_USERNAME')
SUPERFEEDR_PASS = os.getenv('SUPERFEEDR_PASSWORD')

# djpubsubhubbub
PUBSUBHUBBUB_CONFIG = 'feed_to_kippt.config.SubHubConfig'
