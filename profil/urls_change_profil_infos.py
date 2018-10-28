from django.conf.urls import patterns, include, url
from . import views_change_profil_infos

urlpatterns = [
    url(r'^change_email$', views_change_profil_infos.change_email, name='change_email'),
    url(r'^change_password$', views_change_profil_infos.change_password, name='change_password'),
    url(r'^change_photo$', views_change_profil_infos.change_photo, name='change_photo'),
]
