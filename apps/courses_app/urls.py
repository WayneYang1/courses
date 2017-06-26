from django.conf.urls import url
#from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^no$', views.no),
    url(r'^yes/(?P<id>\d+)?$', views.yes)
]