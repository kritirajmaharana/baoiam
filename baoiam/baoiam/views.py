from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def contactus(request):
    return render(request, 'contact-page/index.html')
