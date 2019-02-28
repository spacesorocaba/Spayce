from django.contrib.auth.models import AbstractUser
from django.db import models


class Spacer(AbstractUser):
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.name, 'Ativo' if self.active else 'Inativo')


class Order(models.Model):
    customer = models.ForeignKey(Spacer, related_name='consumidor',
                                 on_delete=models.CASCADE)
    item = models.ForeignKey(Product, related_name='produto',
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
