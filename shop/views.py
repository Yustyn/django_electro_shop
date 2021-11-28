from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'pages/index.html')


def store(request):
    return render(request, 'pages/store.html')


def checkout(request):
    return render(request, 'pages/checkout.html')


def product(request):
    return render(request, 'pages/product.html')
