from unicodedata import category
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from buyer.helper.cart import add_to_cart
from buyer.models import *
# Create your views here.


def product_detail(request, slug):
    if request.method == 'POST':
        filter = add_to_cart(request, slug)
        return render(request, 'detail.html', filter)
    else:
        product = Product.objects.get(pid=slug)
        try:
            uid = User.objects.get(email=request.session['email'])
            carts = Cart.objects.filter(customer=uid)
            return render(request, 'detail.html', {'uid': uid, 'carts': carts, 'product': product, })
        except Exception as e:
            return render(request, 'error-404.html')


def category_detail(request, slug):

    try:
        uid = User.objects.get(email=request.session['email'])
        category = Category.objects.get(id=slug)
        carts = Cart.objects.filter(customer=uid)
        products = Product.get_all_products_by_categoty(category)
        return render(request, 'categories.html', {'uid': uid, 'carts': carts, 'products': products, 'category': category})
    except Exception as e:
        return HttpResponse(e)
        # return render(request, 'error-404.html')
