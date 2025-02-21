from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('whiskey/', views.whiskey, name='whiskey'),
    path('gin/', views.gin, name='gin'),
    path('vodka/', views.vodka, name='vodka'),
    path('wine/', views.wine, name='wine'),
]