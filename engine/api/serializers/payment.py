from rest_framework import serializers
from db.models import Payment

#PaymentSerializer to serialize payment objects
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

