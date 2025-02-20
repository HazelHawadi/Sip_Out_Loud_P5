def cart_contents(request):
    """
    Context processor to make cart total available across all templates.
    """
    grand_total = 0.00

    if 'cart' in request.session:
        for item in request.session['cart'].values():
            grand_total += float(item['price']) * item['quantity']

    return {
        'grand_total': grand_total
    }