"""
WSGI config for north_austin_learn_python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(  "DJANGO_SETTINGS_MODULE",
                        "north_austin_learn_python.settings")

application = get_wsgi_application()
