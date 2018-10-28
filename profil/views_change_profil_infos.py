from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
from django.http import HttpResponse

from django.core.files import File

from django.utils import timezone
import datetime

from common.views_main import home

from emailing.views_profil import send_new_password_email, send_confirmation_email

from profil.forms import ChangeEmailForm, ChangePasswordForm, ChangePhotoForm
from profil.models import User
from profil.views_profil import profil_show, profil_subscribed
from profil.views_decorator import req_profil


#change password
@req_profil({"login": True})
def change_password(request, profil):
    if request.method == 'POST':
       form = ChangePasswordForm(request.POST)
       if form.is_valid():
           old_password =  form.cleaned_data['old_password']
           new_password =  form.cleaned_data['new_password']
           confirm_password =  form.cleaned_data['confirm_password']
           if authenticate(email=profil.email, password=old_password) == None:
               form.add_error('old_password', 'ancien mot de passe invalide !')
               return render(request, 'profil/change_password.html', {'form': form,})
           if new_password != confirm_password:
               form.add_error('confirm_password', 'passwords must match')
               return render(request, 'profil/change_password.html', {'form': form,})
           if old_password == new_password:
               form.add_error('new_password', 'l ancien mot de passe et le nouveau mot de passe sont le meme !')
               return render(request, 'profil/change_password.html', {'form': form,})
           profil.set_password(new_password)
           profil.save()
           if hasattr(auth, 'update_session_auth_hash'):
               auth.update_session_auth_hash(request, profil)
           return redirect (profil_show)
    else:
        form = ChangePasswordForm()
        return render(request, 'profil/change_password.html', {'form': form,})

#change email. doit confirmer ensuite
@req_profil({"login": True})
def change_email(request, profil):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email =  form.cleaned_data['new_email']
            if new_email == profil.email:
                form.add_error('new_email', 'le nouvel email doit etre different de l ancien email')
                return render(request, 'profil/change_email.html', {'form': form,})
            profil.email = new_email
            profil.is_confirmed = False
            profil.save()
            send_confirmation_email(profil)
            logout(request)
            return redirect (profil_subscribed)
    else:
        form = ChangeEmailForm()
        return render(request, 'profil/change_email.html', {'form': form,})
                                                                                                                                                    
#change image de profil

def handle_uploaded_file(profil, f):
    file_name = "data/image/" + str(profil.id) + ".png"
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@req_profil({"login": True})
def change_photo(request, profil):
    if request.method == 'POST':
        form = ChangePhotoForm(request.POST, request.FILES)
        if form.is_valid():
#            new_photo = File(open(form.cleaned_data["photo"], 'r'))
 #           profil.photo = new_photo
#            profil.photo = request.FILES['photo']
            handle_uploaded_file(profil, request.FILES['photo'])
#           profil.save()
            return redirect(profil_show)
        return render(request, 'profil/change_photo.html', {'form': form,})
    else:
        form = ChangePhotoForm()
    return render(request, 'profil/change_photo.html', {'form': form,})
