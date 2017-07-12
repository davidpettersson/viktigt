from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^alerts$', views.alerts),
    url(r'^alerts/(?P<id>\d+)', views.alert_details),
]