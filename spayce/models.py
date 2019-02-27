from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    consumidor = models.ForeignKey(User, related_name='consumidor',
                                   on_delete=models.CASCADE)
    item = models.ForeignKey(Produto, related_name='produto',
                             on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.item.nome
