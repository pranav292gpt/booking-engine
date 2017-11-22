# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Inventory, User, Booking, SiteAddress, City, Site

admin.site.register(Inventory)
admin.site.register(Booking)
admin.site.register(User)
admin.site.register(SiteAddress)
admin.site.register(Site)
admin.site.register(City)
