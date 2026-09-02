import requests

API_KEY = "reqres_c37b3f390aa5437ba04f9f722d1f39b8"
headers = {"x-api-key": API_KEY}

resp = requests.get("https://reqres.in/api/users?page=2", headers=headers)
print(resp.status_code)
print(resp.json())
