import requests

token_url="https://idp.kuleuven.be/auth/realms/kuleuven/protocol/openid-connect/token"
client_id=''
client_secret=''

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]


print(get_access_token(token_url, client_id, client_secret))

					