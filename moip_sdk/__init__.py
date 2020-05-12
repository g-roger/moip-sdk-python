import os

MOIP_API_KEY = os.getenv('MOIP_API_KEY') or None
MOIP_API_URL = os.getenv('MOIP_API_URL', 'https://sandbox.moip.com.br/v2')
