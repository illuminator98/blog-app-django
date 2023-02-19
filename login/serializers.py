from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from blogs.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['age','avatar']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','password','id')
		read_only_fields=['post_set']

	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data['password'])
		return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=255)
	password = serializers.CharField(max_length=255)

	class Meta:
		fields = ['username', 'password']
