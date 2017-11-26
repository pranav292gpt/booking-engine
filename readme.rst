Booking engine to manage vehicle inventory and Bookings.
========================================================

**Version 1**
-------------------------------------------------

Note: **Under Progress**

Install requirements before running

Models
-------------------------------------------------
- User

- Booking

- Inventory

- Site

 - City
 - Site Address
 - Site

- Coupon

 - Coupon(Abstract)
 - Percent Discount(Abstract)
 - Direct Discount(Abstract)
 - Offer (General offer available for all)
 - Reward (User specific offer/Coupon)


Views
-------------------------------------------------
- Booking View
 
 - To manage all CRUD operations on Bookings
 
 - URLS:
   
   - For creating and viewing user bookings: /api/v1/bookings/

- User View
 
 - To manage CRUD operations on Users
 
 - URLS:
  
   - For creating a new user(signup): /api/v1/user/

Serializers
-------------------------------------------------
- User Serializer
 
  - To serialize user data while signup

- Login Serializer

  - To serialize user data while login

- Booking serializer
 
  - To Serialize Booking objects

- Inventory serializer

  - To Serialize Inventory objects

How to Build (Step wise)
-------------------------------------------------
1)Install requirements

2)Create database

3)Create local_settings file

4)Apply migrations

5)Runserver
