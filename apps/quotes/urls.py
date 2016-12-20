from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='quotes_index'),
    url(r'^create$', views.create, name='quotes_create'),
    url(r'^addfave/(?P<id>\d+)$', views.addfave, name='quotes_addfave'),
    url(r'^removefave/(?P<id>\d+)$', views.removefave, name='quotes_removefave'),
    url(r'^/user/(?P<id>\d+)$', views.user, name='quotes_userpage'),
]
