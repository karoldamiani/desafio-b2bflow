import os
import requests
from dotenv import load_dotenv

load_dotenv()

instance = os.getenv("ZAPI_INSTANCE_ID")
token = os.getenv("ZAPI_TOKEN")

def send_message(phone, message):
    url = (
        f"https://api.z-api.io/instances/"
        f"{instance}/token/{token}/send-text"
    )
    body = {
        "phone": phone,
        "message": message
    }
    response = requests.post(
        url,
        json=body
    )
    return response