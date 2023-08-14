from django.shortcuts import render

from shop.models import Product


def index(request):
    product_objects = Product.objects.all()
    return render(request, 'shop/index.html', {'product_objects': product_objects})
