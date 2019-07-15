"""
WSGI config for bigday project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('$HOME/public_html/rauan-and-bartek/django-wedding-website')
sys.path.append('$HOME/public_html/rauan-and-bartek/django-wedding-website/venv/lib/python3.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigday.settings")

application = get_wsgi_application()
