from django.urls import path
from AirConManager import views

urlpatterns = [
    path('on', views.editCon),
    path('set', views.set_),
    path('', views.welcome),
]