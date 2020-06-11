from django.urls import path
from Customer import views


urlpatterns = [
    path('on', views.editCon),
    path('setTemp', views.setTemp),
    path('setWind', views.setWind),
    path('setMode', views.setMode),
    path('queryPost', views.queryPost),
    path('', views.welcome),
]