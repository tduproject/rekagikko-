from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.show, name='show'),
    url(r'^sample/',views.sample , name='test'),
]
