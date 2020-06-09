from django.urls import path
from HotelManager import views


urlpatterns = [
    path('roomPost', views.roomPost),
    path('queryPost', views.queryPost),
    path('setPrice', views.setPrice),
    path('setTemp', views.setTemp),
    path('', views.welcome),
]