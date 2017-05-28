from __future__ import absolute_import, unicode_literals

from .base import *  # noqa: F401, F403


DEBUG = False


try:
    from .local import *  # noqa: F401, F403
except ImportError:
    pass
