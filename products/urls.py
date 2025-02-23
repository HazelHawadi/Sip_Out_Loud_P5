from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', product_list, name='products'), 
    path('<str:category>/', product_list, name='product_list'),
    path('manage/', views.product_management, name='product_management'),
]