import logging
import datetime

from celery import Celery, shared_task
from celery.exceptions import MaxRetriesExceededError, SoftTimeLimitExceeded
from django.db.models import Max
from django.template.loader import render_to_string
from django.conf import settings
from mailjet_rest import Client

from authentication.models import User
from money_heist.constants import MAILJET_API_VERSION

app = Celery()

logger = logging.getLogger('celery')


@shared_task(bind=True, max_retries=3)
def send_notification_noon(self):
    time = datetime.datetime.now() - datetime.timedelta(hours=12)

    # Get the emails of all the users that didn't create any spendings during last {time}
    recipients = User.objects.annotate(max_date=Max('spendings__created_at')).filter(max_date__date__lt=time).values_list('email', flat=True)

    # Template that sends to a user
    template = 'notifications/notification.html'
    subject = "Don't forget to track your spendings!"

    mailjet = Client(auth=(settings.MAILJET_PUBLIC_KEY, settings.MAILJET_SECRET_KEY),
                     version=MAILJET_API_VERSION)
    recipients = [{'Email': recipient} for recipient in recipients]
    message = render_to_string(template)
    data = {
        'Messages': [
            {
                'From': {
                    'Email': settings.MAILJET_USER,
                    'Name': 'Money Heist Team'
                },
                'To': recipients,
                'Subject': subject,
                'HTMLPart': message
            }
        ]
    }
    try:
        result = mailjet.send.create(data=data)
    except SoftTimeLimitExceeded as e:
        logger.error(e)
        return

    if result.status_code != 200:
        error = result.json()
        logger.error(f"Something went wrong while send email, Error: {error}")
        try:
            self.retry(countdown=30)
        except MaxRetriesExceededError as e:
            logger.error(e)
