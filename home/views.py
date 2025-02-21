from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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

def whiskey(request):
    return render(request, 'categories/whiskey.html')

def gin(request):
    return render(request, 'categories/gin.html')

def vodka(request):
    return render(request, 'categories/vodka.html')

def wine(request):
    return render(request, 'categories/wine.html')