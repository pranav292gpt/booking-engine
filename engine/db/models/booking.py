from django.db import models
from inventory import Inventory
from Timestampedmodel import Timestampedmodel
from user import User
from coupon import Offer, Reward

#Booking model from managing all  user and invetory booking data
#TODO: Add quantity if single user is allowed multiple vehicles
class Booking(Timestampedmodel):

    BOOKING_STATUS 	= (
        (0, 'unpaid'),
        (1, 'upcoming'),
        (2, 'ongoing'),
        (3, 'completed'),
        (4, 'cancelled'),
    )
    user = models.ForeignKey(User, related_name="user_bookings")
    inventory = models.ForeignKey(Inventory,related_name="inventory_bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField(default=0, choices=BOOKING_STATUS)
    offer_applied = models.OneToOneField(Offer, null=True, blank=True)
    reward_applied = models.OneToOneField(Reward, null=True, blank=True)
    quantity = models.IntegerField()

    def __unicode__(self):
        return unicode(self.id)
