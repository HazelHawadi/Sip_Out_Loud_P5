from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Add or update the product in the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect('view_bag')

def checkout_view(request):
    return render(request, 'bag/checkout.html')

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if missing
    bag = request.session.get('bag', {})

    if quantity > 0:
        # Update or add product to the bag with the specified quantity
        bag[item_id] = quantity
    else:
        # Remove the product from the bag if quantity is 0 or less
        bag.pop(item_id, None)

    request.session['bag'] = bag
    messages.success(request, f"Updated {product.name} quantity in your bag.")

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'bag': bag})

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the specified product from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        # Remove the product from the bag entirely
        if item_id in bag:
            bag.pop(item_id, None)

        request.session['bag'] = bag
        messages.success(request, f"Removed {product.name} from your bag.")

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'bag': bag})

        return redirect(reverse('view_bag'))

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)