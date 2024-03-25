import requests
import json

response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/')

json_data= response.json() #optional
json_str= json.dumps(json_data, indent=4) #optional

#print(response.json())

print(json_str)

