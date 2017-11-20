# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Inventory, User, Booking

admin.site.register(Inventory)
admin.site.register(Booking)
admin.site.register(User)
