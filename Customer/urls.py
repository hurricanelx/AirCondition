from django.urls import path
from Customer import views


urlpatterns = [
    path('', views.welcome),
]