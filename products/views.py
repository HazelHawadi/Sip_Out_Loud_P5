from django.shortcuts import render
from .models import Product, CATEGORY_CHOICES

def product_list(request, category):
    # Filter products by category
    products = Product.objects.filter(category=category)
    
    filter_option = request.GET.get('filters')
    
    if filter_option == "price_low_to_high":
        products = products.order_by('price')
    elif filter_option == "price_high_to_low":
        products = products.order_by('-price')
    elif filter_option == "alcohol_abv":
        products = products.order_by('alcohol_percentage')
    elif filter_option == "rating":
        products = products.order_by('-rating')
    
    return render(request, f'categories/{category}.html', {
        'products': products,
        'category': category,
        'selected_filter': filter_option,  # Pass the selected filter to the template
    })


def product_management(request):
    return render(request, 'products/manage.html')