from rest_framework import serializers

from spayce.models import Product, Order, Spacer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('receipt_value',)


class SpacerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spacer
        fields = ('id', 'username', 'first_name', 'last_name', 'cpf',
                  'email')
