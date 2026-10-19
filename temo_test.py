# test_opensearch.py

import requests
import json

query = {
    "size": 5,
    "sort": [
        {
            "@timestamp": {
                "order": "desc"
            }
        }
    ]
}

response = requests.get(
    "https://192.168.73.130:9200/wazuh-alerts-*/_search",
    auth=("admin", "Pej.GG9P3Tm4m8Lg+XIp.g2R0NCRljUF"),
    verify=False
)

print(response.status_code)
print(json.dumps(response.json(), indent=2)[:4000])
