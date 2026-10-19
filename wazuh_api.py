import requests

WAZUH_IP = "192.168.73.130"
USERNAME = "username"
PASSWORD = "password"

requests.packages.urllib3.disable_warnings()

def get_token():
    url = f"https://192.168.73.130:55000/security/user/authenticate?raw=true"

    response = requests.get(
        url,
        auth=(USERNAME, PASSWORD),
        verify=False
    )

    return response.text.strip()


def get_agents():

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://192.168.73.130:55000/agents",
        headers=headers,
        verify=False
    )


    return response.json()


def get_alerts():
    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://192.168.73.130:55000/manager/logs?limit=10",
        headers=headers,
        verify=False
    )

    data = response.json()

    logs = []

    for item in data["data"]["affected_items"]:

        description = item.get("description", "")
        level = item.get("level", "info")

        if str(level).lower() == "critical":
            risk = "🔴 HIGH"
            ai = "Critical security event detected. Immediate investigation required."

        elif str(level).lower() == "error":
              risk = "🔴 HIGH"
              ai = "Security error detected. Review the affected service." 

        elif str(level).lower() == "warning":
              risk = "🟡 MEDIUM"
              ai = "Suspicious activity detected. Investigation recommended."

        else:
             risk = "🟢 LOW"
             ai = "Informational system event."

        logs.append({
            "timestamp": item.get("timestamp", ""),
            "description": description,
            "level": level,
            "agent": item.get("tag", "Wazuh Manager"),
            "risk": risk,
            "ai": ai
})

    return logs
def get_manager_status():

    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://192.168.73.130:55000/manager/status",
        headers=headers,
        verify=False
    )

    return response.json()
