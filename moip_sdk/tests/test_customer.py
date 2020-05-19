import random
import unittest

from moip_sdk.customer.schemas import CustomerSchema
from moip_sdk.customer.service import register_customer

customer_payload = {
    'ownId': random.randint(900000, 90000000),
    'fullname': 'João da Silva Teste',
    'email': 'joao.teste@mastertech.com.br',
    'birthDate': '2000-02-02',
    'taxDocument':{
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


class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerSchema().load(customer_payload)
        self.registered_customer = register_customer(self.customer)

    def test_register_customer(self):
        self.customer['own_id'] = random.randint(900000, 90000000)
        response = register_customer(self.customer)

        self.assertIsNotNone(response['id'])
        self.assertEqual(len(response), 10)


if __name__ == '__main__':
    unittest.main()
