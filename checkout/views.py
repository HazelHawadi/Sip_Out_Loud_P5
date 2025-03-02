from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    # Retrieve products in the bag
    bag_items = []
    total = 0
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = product.price * quantity
        total += subtotal
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'bag_items': bag_items,
        'total': total,
    }

    return render(request, 'checkout/checkout.html', context)
