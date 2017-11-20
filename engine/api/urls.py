from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from views.booking import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, base_name='bookings')

urlpatterns = [
]
urlpatterns += router.urls
