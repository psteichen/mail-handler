
def send_email(sender,to,subject,message_content,cc=False,attachment=False,template='default.txt'):
  from django.core.mail import EmailMessage
  from django.core.mail import EmailMultiAlternatives

  is_array = lambda var: isinstance(var, (list, tuple))

  if not sender: sender = settings.EMAILS['sender']['default']
  email = EmailMultiAlternatives(
                subject=settings.EMAILS['tag'] + " " + subject,
                from_email=sender,
                to=[to]
          )
  email.esp_extra = {"sender_domain": settings.EMAIL_SENDER_DOMAIN}
  message_content['FOOTER'] = settings.EMAILS['footer']
  email.body = render_to_string(template,message_content)
  if attachment:
    if is_array(attachment):
      for a in attachment: attach_to_email(email,a)
    else: attach_to_email(email,attachment)
  if cc: email.cc=[cc]

  try:
    email.send()
    return True
  except:
    return False
