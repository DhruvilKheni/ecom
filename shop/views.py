from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def product_detail(request, slug):
    return HttpResponse(slug)
