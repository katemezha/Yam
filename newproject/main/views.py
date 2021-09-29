from django.shortcuts import render
from django.views.generic import ListView

from .models import Products, Locations, Sales, Promos, Makers, Comments


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    products = Products.objects.all()
    return render(request, 'main/catalog.html', {'products': products})


def about(request):
    comments = Comments.objects.all()
    return render(request, 'main/about.html', {'comments': comments})


def sale(request):
    sale_products = Sales.objects.order_by('price')
    return render(request, 'main/sale.html', {'products': sale_products})


