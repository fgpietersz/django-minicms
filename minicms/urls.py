from django.conf.urls import include, url

from minicms import views

app_name = 'minicms'

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<urlpath>.+)/$', views.page_view, name='page'),
]
