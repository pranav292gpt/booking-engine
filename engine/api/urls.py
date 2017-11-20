from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from views.booking import BookingViewSet
from views.user import UserViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, base_name='bookings')
router.register(r'user', UserViewSet, base_name='user')

urlpatterns = [
]
urlpatterns += router.urls
