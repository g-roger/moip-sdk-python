import base64
from moip_sdk import MOIP_API_KEY

encoded_authorization = base64.b64encode(MOIP_API_KEY.encode('utf-8'))
authorization = str(encoded_authorization, 'utf-8')


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + str(authorization)
}
