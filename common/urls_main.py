from django.conf.urls import patterns, include, url
from common import views_main

urlpatterns = [
    url(r'^home$', views_main.home, name='home'),
    url(r'^troubleshouting$', views_main.troubleshouting, name='troubleshouting'),
    url(r'^troubleshouting_sended$', views_main.troubleshouting_sended, name='troubleshouting_sended'),
]
