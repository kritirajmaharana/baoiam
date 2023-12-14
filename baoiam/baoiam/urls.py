
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views
from django.views.generic import TemplateView
# from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    
    path('',include('authentication.urls')),
    path('homepage/',include('homepage.urls')),
   
    

    # path('home/', TemplateView.as_view(template_name='home/index.html'), name='home')
    
    path('login/', TemplateView.as_view(template_name='authentication/login.html'), name='login')
  
   

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

