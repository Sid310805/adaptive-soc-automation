import requests
import urllib3

urllib3.disable_warnings()

WAZUH_URL="https://192.168.73.130:55000"

USERNAME="wazuh-wui"
PASSWORD="P0U+VuHSa2*H.DQd3k8EMbkvcanC?zJB"


def get_token():

    r=requests.post(
        f"{WAZUH_URL}/security/user/authenticate",
        auth=(USERNAME,PASSWORD),
        verify=False
    )

    return r.json()["data"]["token"]


def api_get(endpoint):

    token=get_token()

    headers={
        "Authorization":f"Bearer {token}"
    }

    r=requests.get(
        f"{WAZUH_URL}{endpoint}",
        headers=headers,
        verify=False
    )

    r.raise_for_status()

    return r.json()["data"]["affected_items"]


def get_manager_status():
    return api_get("/manager/status")


def get_logs():
    return api_get("/manager/logs")


def get_agents():
    return api_get("/agents")
