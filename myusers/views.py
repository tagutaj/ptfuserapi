from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework import filters

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from django.views.generic.base import View

from myusers.serializers import UserSerializer, SignupSerializer



#caching
@method_decorator([vary_on_headers("Authorization",),vary_on_cookie, cache_page(60*60*2)], name='dispatch')

#list of users
class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser ]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name', 'email']
    ordering_fields =  ['first_name','last_name', 'email','is_staff','date_joined','is_superuser']

#user signup
class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

#api root
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'signup': reverse('signup', request=request, format=format)
    })