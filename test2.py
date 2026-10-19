import requests
import urllib3

urllib3.disable_warnings()

USER = "wazuh-wui"
PASSWORD = "P0U+VuHSa2*H.DQd3k8EMbkvcanC?zJB"

token = requests.post(
    "https://192.168.73.130:55000/security/user/authenticate?raw=true",
    auth=(USER, PASSWORD),
    verify=False
).text

print("TOKEN RECEIVED")

r = requests.get(
    "https://192.168.73.130:55000/manager/status",
    headers={"Authorization": f"Bearer {token}"},
    verify=False
)

print("STATUS:", r.status_code)
print(r.text)

