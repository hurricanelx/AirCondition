from django.urls import path
from login_hello import views


urlpatterns = [
    path('login', views.login_),
    path('register', views.register_),
    path('login/', views.login_welcome),
    path('register/', views.register_welcome),
    path('login_/', views.login),
    path('register_/', views.register),
    path('', views.welcome),
]
