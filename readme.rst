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

- Payment

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

- Coupon Views

 - Offer View Set

  - To view general offers and verify offer coupons. Available to all users.
  - URL:

   - /api/v1/coupon/?pk=code

  - Request type: Get

 - Reward View Set

  - To view user specific rewards and verify reward coupons.
  - URL:

   - /api/v1/reward/?pk=code

  - Request type: Get

- Payment

 - Payment View Set to create and update payment objects for bookings.

 - URLs:

  - To Create a new payment

   - /api/v1/payment/

  - To Update already existing payment

   - /api/v1/payment/id/

Serializers
-------------------------------------------------
- User Serializer
 
  - To serialize user data while signup

- Login Serializer

  - To serialize user data while login

- Booking serializer
 
  - To Serialize Booking objects

- Inventory Serializer

  - To Serialize Inventory objects

- Offer Serializer

  - To Serialize Offer objects

- Reward Serializer

  - To Serialize Reward objects

- Payment Serializer

  - To Serialize Payment objects

- Site Serializer

  - To Site Offer objects

How to Build (Step wise)
-------------------------------------------------
1)Install requirements

2)Create database

3)Create local_settings file

4)Apply migrations

5)Runserver
