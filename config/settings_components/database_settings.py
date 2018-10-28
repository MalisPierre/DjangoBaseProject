import os
from ..settings import DEPLOYMENT_MODE

if DEPLOYMENT_MODE == 'Local':
    try:
        from .settings_local.database_settings import *
    except ImportError:
        raise Exception("LOCAL DATABASE SETTINGS NOT FOUND")
else:
    try:
        from .settings_heroku.database_settings import *
    except ImportError:
        raise Exception("HEROKU DATABASE SETTINGS NOT FOUND")