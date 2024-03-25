import requests
import json

head = {
    'Accept' : 'text/plain',
    'Content-Type' : 'application/json'
}

body = {
    "id": 2,
    "title": "dhirajks",

}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/5", 
                         headers=head, 
                         json=body)

json_data= response.json()

json_str = json.dumps(json_data, indent=4)

print(json_str)

print(response.status_code)

assert response.status_code == 200

data = response.json()
assert data['id'] == 2