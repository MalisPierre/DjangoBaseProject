from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from profil.views_profil import check_user_connected, get_current_user, profil_show

from common.views_main import home

from emailing.views_helpers import send_email, get_html

def send_confirmation(request):
   if check_user_connected(request) != None :
       current_user = get_current_user(request)
       send_email("pierre.malis@epitech.eu", current_user.email, "confirmation de rendez-vous", "blabla", get_html("blabla"))
       return redirect (profil_show)
   return redirect (home)
