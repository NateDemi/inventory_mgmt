import requests
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class Order:
    """Base class for creating orders via Zinc API."""

    def __init__(self, api_key, retailer, shipping_address):
        self.api_key = api_key
        self.retailer = retailer
        self.shipping_address = shipping_address
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_order(self, products, is_gift=False):
        """Method to create an order."""
        url = 'https://api.zincapi.com/v1/order'
        payload = {
            'retailer': self.retailer,
            'products': products,
            'shipping_address': self.shipping_address,
            'is_gift': is_gift
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response


def load_info(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

