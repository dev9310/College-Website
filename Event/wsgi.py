import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Event.settings')

app = get_wsgi_application()  # ✅ Vercel requires `app`, not just `application`
