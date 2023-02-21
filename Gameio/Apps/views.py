from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "Apps/login.html")


def signup(request):
    return render(request, "Apps/signup.html")


def home(request):
    return render(request, "Apps/home.html")

