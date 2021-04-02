import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .default import *



SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['feedeasyform.herokuapp.com', 'feed-easy.fr', 'www.feed-easy.fr']

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME_DB'),
        'USER': os.environ.get('USER_DB'),
        'PASSWORD': os.environ.get('PWD_DB'),
        'HOST': os.environ.get('HOST_DB'),
        'PORT': os.environ.get('PORT_DB'),
    }
}

# Static files settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

sentry_sdk.init(
    dsn="https://e88ae8aa21d84c2f90035f52ac66b507@o279273.ingest.sentry.io/5703372",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

