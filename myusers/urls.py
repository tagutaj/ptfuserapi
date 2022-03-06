from django.contrib import admin
from django.urls import path
from myusers import views

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    
    
]
