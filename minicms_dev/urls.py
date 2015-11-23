from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

import minicms

urlpatterns = [
    url(r'^$', ListView.as_view(model=minicms.models.Page)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('minicms.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    ]
