from django.urls import path
from . import views
from buyer.views import shop

urlpatterns = [

    path('', shop, name='shop'),
    path('product/<slug:slug>/', views.product_detail),
    path('category/<slug:slug>/', views.category_detail),
]
