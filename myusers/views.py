from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

from myusers.serializers import UserSerializer, SignupSerializer

# Create your views here.

class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer


