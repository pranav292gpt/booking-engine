from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_verification_mail(reciever, code):
    subject = "Verification mail"
    message = "Your verification code is {0}.".format(code)
    sender = 'pranav292gpt@gmail.com'
    send_mail(subject, message, sender, [reciever], fail_silently=False)
