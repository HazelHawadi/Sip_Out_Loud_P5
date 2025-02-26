from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', product_list, name='products'), 
    path('<str:category>/', product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('', views.product_list, name='all_products'),  # Show all products
    path('products/<str:category>/', views.product_list, name='product_list_category'),
    path('<str:category>/', views.product_list, name='product_list_with_category'),  # Show category-specific products
    path('manage/', views.product_management, name='product_management'),
]