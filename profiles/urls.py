from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/', profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]