import requests

TOKEN = "PASTE_THE_TOKEN"

r = requests.get(
    "https://192.168.73.130:55000/security/events",
    headers={"Authorization": f"Bearer {TOKEN}"},
    verify=False
)

print(r.status_code)
print(r.text)
