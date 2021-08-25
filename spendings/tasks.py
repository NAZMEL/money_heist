import logging
from datetime import datetime, timedelta
from celery import Celery, shared_task
from celery.exceptions import MaxRetriesExceededError, SoftTimeLimitExceeded
from django.template.loader import render_to_string
from django.conf import settings
from mailjet_rest import Client
from authentication.models import User
from money_heist.constants import MAILJET_API_VERSION
from spendings.models import Spending

app = Celery()

logger = logging.getLogger('celery')


@shared_task(bind=True, max_retries=3)
def send_notification_noon(self, subject, template, recipients, context):
    now = datetime.now()
    users = User.objects.all()

    for user in users:
        last_spending = Spending.objects.latest(pk=user.id)

        if (now - last_spending.created_at) > timedelta(hours=24):

            mailjet = Client(auth=(settings.MAILJET_PUBLIC_KEY, settings.MAILJET_SECRET_KEY),
                             version=MAILJET_API_VERSION)
            recipients = [{'Email': recipient} for recipient in recipients]
            message = render_to_string(template, context)
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
