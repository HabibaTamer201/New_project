from django.shortcuts import render,get_object_or_404
from .models import Product

def product(request):
    
    return render(request, 'products/product.html')

def products(request):
    
    return render(request, 'products/products.html', {'products':Product.objects.all()})

