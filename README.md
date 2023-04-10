# Projeto de Integração com a API do Moip

Este projeto é uma integração com a API do Moip, utilizando a linguagem Python. Ele consiste em algumas funções que permitem o registro de pedidos, pagamentos e clientes no Moip, além de permitir a consulta de pedidos e clientes cadastrados.

## Como usar

1. Clone o repositório do projeto: git clone https://github.com/g-roger/moip-sdk-python.git
2. Instale as dependências necessárias: pip install -r requirements.txt
3. Importe as funções necessárias do arquivo `moip_sdk.py`:

        from moip_sdk.customer import register_customer, get_customer_by_id
        from moip_sdk.order import register_order, get_order, get_orders_by_email
        from moip_sdk.payment import register_payment

4. Crie as credenciais de autenticação:

            from moip_sdk.authorization.headers import headers
            headers['Authorization'] = f'Bearer {ACCESS_TOKEN}' 


## Funcionalidades disponíveis

### Registrar um novo cliente

    new_customer = {
        'own_id': 'customer_001',
        'fullname': 'John Doe',
        'email': 'john.doe@email.com',
        'tax_document': {
            'type': 'CPF',
            'number': '12345678901'
        },
        'phone': {
            'country_code': '55',
            'area_code': '11',
            'number': '912345678'
        },
        'shipping_address': {
            'city': 'São Paulo',
            'state': 'SP',
            'district': 'Vila Olímpia',
            'street': 'Av. Brigadeiro Faria Lima',
            'street_number': '1234',
            'zip_code': '01234-567'
        }
    }
    
    response = register_customer(new_customer)
    print(response)

### Registrar um novo pedido

        new_order = {
            'own_id': 'order_001',
            'amount': {
                'currency': 'BRL',
                'subtotals': {
                    'shipping': 1500
                }
            },
            'items': [
                {
                    'product': 'Product 1',
                    'quantity': 2,
                    'detail': 'Details about Product 1',
                    'price': 2500
                },
                {
                    'product': 'Product 2',
                    'quantity': 1,
                    'detail': 'Details about Product 2',
                    'price': 3000
                }
            ],
            'customer': {
                'id': response['id']
            }
        }
        
        response = register_order(new_order)
        print(response)
    
    
 ### Registrar um novo pagamento

    new_payment = {
        'installment_count': 1,
        'funding_instrument': {
            'method': 'CREDIT_CARD',
            'credit_card': {
                'expiration_month': 10,
                'expiration_year': 22,
                'number': '5555666677778884',
                'cvc': '123',
                'holder': {
                    'fullname': 'John Doe',
                    'birthdate': '1980-01-01',
                    'tax_document': {
                        'type': 'CPF',
                        'number': '12345678901'
                    },
                    'phone': {
                        'country_code': '55',
                        'area_code': '11',
                        'number': '912345678'
                    }
                }
                }
            }
        }
    
    response = register_payment(new_payment, response['id'])
    print(response)


### Buscar um pedido específico

    response = get_order(response['order_id'])
    print(response)


### Buscar todos os pedidos de um cliente pelo e-mail

    response = get_orders_by_email(new_customer['email'])
    print(response)

### Buscar um cliente pelo ID

    response = get_customer_by_id(new_customer['id'])
    print(response)

## Autor
Foi desenvolvido por Gabriel Roger, na necessidade de integrar com python o MOIP. Em 2020 não existia uma integração pronta desenvolvida pela companhia.
