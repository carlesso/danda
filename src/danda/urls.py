from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('restourant.views',
                        url(r'^$', 'index', name = 'index'),
                        url(r'^restourant/(?P<restourant_id>\d+)/$', 'show', name = 'show'),
                        url(r'^piatti/$', 'piatti', name = 'piatti'),
                        )
