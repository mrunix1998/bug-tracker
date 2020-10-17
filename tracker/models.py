import logging
import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from smtplib import SMTPException

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Bug(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    due_date = models.DateTimeField(null=True)
    description = models.TextField(null=True, blank=True)
    closed = models.BooleanField(default=False)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def send_email(self):
        # do logging stuff here
        if self.assigned_to:
            logger.info(f"[{datetime.datetime.now()}]: Started Sending Bug-{self.pk} to {self.assigned_to}")
            try:
                send_mail(
                    f'[BUG ALERT] {self.title}',
                    self.description,
                    'bug@bug-tracker.com',
                    [self.assigned_to.email],
                )
                self.is_notified = True
                logger.info(f"[{datetime.datetime.now()}]: Finished Sending Bug-{self.pk} to {self.assigned_to}")

            except (SMTPException, OSError):
                self.is_notified = False
                logger.error(f"[{datetime.datetime.now()}]: Failed Sending Bug-{self.pk} to {self.assigned_to}")




