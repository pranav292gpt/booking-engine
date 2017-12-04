# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import csv
import StringIO
import datetime
from django.http import HttpResponse, HttpResponseRedirect

from models import Inventory, User, Booking, SiteAddress, City, Site
from models import Offer, Reward


#Method to create csv for data
def createCSV(self, request, queryset):
            f = StringIO.StringIO()
            writer = csv.writer(f)
            date = datetime.datetime.now().date().isoformat()
            headers = []

            for field in queryset.model._meta.fields:
                    headers.append(field.name)

            """ Extra fields to append on headers CSV file """
            extra_headers = []
            headers += extra_headers

            writer.writerow(headers)

            for obj in queryset:
                    row = []
                    for field in headers[0:len(headers)-len(extra_headers)]:
                            val = getattr(obj, field)
                            if callable(val):
                                    val = val()
                            if type(val) == unicode:
                                    val = val.encode("utf-8")
                            row.append(val)
                    writer.writerow(row)

            f.seek(0)
            response = HttpResponse(f, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=Licence('+date+').csv'
            return response
createCSV.short_description = "Download Selected as CSV"

#CSV_ENABLED_Admin to enable csv on all models
class CSV_ENABLED_Admin(admin.ModelAdmin):
    actions = [createCSV]

admin.site.register(User, CSV_ENABLED_Admin)




#Inventory Admin Registration
admin.site.register(Inventory, CSV_ENABLED_Admin)


#Booking Admin Registration
admin.site.register(Booking, CSV_ENABLED_Admin)

#User Admin Registration
#Site Admin Registration
admin.site.register(SiteAddress, CSV_ENABLED_Admin)
admin.site.register(Site, CSV_ENABLED_Admin)
admin.site.register(City, CSV_ENABLED_Admin)


#Coupon Admin Registration
admin.site.register(Reward, CSV_ENABLED_Admin)
admin.site.register(Offer, CSV_ENABLED_Admin)
