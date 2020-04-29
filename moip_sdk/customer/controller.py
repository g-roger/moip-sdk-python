import requests

from moip_sdk import MOIP_API_URL
from moip_sdk.authorization.headers import headers
from moip_sdk.customer.schemas import CustomerSchema


def register_customer():
    data = requests.get()
    customer_payload = CustomerSchema().dump(data)

    result = requests.post(f'{MOIP_API_URL}/customers/',
                           data=customer_payload,
                           headers=headers)

    return CustomerSchema().load(result)
