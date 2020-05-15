import json

import requests

from moip_sdk import MOIP_API_URL
from moip_sdk.authorization.headers import headers
from moip_sdk.customer.schemas import CustomerSchema


def register_customer(data):
    customer_payload = CustomerSchema().dumps(data)

    result = requests.post(f'{MOIP_API_URL}/customers/',
                           data=customer_payload,
                           headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)


def get_customer_by_id(customer_id):
    result = requests.get(f'{MOIP_API_URL}/customers/{customer_id}',
                          headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)
