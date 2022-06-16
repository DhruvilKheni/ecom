from django.db import models
from calendar import month

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
