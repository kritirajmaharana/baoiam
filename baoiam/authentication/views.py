from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "home/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.username = username
        myuser.email = email

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("signin")

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the index.html upon successful sign-in
            return redirect("home")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "authentication/signup.html")

def signout(request):
    # Add sign-out logic if needed
    pass
