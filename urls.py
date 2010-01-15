from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mirror.views.index'),
    (r'^stats/', include('mirror.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/', 'django.contrib.auth.views.logout'),
    (r'^api/', include('api.urls')),
)

# serve media files in debug mode
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

