from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
    url(r'^(?P<id>\d+)/cancel$', views.cancel),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^join/(?P<id>\d+)$', views.join),
]
