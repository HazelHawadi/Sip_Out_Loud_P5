from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

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

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Forget to set it?')

    context = {
        'order_form': order_form,
        'bag_items': bag_items,
        'total': total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
