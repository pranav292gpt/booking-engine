from rest_framework import serializers
from db.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    offer = serializers.CharField(max_length=None, min_length=None, allow_blank=True, required=False)
    class Meta:
        model = Booking
        fields  = ('id', 'start_time', 'end_time', 'inventory', 'quantity', 'offer', 'reward_applied')
