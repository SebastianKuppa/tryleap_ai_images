import requests

url = "https://api.tryleap.ai/api/v1/images/models/8b1b897c-d66d-45a6-b8d7-8e32421d02cf/inferences"

payload = {"prompt": "A cat in cyberpunk world"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer f002ff09-8fe2-4727-9d3c-b31fc15c28c2"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)