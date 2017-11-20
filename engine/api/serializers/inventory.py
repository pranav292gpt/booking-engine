from rest_framework import serializers
from db.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Inventory
            fields = ('type', 'site', 'quantity', 'start_time', 'end_time')
