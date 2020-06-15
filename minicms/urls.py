from django.urls import include, path, re_path

from minicms import views
import ckeditor_uploader.urls

app_name = 'minicms'

urlpatterns = [
    path('', views.home_page, name='home'),
    #re_path('ckeditor/', include(ckeditor_uploader.urls)),
    #re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^(?P<urlpath>.+)/$', views.page_view, name='page'),
]
