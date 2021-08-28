import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'money_heist.settings')

app = Celery('money_heist')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(timezone='Europe/Kiev')
app.conf.timezone = 'Europe/Kiev'

# Celery Beat schedule
app.conf.beat_schedule = {
    'send_notification_noon': {
        'task': 'spendings.tasks.send_notification_noon',
        'schedule': crontab(hour=11, minute=25),
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
