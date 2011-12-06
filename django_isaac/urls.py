from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^(?P<path>static/.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
