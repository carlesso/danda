from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.http import HttpResponseRedirect
from django.contrib import admin
admin.autodiscover()

def logout(request, user_id = None):
    from django.contrib.auth import logout as _logout
    _logout(request)
    return HttpResponseRedirect('/')



urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name = 'login'),
                       url(r'^accounts/logout/', logout, name = 'logout'),
                       (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('restourant.views',
                        url(r'^$', 'index', name = 'index'),
                        url(r'^about/$', 'about', name = 'about'),
                        url(r'^contattaci/$', 'contattaci', name = 'contattaci'),
                        url(r'^restourant/$', 'show', name = 'show'),
                        url(r'^restourant/(?P<restourant_id>\d+)/$', 'show_restourant', name = 'show_restourant'),
                        url(r'^piatti/$', 'piatti', name = 'piatti'),
                        url(r'^ordini/$', 'ordini', name = 'ordini'),
                        url(r'^ordini/new/$', 'nuovo_ordine', name = 'nuovo_ordine'),
                        url(r'^ordini/(?P<id_ordine>\d+)/$', 'show_ordine', name = 'show_ordine'),
                        )
