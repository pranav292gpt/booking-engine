from db.models import User
from rest_framework import viewsets
from rest_framework import mixins
from api.serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.serializers import ValidationError
import uuid

# User view set to create, update or delete user objects
class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):

    # serializer to serialize and validate data
    serializer_class = UserSerializer
    
    queryset = User.objects.all()
    
    # Create method to take input data, validate it, create a new user, and return user token
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate a random refferal code for the new user
        refferal_code= str(uuid.uuid4())[24:]

        data = serializer.data
        user = User.objects.create_user(username=data['username'],password=data['password'],
                email=data['email'], refferal_code=refferal_code)

        if data['install_type'] == "r":

            try:
                # Get the reffered_by user using refferal code of that user.
                # reffered_by is the user whose refferal code out user used to register.
                reffered_by = User.objects.get(refferal_code=data['refferal_code'])

                # Add current user to the refferals of the reffered_by user.
                reffered_by.refferals.append(user.id)

                # save the reffered_by user's updated data.
                reffered_by.save(update_fields=['refferals'])

                # update new user's reffered_by field with the id of the reffered_by user.
                user.reffered_by  = reffered_by.id

                #Change the current user's install type to "Refferal" instead of the default "Organic"
                user.install_type = "r"

                #Save the new user with the updated fields.
                user.save(update_fields=['reffered_by', 'install_type'])

            # Throw exception if the referral code is invalid.
            except Exception as exception:
                return Response({"Error" : "Invalid refferal code"}, status.HTTP_400_BAD_REQUEST)

        token = Token.objects.create(user=user)
        return Response({'token':token.key}, status=status.HTTP_201_CREATED)

    # Update user details
    def partial_update(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status' : status.HTTP_200_OK})

    # Login method
    @list_route(methods=['POST'])
    def  login(self, request, *args, **kwargs):

        serializer =  LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user = authenticate(email=data['email'], password=data['password'])
        
        if user:
            token, is_created = Token.objects.get_or_create(user=user)  
            return Response({'token':token.key,'name': user.username,
                            'email': user.email})
        else:
            raise ValidationError({'detail':'invalid credentials'})
