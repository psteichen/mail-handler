import sys
import argparse

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mass_mail, EmailMessage

from lists.functions import send_email
from lists.models import List, Member

class Command(BaseCommand):
  help = 'Send to list'

  def add_arguments(self, parser):
    parser.add_argument('message', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

  def handle(self, *args, **options):
    raw_mail = options.get('message').read()

    from mailparser import parse_from_string
    mail = parse_from_string(raw_mail)

    To = mail.to
    try:
      ml = List.objects.get(email=To)
    except List.DoesNotExist:
      raise CommandError('No mailing list by this name "%s"' % To)

    From 	= str(mail.from_)
    Subject 	= str(mail.subject)
    Body 	= str(mail.body)
    Attachments	= mail.attachments

    ok = send_email(To,From,Subject,Body,Attachemnts)
    if ok: self.stdout.write(self.style.SUCCESS('Successfully send message to "%s"' % list_email))
    else: self.stdout.write(self.style.DANGER('Error in sending message to "%s"' % list_email))

