from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.conf import settings

from emailing.views_helpers import send_email, get_html

# appeler lors de la creation de compte et au changement d email
def send_confirmation_email(current_user):
    data = "<p>merci de cliquer sur le lien pour valider votre compte</p>" + "<p><a href=""" + settings.WEBSITE_ADDRESS + "/profil/confirmation/" + current_user.confirmation_key + " "">" + settings.WEBSITE_NAME_STR + "</a></p>"
    send_email("pierre.malis@epitech.eu", current_user.email,
               "confirmation de creation",
               data, get_html(data))
    return True

# appeler lors de l'oubli de mot de passe
def send_new_password_email(current_user):
    data = "votre nouveau mot de passe est " + current_user.password
    send_email("pierre.malis@epitech.eu", current_user.email,
               "votre nouveau mot de passe",
               data, get_html(data))
    return True
