from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from views.booking import BookingViewSet
from views.user import UserViewSet
from views.coupon import OfferViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, base_name='bookings')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'offer', OfferViewSet, base_name='offer')
router.register(r'reward', RewardViewSet, base_name='reward')

urlpatterns = [
]
urlpatterns += router.urls
