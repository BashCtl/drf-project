import requests 


endpoint = "http://localhost:8000/api/products/4/delete/"



response = requests.delete(endpoint)

print(response.status_code)

