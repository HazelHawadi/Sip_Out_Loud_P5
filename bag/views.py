from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))
    bag = request.session.get('bag', {})

    # Add or update the product in the bag
    if str(item_id) in bag:
        bag[str(item_id)] += quantity
        messages.success(
            request,
            f'✅ Updated <strong>{product.name}</strong> quantity to {bag[str(item_id)]}',
            extra_tags='toast-success'
        )
    else:
        bag[str(item_id)] = quantity
        messages.success(
            request,
            f'🛒 Added <strong>{product.name}</strong> to your bag!',
            extra_tags='toast-success'
        )

    request.session['bag'] = bag

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'bag': bag})

    return redirect(redirect_url)

def checkout_view(request):
    """ Render checkout page """
    return render(request, 'bag/checkout.html')

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if missing
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[str(item_id)] = quantity
        messages.info(
            request,
            f'🛍️ Updated <strong>{product.name}</strong> quantity to {quantity}.',
            extra_tags='toast-info'
        )
    else:
        bag.pop(str(item_id), None)
        messages.warning(
            request,
            f'⚠️ Removed <strong>{product.name}</strong> from your bag.',
            extra_tags='toast-warning'
        )

    request.session['bag'] = bag

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'bag': bag})

    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove the specified product from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if str(item_id) in bag:
            bag.pop(str(item_id), None)
            messages.warning(
                request,
                f'🗑️ Removed <strong>{product.name}</strong> from your bag.',
                extra_tags='toast-warning'
            )

        request.session['bag'] = bag

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'bag': bag})

        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(
            request,
            f'❌ An error occurred: {str(e)}',
            extra_tags='toast-error'
        )
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
