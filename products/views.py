from django.shortcuts import render
from django.db.models import Q
from .models import Product, CATEGORY_CHOICES


def product_list(request, category=None):
    if not category:
        category = "all"  # Default category if not provided

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
        'selected_filter': filter_option,
    })



def product_management(request):
    return render(request, 'products/manage.html')


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'home/search_results.html', {
        'products': products,
        'query': query,
        'category': None  # Ensure category is handled properly
    })

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']
    cart.append({'id': product.id, 'name': product.name, 'price': product.price})

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart/cart.html', {'cart_items': cart})


def update_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] = quantity

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

