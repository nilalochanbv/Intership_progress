
import requests

API_KEY = "my-secret-api-key"

url = "https://httpbin.org/anything"

headers = {
    "X-API-Key": API_KEY
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("API Key Sent:", data["headers"].get("X-Api-Key"))
    print("Authentication header received!")
else:
    print("Request failed!")
