from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='Login')
def Dashboard(request):
    return render(request, "Apps/Dashboard.html")


def home(request):
    return render(request, "Apps/home.html")


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
            return render(request, 'login', {'error': ": Username or password is incorrect"})
    return render(request, "Apps/Login.html")


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'signup', {'error': ": Password didn't match"})
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Login')

    return render(request, "Apps/signup.html")


def Logout(request):
    logout(request)
    return redirect('Login')
