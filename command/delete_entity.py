from django.core.management.base import BaseCommand, CommandError
from profil.models import User

from datetime import datetime

def delete_users():
    users = User.objects.all()
    print("--")
    users.delete()
