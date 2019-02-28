from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='consumidor',
                                   on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name='produto',
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
