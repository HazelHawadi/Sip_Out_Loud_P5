from django.contrib import admin
from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', register, name='register'),
    path('whiskey/', views.whiskey, name='whiskey'),
    path('gin/', views.gin, name='gin'),
    path('vodka/', views.vodka, name='vodka'),
    path('wine/', views.wine, name='wine'),
]