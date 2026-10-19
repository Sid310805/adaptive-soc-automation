import requests

r = requests.post(
    "https://192.168.73.130:55000/security/user/authenticate?raw=true",
    auth=("wazuh-wui", "P0U+VuHSa2*H.DQd3k8EMbkvcanC?zJB"),
    verify=False
)

print(r.text)
