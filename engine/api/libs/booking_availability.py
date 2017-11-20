from db.models import Booking, Inventory 
from api.serializers import InventorySerializer
from django.db.models import Q
from django.db.models import Sum

#Method to check if vehicle is available in inventory
def booking_availability(start, end, inventory):

    #All booking objects except cancelled one's
    bookings = Booking.objects.filter(status__in=[1,2,3])

    #if atleast one such booking exists
    if bookings.count():
        
        #All booking objects between start time and end time
        bookings = bookings.filter(
                    Q(start_time__gte=start , start_time__lte=end)
                    |Q(start_time__lt=start ,end_time__gt=start))
        
        #Count of booking objects between start time and end time
        booking_count  = bookings.count()
    
    #If no booking exists
    else:
        booking_count=0
    
    #If quantity of inventory is greater then bookings, return true otherwise false
    return 1  <= inventory.quantity - booking_count
