import os
from ..settings import DEPLOYMENT_MODE

if DEPLOYMENT_MODE == 'Local':
    try:
        from .settings_local.domain_settings import *
    except ImportError:
        raise Exception("LOCAL DOMAIN SETTINGS NOT FOUND")
else:
    try:
        from .settings_heroku.domain_settings import *
    except ImportError:
        raise Exception("HEROKU DOMAIN SETTINGS NOT FOUND")