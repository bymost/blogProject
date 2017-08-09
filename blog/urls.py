from django.conf.urls import url

from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url(r'^index.html', views.index, name = 'index'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name = 'detail')
    url(r'^(?P<category>[^/]+)/(?P<title>[^/]+)$', views.detail, name = 'detail'),
    url(r'^(?P<category>[^/]+)$', views.category, name = 'category'),
    url(r'^about_me$', views.about_me, name = 'about_me')
]