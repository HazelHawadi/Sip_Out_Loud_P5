from django.shortcuts import render
from .models import Product, CATEGORY_CHOICES

def product_list(request, category):
    products = Product.objects.filter(category=category)
    return render(request, f'categories/{category}.html', {'products': products})


def product_management(request):
    return render(request, 'products/manage.html')