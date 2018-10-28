from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^profil/', include ('profil.urls')),
    url(r'^common/', include ('common.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
