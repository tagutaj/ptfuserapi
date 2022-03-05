from django.shortcuts import render
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework import filters

from myusers.serializers import UserSerializer, SignupSerializer

# caching
@method_decorator([vary_on_headers("Authorization",),vary_on_cookie, cache_page(60*60*2)], name='dispatch')
#list of users
class UserList(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated,IsAdminUser ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name', 'email']
    ordering_fields =  ['first_name','last_name', 'email']

#user signup
class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer