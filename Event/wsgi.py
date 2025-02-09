import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Event.settings')

application = get_wsgi_application()  # Ensure this line exists
