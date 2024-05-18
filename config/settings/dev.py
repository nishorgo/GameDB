from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-89p2055yy$c(jtg)8#yan@mnn-erwue8_^nnvdnnj-7^yu5fa7'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gamedb',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'P@ssword'
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

CORS_ALLOWED_ORIGINS = [
    
]