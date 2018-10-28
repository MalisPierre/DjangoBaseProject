from django.db import IntegrityError
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages as flash_messages
from django.http import HttpResponse

from django.utils import timezone
import datetime

import datetime, hashlib, random

from common.views_main import home

from profil.forms import UserConnectionForm, UserSubscriptionForm
from profil.models import User, UserGroup
from profil.views_decorator import req_profil
from emailing.views_profil import send_confirmation_email, send_new_password_email

@req_profil({"login": False})
def profil_subscription(request):
    if request.method == 'POST':
        form = UserSubscriptionForm(request.POST)
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirmation = form.cleaned_data['password_confirm']
            if password != password_confirmation:
                form.add_error('password_confirm', 'passwords must match')
                return render(request, 'profil/subscription.html', {'form': form, })
            try:
                profil_tmp = User.objects.create_user(pseudo, email, password, UserGroup.objects.get(name="User"))
                profil_tmp.is_active = True
                salt =  hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
                profil_tmp.key_date = datetime.datetime.today() + datetime.timedelta(2)
                profil_tmp.confirmation_key = hashlib.sha1((salt+profil_tmp.email).encode('utf-8')).hexdigest()
                profil_tmp.save()
                send_confirmation_email(profil_tmp)
                return redirect(profil_subscribed)
            except IntegrityError:
                
                form.add_error('pseudo', 'pseudo deja pris')
                return render (request, 'profil/subscription.html', {'form': form, })
        else:
            #form is not valid
            return render (request, 'profil/subscription.html', {'form': form, } )
    else:
        #method post = false
        form = UserSubscriptionForm()
        return render(request, 'profil/subscription.html', {'form': form })

@req_profil({"login": False, })
def profil_subscribed(request):
    return render (request, 'profil/subscribed.html')

@req_profil({"login": False})
def profil_login(request):
    if request.method == 'POST':
        form = UserConnectionForm(request.POST)
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            password = form.cleaned_data['password']
            user = authenticate(username=pseudo, password=password)
            if user is not None and user.is_confirmed == True:
                login(request, user)
            elif user is not None and user.is_confirmed == False:
                form.add_error('pseudo', 'votre compte n est pas encore actif, veuillez regarder votre boite mail')
                return render(request, 'profil/login.html', {'form': form, } )
            elif user is None:
                form.add_error('pseudo', 'combinaison emal / mot de passe incorrecte !')
                return render(request, 'profil/login.html', {'form': form, })
            return redirect (home)
    else:
        form = UserConnectionForm()
        return render(request, 'profil/login.html', {'form': form, })
    
@req_profil({"login": False })
def profil_confirmation(request, activation_key):
    profil = User.objects.get(confirmation_key=activation_key)
    if profil is None:
        return redirect(home)
    if profil.key_date < timezone.now():
        return render (request, 'profil/confirmation_fail.html')
        if profil.is_confirmed == True:
            return redirect(home)
    profil.is_confirmed = True
    profil.save()
    return render (request, 'profil/confirmation_success.html', {'email': profil.email})

@req_profil({"login": True })
def profil_logout(request, profil):#, profil):
    logout(request)
    return redirect(home)

@req_profil({"login": True})
def profil_show(request, profil):
    if profil.is_confirmed == False:
        flash_messages.add_message(request, flash_messages.WARNING, 'profil not confirmed !')
    return render(request, 'profil/show.html', {'profil':profil })
