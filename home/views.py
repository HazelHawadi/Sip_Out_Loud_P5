from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from products.models import Product
from django.db.models import Sum


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def dashboard(request):
    products = Product.objects.all()[:5]

    # Get product count and total sales (summed up)
    product_count = Product.objects.count()
    total_sales = Product.objects.aggregate(Sum('price'))['price__sum'] or 0  # Sum the price field

    return render(request, 'home/dashboard.html', {
        'products': products,
        'product_count': product_count,
        'total_sales': total_sales,
    })

def whiskey(request):
    return render(request, 'categories/whiskey.html')

def gin(request):
    return render(request, 'categories/gin.html')

def vodka(request):
    return render(request, 'categories/vodka.html')

def wine(request):
    return render(request, 'categories/wine.html')

def profile(request):
    return render(request, 'accounts/profile.html')

