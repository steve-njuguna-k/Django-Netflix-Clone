from django import urls
from Netflix import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home'),
    path('register', views.Register, name='Register'),
    path('login', views.Login, name='Login'),
]
