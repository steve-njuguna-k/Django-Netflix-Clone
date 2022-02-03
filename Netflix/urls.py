from django import urls
from Netflix import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='Home'),
    path('register', views.Register, name='Register'),
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='Logout'),
    path('recommendations', views.Recommendations, name='Recommendations'),
    path('tv/<int:tv_id>/details', views.TVDetails, name='TVDetails'),
    path('movie/<int:movie_id>/details', views.MovieDetails, name='MovieDetails'),
]
