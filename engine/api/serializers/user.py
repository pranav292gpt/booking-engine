from rest_framework import serializers
from db.models import User

#User Serializer to serlialize user data while creating/fetching user
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

#LoninSerializer to serialize data while login
class LoginSerializer(serializers.Serializer):
	email 		= serializers.CharField(required=True, allow_blank=False, allow_null=False)
	password 	= serializers.CharField(required=True, allow_blank=False, allow_null=False)
