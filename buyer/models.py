from django.db import models
from calendar import month
import uuid
import datetime

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True, default=1)

    def __str__(self):
        return self.name


class Product(models.Model):

    pname = models.CharField(max_length=50)
    pid = models.CharField(
        primary_key=True, max_length=100, default=uuid.uuid4())
    price = models.IntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    pdes = models.CharField(max_length=200, default='')
    ptype = models.CharField(max_length=50)
    ipic = models.ImageField(upload_to='product', default='avatar.jpg')

    def __str__(self):
        return self.pname


class Cart(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    cid = models.CharField(
        max_length=100, default=uuid.uuid4())
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.pname

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Cart.objects.filter(customer=customer_id).order_by('-date')
