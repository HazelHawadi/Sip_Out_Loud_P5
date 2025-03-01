from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    bag = request.session.get('bag', {})

    # Add or update the product in the bag
    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)   
