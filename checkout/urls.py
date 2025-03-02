from django.urls import path
from . import views
from .views import clear_bag_session

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('clear-bag-session/', clear_bag_session, name='clear_bag_session'),
]