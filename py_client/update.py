import requests 


endpoint = "http://localhost:8000/api/products/5/update/"

data = {
    "title": "Hi There, New World",
    "price": 129.99
}

response = requests.put(endpoint, json=data)

print(response.json())




