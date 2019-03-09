"""
WSGI config for erichsblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

#added from web
# path = '/home/erichsblog'
# if path not in sys.path:
#     sys.path.append(path)
# added from web

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erichsblog.settings')

application = get_wsgi_application()
