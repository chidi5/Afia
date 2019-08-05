from django.contrib import admin
from django.urls import path
from market import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    path('buy/apple/', views.apple, name='apple'),
    path('my/afia/', views.afia, name='afia'),
]
