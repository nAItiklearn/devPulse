import requests

url="https://api.github.com/users/nAItiklearn"

response = requests.get(url)

print("Status:", response.status_code)
data = response.json()

print("name:" ,data["name"])
print("public repos:", data["public_repos"])
