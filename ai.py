import requests

def explain(log):

    prompt = f"""
    You are a SOC analyst.

    Alert: 
    {log} 

    Explain:
    Here is clear view :
    Prevention Methods :
    Keep it under 4 lines.
    """

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]
