# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Inventory, User, Booking, SiteAddress, City, Site
from models import Offer, Reward

#Inventory Admin Registration
admin.site.register(Inventory)


#Booking Admin Registration
admin.site.register(Booking)


#User Admin Registration
admin.site.register(User)


#Site Admin Registration
admin.site.register(SiteAddress)
admin.site.register(Site)
admin.site.register(City)


#Coupon Admin Registration
admin.site.register(Reward)
admin.site.register(Offer)
