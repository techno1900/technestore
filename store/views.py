from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator


# Create your views here.

def store(req, category_name=None):

    categories = None
    product = None

    if category_name is not None:
        categories = get_object_or_404(Category, category_name = category_name)
        product = Product.objects.filter(category = categories)
        paginator = Paginator(product, 30)
        page = req.GET.get('page')
        product_paginator = paginator.get_page(page)

    else:
        product = Product.objects.all()
        paginator = Paginator(product, 30)
        page = req.GET.get('page')
        product_paginator = paginator.get_page(page)

    context = {'product':product_paginator}
    return render(req, 'store/store.html', context)

def single_product(req, pk):
    product = Product.objects.get(id =pk)
    context = {'product':product}
    return render(req, 'store/single-product.html', context)



def search(req):
    if req.method == "GET":
        keyword = req.GET['keyword']
        
        if keyword:
            product = Product.objects.filter(product_name__icontains = keyword)

            paginator = Paginator(product, 30)
            page = req.GET.get('page')
            product_paginator = paginator.get_page(page)
        
    context = {'product':product_paginator, 'keyword':keyword}
    
    return render(req, 'store/search.html', context)
