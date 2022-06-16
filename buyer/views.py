from asyncio import events
from urllib import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from random import choices, randrange
from django.conf import settings
from django.core.mail import send_mail
from buyer.models import *
from datetime import datetime

# Create your views here.


def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'index.html', {'uid': uid})
    except:
        pass

    return render(request, 'index.html')


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
        return render(request, 'checkout.html', {'uid': uid})
    except:
        pass

    return render(request, 'checkout.html')


def detail(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'detail.html', {'uid': uid})
    except:
        pass

    return render(request, 'detail.html')


def shop(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'shop.html', {'uid': uid})
    except:
        pass

    return render(request, 'shop.html')


def cart(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'cart.html', {'uid': uid})
    except:
        pass

    return render(request, 'cart.html')


def contact(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request, 'contact.html', {'uid': uid})
    except:
        pass

    return render(request, 'contact.html')
