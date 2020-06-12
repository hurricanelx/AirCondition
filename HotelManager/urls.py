from django.urls import path
from HotelManager import views


urlpatterns = [
    path('register', views.register),
    path('roomPost', views.roomPost),
    path('queryPost', views.queryPost),
    path('setPrice', views.setPrice),
    path('setTemp', views.setTemp),
    path('data', views.data, name='data'),
    path('', views.welcome),
]