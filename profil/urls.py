from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'', include ('profil.urls_profil')),
    url(r'', include ('profil.urls_change_profil_infos')),
]
