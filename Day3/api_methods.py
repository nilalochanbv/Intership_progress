
import requests

base_url = "https://jsonplaceholder.typicode.com/users"

# 1. POST - Create a new user
new_user = {
    "name": "Nila",
    "email": "nila@example.com"
}

post_response = requests.post(base_url, json=new_user)

print("POST Status:", post_response.status_code)
print("Created User:", post_response.json())

# 2. PUT - Update an existing user
updated_user = {
    "id": 1,
    "name": "Nila Updated",
    "email": "updated@example.com"
}

put_response = requests.put(
    f"{base_url}/1",
    json=updated_user
)

print("\nPUT Status:", put_response.status_code)
print("Updated User:", put_response.json())

# 3. DELETE - Delete a user
delete_response = requests.delete(f"{base_url}/1")

print("\nDELETE Status:", delete_response.status_code)
print("User deletion request completed!")
