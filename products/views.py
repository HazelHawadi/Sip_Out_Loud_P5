from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category


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


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


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


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})
