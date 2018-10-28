from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils import timezone


from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend




class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, pseudo, email, password, is_staff, is_superuser, group, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=pseudo,
                          email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, group=group, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, pseudo, email, password, group, **extra_fields):
        return self._create_user(pseudo, email, password, False, False, group, **extra_fields)

    def create_superuser(self, pseudo, email, password, group, **extra_fields):
        return self._create_user(pseudo, email, password, True, True, group, **extra_fields)


class UserGroup(models.Model):

    """
    fields
    """
    name = models.CharField(max_length=16, db_column='name')
    
    def __unicode__( self ):
        return self.name
    
    class Meta:
        db_table = "UserGroup"

# CAN ADD NEW VARIABLE BUT AUTH SYSTEM IS NOT OVERRIDED, OVERRIDE ABSTRACTBASEUSER IF NEEDED, UNIQUE ON PSEUDO
class User(AbstractUser):

    #username = models.CharField(max_length=16, db_column='username')
    #email = models.EmailField('email address', unique=True, db_index=True, db_column='email')
    #first_name = models.CharField(max_length=16, db_column='first_name')
    #last_name = models.CharField(max_length=16, db_column='last_name')
    #is_active = models.BooleanField(default=True, db_column='is_active')
    is_confirmed = models.BooleanField(default=False, db_column='is_confirmed')
    confirmation_key = models.CharField(max_length=40, blank=True, db_column='confirmation_key')
    key_date = models.DateTimeField(default=datetime.now(), db_column='key_date')
    group = models.ForeignKey(UserGroup, db_column='group', )


    objects = UserManager()

    def __unicode__( self ):
        return self.email

    class Meta:
        db_table = "User"
