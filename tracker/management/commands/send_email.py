from django.core.management.base import BaseCommand
from tracker.models import Bug


class Command(BaseCommand):
    help = 'Send Notification Email'

    def handle(self, *args, **options):
        bugs = Bug.objects.filter(is_notified=False)

        if bugs:
            bug = bugs[0]
            bug.send_email()
            bug.save()
