from django.urls import path
from . import views


urlpatterns = [

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('handler404', views.handler404, name='handler404'),
    path('handler500', views.handler500, name='handler500'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('addcategory', views.addcategory, name='addcategory'),


]
handler404 = 'seller.views.handler404'

# /addproduct
# /addcategory
