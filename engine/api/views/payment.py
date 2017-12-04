from rest_framework import viewsets, mixins
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models import Payment, Booking
from api.serializers import PaymentSerializer


# PaymentViewSet to Create or update payment objects for bookings 
class PaymentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):

    # Token Authentication for the whole view
    authentication_classes=[TokenAuthentication]

    # No unauthenticated user can make requests
    permission_classes = [IsAuthenticated]

    queryset = Payment.objects.all()

    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'created'})
        
