
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    users = response.json()

    print("\nUser Details:")

    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("-------------------")
else:
    print("API request failed!")
