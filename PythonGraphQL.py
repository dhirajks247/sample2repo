import json

import requests

head = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9FWTJSVGM1UlVOR05qSXhSRUV5TURJNFFUWXdNekZETWtReU1EQXdSVUV4UVVRM05EazFNQSJ9.eyJodHRwczovL2hhc3VyYS5pby9qd3QvY2xhaW1zIjp7IngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzIjpbInVzZXIiXSwieC1oYXN1cmEtdXNlci1pZCI6ImF1dGgwfDY1NjQyYzA1Yjc2OTUzNThhNzRiYTUyNiJ9LCJuaWNrbmFtZSI6ImRoaXJhai5rIiwibmFtZSI6ImRoaXJhai5rQGdlZWt5YW50cy5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvMWU4MzZkOWEwMDNhZjQwOGExZDg3ODdlYWVmODllOTA_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZkaC5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyNC0wMi0xM1QwNzoxMzoxOC4zNDJaIiwiaXNzIjoiaHR0cHM6Ly9ncmFwaHFsLXR1dG9yaWFscy5hdXRoMC5jb20vIiwiYXVkIjoiUDM4cW5GbzFsRkFRSnJ6a3VuLS13RXpxbGpWTkdjV1ciLCJpYXQiOjE3MDgwNjA5OTEsImV4cCI6MTcwODA5Njk5MSwic3ViIjoiYXV0aDB8NjU2NDJjMDViNzY5NTM1OGE3NGJhNTI2IiwiYXRfaGFzaCI6IjhDcUpiS1Bmck9GeC1LNnBxSUtadWciLCJzaWQiOiJucHp2RTl3Y0FadjFBOGVIWUtOR0hkZG43RDg1Y0JERyIsIm5vbmNlIjoiNW9NOGVHeDBKWW5ROU1hc2tGa2hHeEE5cDVCUGRGZjgifQ.bbKIXMaTzPTbsbt-nz4GkiKQYb3hwjigvOvgJc4Cs2UFgzrI_uRPuaRXs9Arko8SsjwlZW7bcrkws3IWb4DqrXuFRurVyVlPgEAwxxm2k8DpAfS1-8stSLD3e4SlkqaTERcjHh5gObUKa0anRpNmsQ2nxc_6Nyq1qK3kF7QPpFdfCkpXqm1-ttZjmcY2H0JNRQJWmtq0NSnipdi35ldwrqgqHsDUi3vwx_ceoNNx7WyrpaczdnDjABVCtHSpROWnyduepwSmHYIUN-w60gRfC47wGTnmg8esGPUZiA648rjxV6mCmwDtdEE5zBCkNa3kTBVW9Q9BUqZLCLghpEPtxA",
    "Content-Type": "application/json",
}

body = """
{
  todos(limit: 5) {
    title
  }
}
"""

body1 = """
query ($name: String!, $limit: Int!) {
  users(where: {name: {_eq: $name}}, limit: $limit) {
    name
  }
}

"""

variable = {"name": "hello", "limit": 10}


response = requests.post(
    "https://hasura.io/learn/graphql",
    headers=head,
    json={"query": body1, "variables": variable},
)

# print(response.json())

json_response = response.json()
json_str = json.dumps(json_response, indent=4)
print(json_str)

print(response.status_code)

assert response.status_code == 200

data = response.json()

assert data["data"]["users"][0]["name"] == "hello"
