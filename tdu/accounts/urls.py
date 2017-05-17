from django.conf.urls import url
from . import views


urlpatterns = [
    #会員登録
    url(r'^create/$', views.CreateUserView.as_view(), name='create'),
    url(r'^create_done/$', views.CreateDoneView.as_view(), name='create_done'),
    url(r'^create_complete/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.CreateCompleteView.as_view(), name='create_complete'),

    #ログイン ログアウト
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

]
