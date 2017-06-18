from __future__ import absolute_import, unicode_literals

import os

from .base import *  # noqa: F401, F403


DEBUG = False


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


try:
    from .local import *  # noqa: F401, F403
except ImportError:
    pass
