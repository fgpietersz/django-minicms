from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import ListView
from django.views.static import serve as static_serve

import minicms

urlpatterns = [
    url(r'^$', ListView.as_view(model=minicms.models.Page)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('minicms.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]
