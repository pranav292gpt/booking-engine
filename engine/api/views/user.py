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

#User view set to create, update or delete user objects
class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):

    #serializer to serialize and validate data
    serializer_class = UserSerializer
    
    queryset = User.objects.all()
    
    #Create method to take input data, validate it, create a new user, and return user token
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        user = User.objects.create_user(username=data['username'],password=data['password'],
                email=data['email'])

        user.save()

        token = Token.objects.create(user=user)
        return Response({'token':token.key}, status=status.HTTP_201_CREATED)

    #Update user details
    def partial_update(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status' : status.HTTP_200_OK})

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
