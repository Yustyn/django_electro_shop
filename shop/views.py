from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.cart import Cart
from django.conf import settings


# Create your views here.
def homepage(request):
    return render(request, 'pages/index.html', {'count': count(request)})


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brand = None
    brands = Brand.objects.all()
    product = None
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.objects.filter(category=category)
    cart_product_form = CartAddProductForm()
    cart_items = request.session.get(settings.CART_SESSION_ID)
    product = cart_items.keys()

    print(product)
    return render(request, 'pages/store.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form,
        'count': count(request),
    })


def product_page(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/product.html', {'product_detail': product,
                                                  'cart_product_form': cart_product_form,
                                                  'count': count(request)})


def checkout(request):
    return render(request, 'pages/checkout.html', {'count': count(request)})


def product(request):
    return render(request, 'pages/product.html', {'count': count(request)})


def count(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = 0
    for item in cart:
        count += cart[item]['quantity']
    return count
