from django.urls import path
from . import views
from .views import clear_bag_session
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('clear-bag-session/', clear_bag_session, name='clear_bag_session'),
    path('wh/', webhook, name='webhook'),
]