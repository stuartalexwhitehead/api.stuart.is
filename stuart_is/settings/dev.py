from __future__ import absolute_import, unicode_literals

from .base import *  # noqa: F401, F403


DEBUG = True

SECRET_KEY = '!gyg)4vfwcrw103v75kl7zte(yiltu1^banxpqqa^rik+f-ew%'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'rest_framework'
]


try:
    from .local import *  # noqa: F401, F403
except ImportError:
    pass
