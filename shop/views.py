from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.cart import Cart
from django.conf import settings


# Create your views here.
def homepage(request):
    return render(request, 'pages/index.html', {
        'count': count(request),
        'cart': cart(request)})


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
    pr = []
    product = []
    if cart_items:
        product = cart_items.keys()
        pr = Product.objects.filter(id__in=product)
    return render(request, 'pages/store.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form,
        'count': count(request),
        'cart_items': pr,
        'cart': cart(request),
    })


def product_page(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/product.html', {'product_detail': product,
                                                  'cart_product_form': cart_product_form,
                                                  'count': count(request),
                                                  'cart': cart(request)})


def checkout(request):
    return render(request, 'pages/checkout.html', {'count': count(request),
                                                   'cart': cart(request)})


def product(request):
    return render(request, 'pages/product.html', {'count': count(request),
                                                  'cart': cart(request)})


def count(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = 0
    if cart:
        cart_values = cart.values()
        for item in cart_values:
            count += item['quantity']
        return count


def cart(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = 0
    subtotal = 0
    if cart:
        cart_values = cart.values()

        for item in cart_values:
            count += item['quantity']
            subtotal += item['quantity']*float(item['price'])

        cart_items_id = cart.keys()

        product_list = Product.objects.filter(id__in=cart_items_id)
        return {'counts': count, 'product_list': product_list, 'carts': cart, 'subtotal': subtotal}
