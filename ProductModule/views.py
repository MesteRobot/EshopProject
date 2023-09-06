from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory, ProductTag
from django.db.models import Avg, Min, Max

# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('price')
    numberOfProducts = products.count()
    avgRating = products.aggregate(Avg("rating"))
    return render(request, 'product/productList.html',
                  {"products":products,
                   'totalProducts': numberOfProducts,
                   'avgRaiting':avgRating})


def productDetails(request, slug):
    product = get_object_or_404(Product, slug)
    return render(request, 'product/productDetails.html', {'product':product})