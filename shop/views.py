from django.shortcuts import render
from django.http.response import HttpResponse
from buyer.models import *
# Create your views here.


def product_detail(request, slug):
    product = Product.objects.get(pid=slug)
    try:
        uid = User.objects.get(email=request.session['email'])
        carts = Cart.objects.filter(customer=uid)
        return render(request, 'detail.html', {'uid': uid, 'carts': carts, 'product': product, })
    except Exception as e:
        # return HttpResponse(slug)
        return render(request, 'error-404.html')
