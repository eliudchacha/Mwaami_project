import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  
# ^ Replace 'mwami' with your actual Django project folder name that has settings.py

application = get_wsgi_application()
