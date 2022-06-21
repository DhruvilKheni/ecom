import uuid
from asyncio import events
from urllib import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from buyer.helper.cart import add_to_cart
from .models import *
from random import choices, randrange
from django.conf import settings
from django.core.mail import send_mail
from buyer.models import *
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.session['email'])
            categories = Category.objects.all()
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
            return render(request, 'index.html', {'uid': uid, 'products': products, 'carts': carts, 'categories': categories})
        except Exception as e:
            return render(request, 'error-404.html')
    else:
        try:
            uid = User.objects.get(email=request.session['email'])
            carts = Cart.objects.filter(customer=uid)
            products = Product.objects.all()
            categories = Category.objects.all()

            return render(request, 'index.html', {'uid': uid, 'products': products, 'carts': carts, 'categories': categories})

        except:
            categories = Category.objects.all()
            products = Product.objects.all()
            return render(request, 'index.html', {'products': products, 'categories': categories})


def ulogin(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                return redirect('index')
            else:
                return render(request, 'ulogin.html', {'msg': 'Wrong Password'})
        except:
            return render(request, 'ulogin.html', {'msg': 'Wrong Email'})
    return render(request, 'ulogin.html')


def uregister(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request, 'uregister.html', {'msg': 'Email is already register'})
        except:
            otp = randrange(1111, 9999)
            subject = 'Welcome to Soc Management App'
            message = f"""Hello {request.POST['name']}!!
            Your Verification OTP is : {otp}.
            """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email']]
            send_mail(subject, message, email_from, recipient_list)
            global temp
            temp = {
                'name': request.POST['name'],
                'email': request.POST['email'],
                'password': request.POST['password'],
            }
            return render(request, 'otp.html', {'otp': otp})

    else:
        return render(request, 'uregister.html')


def otp(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['uotp']:
            global temp
            User.objects.create(
                name=temp['name'],
                email=temp['email'],
                password=temp['password']
            )
            del temp
            msg = 'User created'
            return render(request, 'ulogin.html', {'msg': msg})
        else:
            msg = 'Incorrect OTP'
            return render(request, 'otp.html', {'otp': request.POST['otp'], 'msg': msg})


def ulogout(request):
    del request.session['email']
    return redirect('ulogin')


def checkout(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        carts = Cart.objects.filter(customer=uid)

        products = Product.objects.all()
        return render(request, 'checkout.html', {'uid': uid, 'carts': carts, 'products': products, })
    except:
        return render(request, 'checkout.html')


def detail(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        carts = Cart.objects.filter(customer=uid)
        products = Product.objects.all()
        return render(request, 'detail.html', {'uid': uid, 'carts': carts, 'products': products, })
    except:
        return render(request, 'detail.html')


def shop(request):
    # try:
    filter = add_to_cart(request)
    print(filter)
    return render(request, 'shop.html', filter)
    # except:
    #     return render(request, 'shop.html')


def cart(request):
    if request.method == 'POST':
        try:
            item = Cart.objects.get(cid=request.POST['cid'])
            if request.POST['count'] == 'plus':
                item.quantity = item.quantity+1
                item.total = item.product.price*item.quantity
                item.save()
            elif request.POST['count'] == 'minus':
                item.quantity = item.quantity-1
                item.total = item.product.price*item.quantity
                item.save()
            else:
                Cart.objects.filter(cid=request.POST['cid']).delete()
            uid = User.objects.get(email=request.session['email'])
            carts = Cart.objects.filter(customer=uid)
            products = Product.objects.all()
            return render(request, 'cart.html', {'uid': uid, 'carts': carts, 'products': products, })
        except:
            return render(request, 'error-404.html')
    else:
        # try:
        uid = User.objects.get(email=request.session['email'])
        carts = Cart.objects.filter(customer=uid)
        products = Product.objects.all()
        return render(request, 'cart.html', {'uid': uid, 'carts': carts, 'products': products, })
        # except Exception as e:
        #     return HttpResponse(f"<h1>{e}</h1>")
        # return render(request, 'cart.html')


def contact(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        carts = Cart.objects.filter(customer=uid)
        products = Product.objects.all()
        return render(request, 'contact.html', {'uid': uid, 'carts': carts, 'products': products, })
    except:
        pass

    return render(request, 'contact.html')
