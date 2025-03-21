from django.contrib import admin
from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('whiskey/', views.whiskey, name='whiskey'),
    path('gin/', views.gin, name='gin'),
    path('vodka/', views.vodka, name='vodka'),
    path('wine/', views.wine, name='wine'),
]