from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('contact-page/',views.contactus, name='contactus'),
   path('signup/',views.signup, name="signup"),
   path('login/', views.login, name='login'), 
]
