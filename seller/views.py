from django.shortcuts import render
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
