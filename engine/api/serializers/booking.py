from rest_framework import serializers
from db.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields  = ('id', 'start_time', 'end_time', 'inventory', 'quantity')
