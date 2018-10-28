import os
from ...settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'XXX',  
        'USER': 'XXX',
        'PASSWORD': 'XXX',
        'HOST': 'XXXX',  
        'PORT': '5432', 
    }
}

ALLOWED_HOSTS = ['*']