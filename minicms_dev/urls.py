from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.views.generic import ListView
from django.conf.urls.static import static

import minicms.urls
import ckeditor_uploader.urls

urlpatterns = [
    path('', ListView.as_view(model=minicms.models.Page)),
    path('admin/', admin.site.urls),
    path('ckeditor/', include(ckeditor_uploader.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path('', include(minicms.urls))]
