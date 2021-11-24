from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from django.db.models.lookups import PostgresOperatorLookup

from catalog.models import Book

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    postalCode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    paid = models.BooleanField()

class OrderItem: 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    book =  models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField()
    quantity = models.IntegerField()
