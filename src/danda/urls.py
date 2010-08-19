from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('restourant.views',
                        url(r'^$', 'index', name = 'index'),
                        url(r'^about/$', 'about', name = 'about'),
                        url(r'^restourant/$', 'show', name = 'show'),
                        url(r'^restourant/(?P<restourant_id>\d+)/$', 'show_restourant', name = 'show_restourant'),
                        url(r'^piatti/$', 'piatti', name = 'piatti'),
                        url(r'^ordini/$', 'ordini', name = 'ordini'),
                        url(r'^ordini/(?P<id_ordine>\d+)/$', 'show_ordine', name = 'show_ordine'),
                        )
