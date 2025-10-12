import sys, os

project_home = u'/home/justuski/repositories/ReliefApp'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relief_backend.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()