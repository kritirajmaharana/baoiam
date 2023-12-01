from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request,"home/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('passwordagain')
        email = request.POST.get('email')

        if password == password_again:
            try:
                user = User.objects.get(username=username)
                return render(request, 'authentication/register.html', {'error': "Username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth.login(request, user)
                messages.success(request, "You have successfully signed up!")
                
                return render(request,'authentication/login.html')
              
        else:
            return render(request, 'authentication/register.html', {'error': "Passwords don't match"})
    else:
        return render(request, 'authentication/register.html')



def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'home/index.html')
        else:
            return render(request,'authentication/login.html',{'error':'invalid data'})
    else:
        return render(request,'authentication/login.html')


def signout(request):
    # Add sign-out logic if needed
    pass

def contactus(request):
    return render(request, 'contact-page/index.html')