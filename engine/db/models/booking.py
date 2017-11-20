from django.db import models
from inventory import Inventory
from Timestampedmodel import Timestampedmodel
from django.contrib.auth.models import User

#Booking model from managing all  user and invetory booking data
#TODO: Add quantity if single user is allowed multiple vehicles
class Booking(Timestampedmodel):
    user = models.ForeignKey(User, related_name="user_bookings")
    inventory = models.ForeignKey(Inventory,related_name="inventory_bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField()
