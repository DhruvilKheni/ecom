from django.db import models
from calendar import month

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class product(models.Model):

    categori = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    pid = models.CharField(max_length=20)
    price = models.IntegerField()
    ptype = models.CharField(max_length=50)
    ipic = models.FileField(upload_to='product', default='avatar.jpg')

    def __str__(self):
        return self.pname


class Cart(models.Model):

    pid = models.ForeignKey(product, on_delete=models.CASCADE)
    pqty = models.IntegerField()
    # pname = models.CharField(max_length=20)
    cby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cby
