import uuid
from urllib import request
from buyer.models import *


def add_to_cart(request, slug=None):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.session['email'])
            products = Product.objects.all()
            pid = request.POST.get('pid')

            product = Product.objects.get(pid=pid)
            quantity = 1
            customer = uid

            carts = Cart.objects.filter(customer=uid)
            in_cart = False
            for item in carts:
                if item.product.pid == product.pid:
                    item.quantity = item.quantity+1
                    item.total = item.product.price*item.quantity
                    item.save()
                    in_cart = True
            if not in_cart:
                Cart.objects.create(
                    product=product,
                    quantity=quantity,
                    customer=customer,
                    total=float(product.price*quantity),
                    cid=uuid.uuid4()
                )
            carts = Cart.objects.filter(customer=uid)
            if slug == None:
                return {'uid': uid, 'carts': carts, 'products': products}
            else:
                return {'uid': uid, 'carts': carts, 'product': product}
        except Exception as e:
            return {
                "error": e
            }
    else:
        try:
            uid = User.objects.get(email=request.session['email'])
            products = Product.objects.all()
            carts = Cart.objects.filter(customer=uid)
            return {'uid': uid, 'carts': carts, 'products': products}
        except Exception as e:
            return {
                "error": e
            }
