"""
WSGI config for mlh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

# set sys.path to the directory containing the django app
# else wsgi will not find the settings file below
sys.path.append('/var/www/aperta.lu/django')
sys.path.append('/var/www/aperta.lu/django/mail-handler')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlh.settings")

application = get_wsgi_application()
