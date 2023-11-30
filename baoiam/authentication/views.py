from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
#from .models import User as CustomUser
from django.contrib.auth import authenticate, login

# def home(request):
#     return render(request, "home/index.html")
def home(request):
    return render(request,"home/index.html")

def signup(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'authentication/register.html',{'error':"name already exit"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect(login)
        else:
            return render(request,'authentication/register.html',{'error':"password dont match"})
    else:
        
        return render(request,'authentication/register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
            return render(request,'authentication/login.html',{'error':'invalid data'})
    else:
        return render(request,'authentication/login.html')


def signout(request):
    # Add sign-out logic if needed
    pass
