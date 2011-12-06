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
    'middleware.UrlMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_PORT = 587


ROOT_URLCONF = 'urls'
REMOVE_WWW = True


INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'south',
    'compressor',
    'core',
    'gunicorn',
)
