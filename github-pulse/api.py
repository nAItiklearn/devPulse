import requests

url="https://api.github.com/users/nAItiklearn"

response = requests.get(url)

print(response.status_code)
print(response.json())