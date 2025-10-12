import os
import sys


project_home = '/home/justuski/reliefapp'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relief_backend.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
