from django.conf.urls import include, url

from minicms import views

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<urlpath>.+)/$', views.page_view, name='page'),
]
