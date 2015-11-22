from django.conf.urls import include, url
from django.contrib import admin
import minicms

urlpatterns = [
    url(r'^pages/', include('minicms.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
