from __future__ import absolute_import, unicode_literals
import os
import celery
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'money_heist.settings')


@celery.signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    pass


app = Celery('money_heist')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['money_heist'], )