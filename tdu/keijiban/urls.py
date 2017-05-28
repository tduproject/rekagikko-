from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^keijiban/$', views.post_list, name='list'),
    url(r'^keijiban/create/$', views.create_thread, name='create'),
    url(r'^keijiban/(?P<pk>[0-9]+)/index/$', views.index, name='index'),
    ]
