import requests
from settings import settings


class APIClientBase:
    auth = (settings.USER, settings.PASSWORD)
    session = requests.Session()

    def list(self):
        return self.session.get(url=self.url, auth=self.auth)

    def fetch(self, pk):
        return self.session.get(self.url + f'{pk}/', auth=self.auth)

    def create(self, data=None):
        return self.session.post(url=self.url, data=data, auth=self.auth)


class Spacer(APIClientBase):
    url = settings.SPACER_URL


class ProductClient(APIClientBase):
    url = settings.PRODUCT_URL


class OrderClient(APIClientBase):
    url = settings.ORDER_URL
