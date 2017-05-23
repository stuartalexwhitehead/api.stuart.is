from __future__ import absolute_import, unicode_literals

from .base import *


DEBUG = True

SECRET_KEY = '!gyg)4vfwcrw103v75kl7zte(yiltu1^banxpqqa^rik+f-ew%'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
