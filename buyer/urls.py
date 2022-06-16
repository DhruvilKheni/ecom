from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('ulogin',views.ulogin,name = 'ulogin'),
    path('uregister',views.uregister,name = 'uregister'),
    path('otp/',views.otp,name='otp'),
    path('ulogout/',views.ulogout,name='ulogout'),
    path('shop',views.shop,name = 'shop'),
    path('cart',views.cart,name = 'cart'),
    path('detail',views.detail,name = 'detail'),
    path('checkout',views.checkout,name = 'checkout'),
    path('contact',views.contact,name = 'contact'),
]



