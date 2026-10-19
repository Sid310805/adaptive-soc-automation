import requests

USER = "wazuh-wui"
PASSWORD = "P0U+VuHSa2*H.DQd3k8EMbkvcanC?zJB"

token = requests.get(
    "https://192.168.73.130:55000/security/user/authenticate?raw=true",
    auth=(USER, PASSWORD),
    verify=False
).text

headers = {"Authorization": f"Bearer {token}"}

r = requests.get(
    "https://192.168.73.130:55000/manager/status",
    headers=headers,
    verify=False
)

print(r.json())
