"""
WSGI config for news_project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vishubhnews_project.settings')

application = get_wsgi_application()
