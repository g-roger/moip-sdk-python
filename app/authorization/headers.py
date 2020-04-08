import base64

from app import MOIP_API_KEY

key = MOIP_API_KEY.encode('utf-8')
authorization = base64.standard_b64decode(key)
authorization = authorization.decode('utf-8')


def headers():
    result = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + str(authorization)
    }

    return result
