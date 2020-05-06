import os

MOIP_API_KEY = os.getenv('MOIP_API_KEY')
MOIP_API_URL = os.getenv('MOIP_API_URL', 'https://sandbox.moip.com.br/v2')

if not MOIP_API_KEY:
    raise Exception('Must set environment variable MOIP_API_KEY')
