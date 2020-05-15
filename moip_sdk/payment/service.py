import json

import requests

from moip_sdk import MOIP_API_URL
from moip_sdk.authorization.headers import headers
from moip_sdk.payment.schemas import PaymentSchema


def register_payment(data, order_id):
    payment_payload = PaymentSchema().dumps(data)

    result = requests.post(f'{MOIP_API_URL}/orders/{order_id}/payments/',
                           data=payment_payload,
                           headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)
