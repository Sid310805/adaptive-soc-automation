import requests
from wazuh_api import get_token

token = get_token()

r = requests.get(
    "https://192.168.73.130:55000",
    headers={"Authorization": f"Bearer {token}"},
    verify=False
)

print(r.text)
