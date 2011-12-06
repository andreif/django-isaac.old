import os
import socket

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


DEBUG = False
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'development.db',
    }
}


TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.debug',)


MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)


ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'south',
    'compressor',
    'core',
    'gunicorn',
)
