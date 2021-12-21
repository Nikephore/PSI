from django.db import models
from decimal import Decimal


from catalog.models import Book


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    paid = models.BooleanField(null=True)

    def __str__(self):
        return self.first_name

    def get_total_cost(self):
        ret = 0
        for item in self.items.all():
            ret += Decimal(item.price) * item.quantity

        return ret


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return "Item:" + str(self.book) + " con precio " + str(self.price)
