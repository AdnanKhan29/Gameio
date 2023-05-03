from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.Logout, name='logout'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('profile', views.profile, name='profile'),
    path('Homepage', views.Homepage, name='Homepage'),
    path('Snakerules', views.Snakerules, name='Snakerules'),
    path('snake', views.snake, name='snake'),
    path('gameover', views.gameover, name='gameover'),
]