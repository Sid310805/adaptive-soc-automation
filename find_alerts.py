from wazuh_api import get_token
import requests

token = get_token()

headers = {
    "Authorization": f"Bearer {token}"
}

urls = [
    "https://192.168.73.130:55000/security/events",
    "https://192.168.73.130:55000/alerts",
    "https://192.168.73.130:55000/manager/logs",
    "https://192.168.73.130:55000/events",
    "https://192.168.73.130:55000/manager/logs/summary"
]

for url in urls:
    try:
        r = requests.get(url, headers=headers, verify=False)
        print(url)
        print(r.status_code)
        print(r.text[:200])
        print("="*50)
    except Exception as e:
        print(url, e)
