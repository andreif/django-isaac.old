from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'^', include('core.urls')),
)


static_files = [
    r'^static/(?P<path>.*)$',
    r'^(?P<path>favicon.ico)$',
    r'^(?P<path>robots.txt)$',
    r'^(?P<path>humans.txt)$',
    r'^(?P<path>crossdomain.xml)$',
    r'^(?P<path>apple-touch-icon(-\d*x\d*)?(-precomposed)?.png)$',
]

for static_file in static_files:
    urlpatterns += patterns('', 
        url(static_file, 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
