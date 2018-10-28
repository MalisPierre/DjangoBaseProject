from django.conf.urls import patterns, include, url
from . import views_profil

urlpatterns = [
    url(r'^subscription$', views_profil.profil_subscription, name='profil_subscription'),
    url(r'^subscribed$', views_profil.profil_subscribed, name='profil_subscribed'),
    url(r'^confirmation/(?P<activation_key>\w+)$', views_profil.profil_confirmation, name='profil_confirmation'),
    url(r'^login$', views_profil.profil_login, name='profil_login'),
    url(r'^logout$', views_profil.profil_logout, name='profil_logout'),
    url(r'^show$', views_profil.profil_show, name='profil_show'),
]
