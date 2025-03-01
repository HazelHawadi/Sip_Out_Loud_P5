from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import product_list
from .views import product_list, product_management, search, add_to_cart, view_cart, update_cart, remove_from_cart

urlpatterns = [
    path('', product_list, name='products'),
    path('search/', search, name='search'),
    path('<str:category>/', product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('', views.product_list, name='all_products'),  # Show all products
    path('products/<str:category>/', views.product_list, name='product_list_category'),
    path('<str:category>/', views.product_list, name='product_list_with_category'),  # Show category-specific products
    path('products/search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('manage/', views.product_management, name='product_management'),
]