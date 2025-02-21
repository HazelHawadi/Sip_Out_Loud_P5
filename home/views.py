from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def whiskey(request):
    return render(request, 'categories/whiskey.html')

def gin(request):
    return render(request, 'categories/gin.html')

def vodka(request):
    return render(request, 'categories/vodka.html')

def wine(request):
    return render(request, 'categories/wine.html')