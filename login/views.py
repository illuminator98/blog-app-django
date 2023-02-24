from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
	serializer = UserSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=400)
	serializer.save()
	return Response(serializer.data, status=201)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if not serializer.is_valid():
		return Response(serializer.errors, status=400)

	user = authenticate(
		username=serializer.validated_data['username'],
		password=serializer.validated_data['password']
	)
	if not user:
		return Response({'detail': 'Invalid credentials'}, status=400)

	token, created = Token.objects.get_or_create(user=user)
	return Response({'token': token.key}, status=200)

@api_view(['GET'])
def logout_user(request):
	token = Token.objects.get(user=request.user)
	token.delete()
	return Response(status=200)