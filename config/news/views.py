from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.filter(published=True)


    context = {
        'products': products
    }

    return render(request, 'index.html', context)

def about_products(request, product_id):
    products = get_object_or_404(Product, id=product_id)

    products.views += 1
    products.save()

    context = {
        'products': products,
    }



    return render(request, 'details.html', context)
