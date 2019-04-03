import datetime

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from django.shortcuts import get_object_or_404

from spayce.models import Order, Product


class PedidoForm(ModelForm):
    consumidor = forms.IntegerField()
    item = forms.IntegerField()
    quantidade = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['consumidor', 'item', 'quantidade']

    def clean_consumidor(self):
        consumidor_id = self.cleaned_data['consumidor']

        user = get_object_or_404(User, pk=consumidor_id)

        return user

    def clean_item(self):
        item_id = self.cleaned_data['item']

        item = get_object_or_404(Product, pk=item_id)

        return item


class PedidoForm(Form):
    first_date = datetime.date.today() - datetime.timedelta(weeks=4)
    start_date = forms.DateField(label="Data Inicial",
                                 initial=first_date,
                                 widget=forms.DateInput(
                                     attrs={'type': 'date'}))
    end_date = forms.DateField(label="Data Final",
                               initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'type': 'date'}))
