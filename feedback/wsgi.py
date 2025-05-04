"""
WSGI config for feedback project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import sys
import os

# Set path to your project directory
project_home = '/home/SaadiCodes/NetConnect-HTTPS-website'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'feedback.settings'  # adjust if your settings module name is different

# Activate the virtualenv
activate_this = '/home/SaadiCodes/NetConnect-HTTPS-website/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

