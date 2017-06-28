from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events, name='events'),
    url(r'^intern101/$', views.intern101, name='intern101'),
]