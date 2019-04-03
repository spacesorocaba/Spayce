from django.contrib.auth.models import AbstractUser
from django.db import models


class Spacer(AbstractUser):
    cpf = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.name, 'Ativo' if self.active else 'Inativo')


class Order(models.Model):
    customer = models.ForeignKey(Spacer, related_name='consumidor',
                                 on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name='produto',
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    receipt_value = models.FloatField(null=True, blank=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
