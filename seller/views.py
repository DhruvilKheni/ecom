from django.shortcuts import render
from buyer.models import *
import uuid
# Create your views here


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def handler404(request, exception):
    print(exception)
    return render(request, 'error-404.html', {})


def handler500(request):
    return render(request, 'error-500.html')


def addproduct(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        print(request.FILES)
        product = Product()
        product.pname = request.POST['name']
        product.pid = uuid.uuid4()
        product.price = float(request.POST['price'])
        product.category = Category.objects.get(name=request.POST['category'])
        product.pdes = request.POST['description']
        product.ptype = request.POST['product-type']

        if len(request.FILES) != 0:
            product.ipic = request.FILES['image']

        product.save()
        return render(request, 'add-product.html', {'categories': categories})
    else:
        return render(request, 'add-product.html', {'categories': categories})
