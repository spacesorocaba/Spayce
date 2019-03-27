import os
from pprint import pprint
import requests
from prettyconf import config
from models import ProductClient, OrderClient
from collections import namedtuple

product_client = ProductClient()
order_client = OrderClient()

products_data = product_client.list()

products = {product['name']: product['id'] for product in products_data.json()}
Order = namedtuple('Order', ['cpf', 'product'])


def order_payload(orders):
    payload = []
    for order in orders:
        data = {
            'quantity': 1,
            'paid': False,
            'customer': order.cpf,
            'item': order.product,
        }
        payload.append(data)
    return payload


def main():
    cpf = input('Digite seu cpj: ')
    orders = []

    while True:
        print('Produtos disponiveis:')

        for product, id_ in products.items():
            print(f'{id_} - {product}')

        product_code = input('Adicione um producto, digite seu código: ')

        if product_code == '0':
            break

        if not int(product_code) in products.values():
            os.system('clear')
            continue

        orders.append(Order(cpf, product_code))
        print('ORDER: ', orders)

    for order in order_payload(orders):
        print(order)
        r = order_client.create(order)
        print(r)


if __name__ == '__main__':
    main()
