import os
from ..settings import DEPLOYMENT_MODE

if DEPLOYMENT_MODE == 'Local':
    try:
        from .settings_local.email_settings import *
    except ImportError:
        raise Exception("LOCAL EMAIL SETTINGS NOT FOUND")
else:
    try:
        from .settings_heroku.email_settings import *
    except ImportError:
        raise Exception("HEROKU EMAIL SETTINGS NOT FOUND")