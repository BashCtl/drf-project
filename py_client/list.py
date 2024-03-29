import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()


auth_endpoint = "http://localhost:8000/api/auth/"


auth_response = requests.post(auth_endpoint, json={"username" : getenv("username"), "password": getenv("password")})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
