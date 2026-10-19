from wazuh_api import get_alerts

alerts = get_alerts()

for a in alerts:
    print(a)
