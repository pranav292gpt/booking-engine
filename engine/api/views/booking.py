from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from db.models import Booking
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models.inventory import Inventory
from api.serializers import BookingSerializer
from api.libs.booking_availability import booking_availability


#BookingVeiwSet to manage, and perform CRUD operations on bookings
class BookingViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, viewsets.GenericViewSet):

    #Token Authentication for the whole view
    authentication_classes=[TokenAuthentication]

    #No unauthenticated user can view or make bookings
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()

    serializer_class = BookingSerializer
    #List view to output user's own bookings as list

    def list(self, request, *args, **kwargs):
        bookings =  Booking.objects.filter(user=request.user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    #Create method so user can make booking
    def create(self, request, *args, **kwargs):

        #validate input
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        start_time = data['start_time']
        end_time = data['end_time']

        inventory = Inventory.objects.first()

        #Check inventory availability from start time to end time for given inventory
        if booking_availability(start_time, end_time,inventory):

            #Create Booking if available
            serializer.save(inventory=inventory,status=1,user=request.user,)
            return Response({"status":"Created"})

        #Return output with error if vehicle is not available
        else:
            return Response({"Error" : "Requested number of objects not available"})
