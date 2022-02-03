from django import urls
from Netflix import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home'),
]
