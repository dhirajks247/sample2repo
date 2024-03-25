import json

import requests

head = {"Accept": "text/plain", "Content-Type": "application/json"}

body = {
    "id": 1,
    "title": "dhiraj",
    "dueDate": "2023-12-09T06:04:59.989Z",
    "completed": True,
}

response = requests.post(
    "https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head, json=body
)

# print(response.json())

json_response = response.json()
json_str = json.dumps(json_response, indent=4)
print(json_str)

print(response.status_code)

assert response.status_code == 200

data = response.json()
assert data["id"] == 1
