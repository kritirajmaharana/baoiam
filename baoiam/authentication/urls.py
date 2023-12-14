
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from authentication import views


urlpatterns = [
    path('admin/', admin.site.urls),

   
    
    path('', views.home, name="home"),
    path('signup/',views.signup, name="signup"),
    path('login/', views.login, name='login'),
  
    path('signout/', views.signout, name='signout'),
    # path('contactus/',views.contactus,name="contactus") ,

]