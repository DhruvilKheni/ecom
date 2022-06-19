from django.urls import path
from . import views
from buyer.views import shop

urlpatterns = [

    path('', shop, name='shop'),
    path('<slug:slug>/', views.product_detail),
]
