from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='rnl_index'),
    url(r'^register$', views.register, name='rnl_register'),
    url(r'^login$', views.login, name='rnl_login'),
    url(r'^logout$', views.logout, name='rnl_logout'),
]
