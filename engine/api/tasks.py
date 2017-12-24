from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from db.models import Booking
import datetime
from datetime import timedelta
from django.db.models import Q

@shared_task
def send_verification_mail(reciever, code):
    subject = "Verification mail"
    message = "Your verification code is {0}.".format(code)
    sender = 'pranav292gpt@gmail.com'
    send_mail(subject, message, sender, [reciever], fail_silently=False)
    return code

@shared_task
def send_booking_status_mail(booking_object):
    email = booking_object.user.email
    if email:
        subject = 'Booking notification'
        message = "Dear user. You have a booking tomorrow"
        sender = 'pranav292gpt@gmail.com'
        send_mail(subject, message, sender, [email], fail_silently=False)
        print email
        return "Verification mail sent"

@shared_task
def booking_status_update():
    today = datetime.date.today()
    tomorrow = today + timedelta(days=1)

    bookings = Booking.objects.filter(status__in=[1,2])
    bookings = bookings.filter(start_time__lte=tomorrow, end_time__gt=today)
    print bookings
    for object in bookings:
        send_booking_status_mail(object)
        return 'sent mail'
