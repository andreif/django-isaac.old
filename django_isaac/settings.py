import os
import socket

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
HOSTNAME = socket.gethostname()

if HOSTNAME == 'nebula':
    DEBUG = False

    # For database and email settings.
    from site_settings import *

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': 'isaacbythewood',
        }
    }

    CACHE_MIDDLEWARE_SECONDS = 60 * 15
else:
    DEBUG = True

    INTERNAL_IPS = ('127.0.0.1',)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(SITE_ROOT, 'development.db')
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'core/templates/'),
)
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.debug',)

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'core/static/'),
)
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'south',
    'compressor',
    'core',
    'gunicorn',
)
