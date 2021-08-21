import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'money_heist.settings')

app = Celery('money_heist')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks('[money_heist]')
