# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Timestampedmodel import Timestampedmodel

# Timestamped Model for maintaining vehicle inventory

# TODO: Add Sites/Station model

class Inventory(Timestampedmodel):
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.id)
