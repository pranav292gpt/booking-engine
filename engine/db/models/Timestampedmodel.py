# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Timestamped model from which all other models to be inherited to keep track of creation and updation time
class Timestampedmodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
