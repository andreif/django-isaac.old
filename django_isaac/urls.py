from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'^', include('core.urls')),
)


static_files = [
    r'^static/(?P<path>.*)$',
    r'^favicon.ico$',
    r'^robots.txt$',
    r'^humans.txt$',
    r'^crossdomain.xml$',
    r'^apple-touch-icon.png$',
    r'^apple-touch-icon-precomposed.png$',
    r'^apple-touch-icon-57x57-precomposed.png$',
    r'^apple-touch-icon-72x72-precomposed.png$',
    r'^apple-touch-icon-114x114-precomposed.png$',
]

for static_file in static_files:
    urlpatterns += patterns('', 
        url(static_file, 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
