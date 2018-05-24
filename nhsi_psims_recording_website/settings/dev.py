import socket

from .base import *


DEBUG = True

DEV_APPS = [
  'debug_toolbar',
]

MIDDLEWARE_DEV = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INSTALLED_APPS = BUILTIN_APPS + THIRD_PARTY_APPS + DEV_APPS + PROJECT_APPS

MIDDLEWARE = MIDDLEWARE + MIDDLEWARE_DEV

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'ezn^k@w45@&zncvn)fzsrnke-e04s#+3$$ol$m=_nfwsfchlvp')

# Custom django debug toolbar settings
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'nhsi_psims_recording_website.utilities.show_django_debug_toolbar',
}
