from Timestampedmodel import Timestampedmodel
from django.db import models

#City for the site
class City(Timestampedmodel):
    name = models.CharField(max_length=32)
    code = models.IntegerField()

#Address for the site
class SiteAddress(Timestampedmodel):
    name = models.CharField(max_length=16, null=True)
    city = models.ForeignKey(City , related_name="siteaddress")
    location = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    landmark = models.CharField(max_length=256)
    pincode = models.CharField(max_length=8)
    plot_number = models.CharField(max_length=6)
    street_line = models.CharField(max_length=128)
    main_line = models.CharField(max_length=128)
    locality = models.CharField(max_length=128)

#Site details 
class Site(Timestampedmodel):
    name = models.CharField(max_length=64)
    address = models.OneToOneField(SiteAddress, related_name="sites")
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField( auto_now=True)
