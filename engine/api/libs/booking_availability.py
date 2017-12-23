from db.models import Booking, Inventory 
from api.serializers import InventorySerializer
from django.db.models import Q
from django.db.models import Sum

#Method to check if vehicle is available in inventory
def booking_availability(start, end, inventory, quantity):

    #All booking objects except cancelled one's
    bookings = Booking.objects.filter(status__in=[1,2,3], inventory=inventory)

    #if atleast one such booking exists
    if bookings.count():
        
        #All booking objects between start time and end time
        bookings = bookings.filter(
                    Q(start_time__gte=start , start_time__lte=end)
                    |Q(start_time__lt=start ,end_time__gt=start))
        
        #Count of booking objects between start time and end time
        booking_count = bookings.aggregate(Sum('quantity'))['quantity__sum']
        if not booking_count:
            booking_count = 0

    #If no booking exists
    else:
        booking_count=0
    
    #If quantity of inventory is greater then bookings, return true otherwise false
    return quantity <= inventory.quantity - booking_count
