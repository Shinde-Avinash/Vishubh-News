"""
ASGI config for news_project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vishubhnews_project.settings')

application = get_asgi_application()
