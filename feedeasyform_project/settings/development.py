from .default import *
import os


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['192.168.1.47']

INSTALLED_APPS.append('django_extensions')

if os.environ.get('DB_LOCAL') == 'laptopAsus':
    # For local database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'feedeasyform_db',
            'USER': 'florent',
            'PASSWORD': os.environ.get('PWDDB_LOCAL'),
            'HOST': '',
            'PORT': os.environ.get('PORT_DB'),
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'feedeasy_form_db',
            'USER': os.environ.get('USER_DB'),
            'PASSWORD': os.environ.get('PWD_DB'),
            'HOST': os.environ.get('HOST_DB'),
            'PORT': os.environ.get('PORT_DB'),
        }
    }
