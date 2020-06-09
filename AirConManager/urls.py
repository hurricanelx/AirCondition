from django.urls import path
from AirConManager import views

urlpatterns = [
    path('', views.welcome),
]