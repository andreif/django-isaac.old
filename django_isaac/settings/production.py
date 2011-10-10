DEBUG = False
TEMPLATE_DEBUG = DEBUG


# For database and email settings.
from site_settings import *


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'isaacbythewood',
        'TIMEOUT': 60 * 15,
    }
}
CACHE_MIDDLEWARE_SECONDS = 60 * 15


from settings.essentials import *
