from django.core.management.base import BaseCommand, CommandError
from profil.models import User, UserGroup

import datetime, hashlib, random

def get_date_from_str(date_str):
    print ("date str = [" + date_str + "]")
    return datetime.now()#datetime.strptime(date_str, '%Y-%b-%d %H:%M:%S').date()

def create_profil_group(update, name_str):
    try:
        group = UserGroup.objects.get(name=name_str)
        if update == True:
            #group = fill_profil_group(group, name_str)
            group.save()
            print ("Update  : Group   [" + name_str +"]")
        else:
            print ("Warning : Group   [" + name_str + "]")
    except UserGroup.DoesNotExist:
        group = UserGroup()
        group.name = name_str
        #group = fill_group
        group.save()
        print ("Succes    : Group   [" + name_str + "]")

def create_superuser(update, pseudo_str, email_str, password_str):
    try:
        user = User.objects.get(email=email_str)
        if update == True:
            user.email = email_str
            user.first_name = ''
            user.last_name = ''
            user.is_staff = True
            user.is_superuser = True
            salt =  hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            user.key_date = datetime.datetime.today() + datetime.timedelta(2)
            user.confirmation_key = hashlib.sha1((salt+user.email).encode('utf-8')).hexdigest()
            user.save()
        else:
            print("Warning: User [" + email_str + "] Alerady Exist !")
    except User.DoesNotExist:
        user = User.objects.create_user(pseudo_str, email_str, password_str, UserGroup.objects.get(name="Admin"))
        user.first_name = ''
        user.last_name = ''
        user.is_staff = True
        user.is_superuser = True
        salt =  hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        user.key_date = datetime.datetime.today() + datetime.timedelta(2)
        user.confirmation_key = hashlib.sha1((salt+user.email).encode('utf-8')).hexdigest()
        user.save()
