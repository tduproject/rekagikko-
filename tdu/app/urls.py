from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^csv_import/$', views.csv_import, name='csv_import'),
    url(r'^csv_export/$', views.csv_export, name='csv_export'),
]
 
