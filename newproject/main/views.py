from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def about(request):
    return render(request, 'main/about.html')


def sale(request):
    return render(request, 'main/sale.html')


