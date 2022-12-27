import requests

href = 'http://localhost:8000/api/v1'
param = {
    'param1': 'param1',
}
response = requests.get(href, param)

print(response.text)
print(response.status_code)
