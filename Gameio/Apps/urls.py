from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.Logout, name='logout')
]