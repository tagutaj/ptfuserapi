from django.contrib import admin
from django.urls import path
from myusers import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('signup/', views.SignupView.as_view()),
    
]
