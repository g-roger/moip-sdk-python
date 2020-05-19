import random
import unittest

from moip_sdk.customer.schemas import CustomerSchema
from moip_sdk.customer.service import register_customer
from moip_sdk.order.schemas import OrderSchema
from moip_sdk.order.service import register_order
from moip_sdk.payment.service import register_payment
from moip_sdk.payment.schemas import PaymentSchema
from moip_sdk.payment.enums import MoipPaymentMethod

payment_payload = {
    'installmentCount': 1,
    'statementDescriptor': 'Teste'
}


class PaymentTestCase(unittest.TestCase):
    def setUp(self):
        customer_payload = {
            'ownId': random.randint(900000, 90000000),
            'fullname': 'João da Silva Teste',
            'email': 'joao.teste@mastertech.com.br',
            'birthDate': '2000-02-02',
            'taxDocument': {
                'type': 'CPF',
                'number': '55237990096'
            },
            'phone': {
                'countryCode': '55',
                'areaCode': '11',
                'number': '40028922'
            },
            'shippingAddress': {
                'city': 'Santa Catarina',
                'zipCode': '88132241',
                'street': 'Rua Bréscia',
                'streetNumber': '12',
                'state': 'SC',
                'country': 'Brazil',
                'district': 'Passa Vinte'
            }
        }

        self.customer = CustomerSchema().load(customer_payload)
        registered_customer = register_customer(self.customer)

        order_payload = {
            'ownId': random.randint(900000, 90000000),
            'amount': {
                'currency': 'BRL'
            },
            'items': [{
                'product': 'Curso Mastertech',
                'quantity': 1,
                'detail': 'Este é um teste para venda de um produto',
                'price': 40000,
            }],
            'customer': {
                'id': registered_customer['id']
            }
        }

        order = OrderSchema().load(order_payload)
        self.registered_order = register_order(order)

    def test_register_credit_card_payment(self):
        payment_payload['fundingInstrument'] = {
            'method': MoipPaymentMethod.CREDIT_CARD.name,
            'creditCard': {
                'hash': 'MD6ZDloloRbBcYCnQKjluRzblLmUrGqfd0U0FuzTcmaWkhpHMX1Im9lh'
                        'MwzhA3YDrYWui9GY3hVef37c6rSEWsb6ztZZqRbUz5dElpm3AKcKhVHpm'
                        'LayKTcAWNLVynw+Fy3nfpTboN756e6nM8DmfaPBkUfQ2OXtgZKUWS6kGCPG'
                        'Q4pIHRSA/dxSkxVmzUmTtbUsToT9fAZJbXIh88/Q6tznlV3Ulsb/WE8jkZm'
                        '872zebB2fkfyQS+6IExDOuRa3WndiFGJHdTHS/JdpHe+lRXondIFjBrJ9lW'
                        '8+EK4yZjLTvWxUMNbgGRui1dQ6Y5KDJHc5bVPVHFuVaH50lmcbnw==',
                'store': False,
                'holder': {
                    'fullname': 'João da Silva',
                    'birthDate': '2000-03-02',
                    'taxDocument': {
                        'type': 'CPF',
                        'number': '55237990096'
                    },
                    'phone': {
                        'countryCode': '55',
                        'areaCode': '11',
                        'number': '40028922'
                    }
                }
            }
        }

        payment = PaymentSchema().load(payment_payload)
        response = register_payment(payment, self.registered_order['id'])

        self.assertIsNotNone(response['id'])
        self.assertEqual(len(response), 14)

    def test_register_boleto_payment(self):
        payment_payload['fundingInstrument'] = {
            'method': MoipPaymentMethod.BOLETO.name,
            'boleto': {
                'expirationDate': '2030-02-02'
            }
        }

        payment = PaymentSchema().load(payment_payload)
        response = register_payment(payment, self.registered_order['id'])

        self.assertIsNotNone(response['id'])
        self.assertEqual(len(response), 13)


if __name__ == '__main__':
    unittest.main()
