from django.shortcuts import render
from .models import Products, Locations, Sales, Promos, Makers, Comments


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    products = Products.objects.all()
    return render(request, 'main/catalog.html', {'products': products})


def about(request):
    return render(request, 'main/about.html')


def sale(request):
    sale_products = Sales.objects.sort()
    return render(request, 'main/sale.html', {'products': sale_products})


