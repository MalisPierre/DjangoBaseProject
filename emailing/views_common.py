from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from emailing.views_helpers import send_email, get_html

from django.conf import settings

# appeler lors de la creation de compte et au changement d email
# appeler lors de l'oubli de mot de passe
def send_troubleshouting(cool, comment):
    data = "commentaire = [" + comment + "]"
    if cool == True:
        obj = "avis positif"
    else:
        obj = "avis negatif"

    #send_email(settings.EMAILER_TEAM , "pierre.malis@epitech.eu",
     #   obj,
      #  data, get_html(data))
    return True
