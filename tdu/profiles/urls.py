#profilesの全てのviewをインポートするよ
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.profile_list),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.profile_detail, name = 'profile_detail'),
    url(r'^profiles/new/$', views.profile_new, name='profile_new'),
    url(r'^profiles/(?P<pk>[0-9]+)/edit/$', views.profile_edit, name='profile_edit'),
]
