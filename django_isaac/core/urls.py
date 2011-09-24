from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='core_index'),
    url(r'^bluescreen.html$', 'bluescreen', name='core_bluescreen'),
)
