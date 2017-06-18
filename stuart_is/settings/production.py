from __future__ import absolute_import, unicode_literals

import os

from .base import *  # noqa: F401, F403


DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stuartis',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

INSTALLED_APPS = INSTALLED_APPS + [
    'storages',
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {}
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = os.environ.get('AWS_DEFAULT_REGION')

BASE_URL = 'https://api.stuart.is'

WAGTAILAPI_BASE_URL = 'https://stuart.is'

ALLOWED_HOSTS = [
    os.environ.get('API_GATEWAY_ENDPOINT')
]

try:
    from .local import *  # noqa: F401, F403
except ImportError:
    pass
