from django.db import models
from Timestampedmodel import Timestampedmodel
from user import User


# Coupon model from which Direct Discount and Percentage Discount Coupon will inherit. 
# Field amount represents either direct discount amount or percentage discount

class Coupon(Timestampedmodel):
    code = models.CharField(max_length = 16)
    amount = models.IntegerField()
    is_percentage_discount = models.BooleanField(default=False)
    is_direct_discount = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return unicode(self.code)



# Percentage Discount Coupon which inherits from coupon model. 
# In this case is_percentage_discount boolean will be set True.
# Maximum_discount is the maximum amount that can be discounted by the coupon irrespective of the percentage.

class PercentageDiscountCoupon(models.Model):
    maximum_discount = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


# Direct Discount Coupon which inherits from coupon model.
# In this case is_direct_discount boolean will be set True.
# Minimum order is the minimum order value above which the coupon will be applicable otherwise not.

class DirectDiscountCoupon(models.Model):
    minimum_order = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


# Offer model which will be available for everyone to use having the coupon code

class Offer(PercentageDiscountCoupon, DirectDiscountCoupon, Coupon):
    stat_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)


# Reward model which will contain rewards/coupons for selected users

class Reward(PercentageDiscountCoupon, DirectDiscountCoupon, Coupon):
    allowed_users = models.ManyToManyField(User)
