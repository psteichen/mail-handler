from django.core.management.base import BaseCommand, CommandError

from lists.functions import send_email
from lists.models import List, Member

class Command(BaseCommand):
    help = 'Send to list'

    def add_arguments(sef, parser):
        parser.add_argument('list_email', nargs='+', type=str)

    def handle(self, *args, **options):
        list_email = options['list_email']:
        try:
          ml = List.objects.get(email=list_email)
        except List.DoesNotExist:
          raise CommandError('No mailing list by this name "%s"' % list_email)

        # read content from stdin
        raw_msg = self.stdin.readlines()

        from email import message_to_string
        msg = message_from_string(raw_msg.join());

        to = msg['to']
        if to != list_email:
          self.stdout.write(self.style.DANGER('Destination mismatch, to: "%s" vs. list_email: "%s"' % to, list_email))

        from = msg['from']
        subject = msg['subject']
        body = msg['body']

        ok = send_email(to,from,subject,body)
        if ok: self.stdout.write(self.style.SUCCESS('Successfully send message to "%s"' % list_email))
        else: self.stdout.write(self.style.DANGER('Error in sending message to "%s"' % list_email))

