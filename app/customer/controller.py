import requests

from app import MOIP_API_URL
from app.authorization.headers import headers
from app.customer.schemas import CustomerSchema


def register_customer():
    data = requests.get()
    customer_payload = CustomerSchema().dump(data)

    result = requests.post(f'{MOIP_API_URL}/customers/',
                           data=customer_payload,
                           headers=headers)

    return CustomerSchema().load(result)
