import requests

url = "https://019sms.co.il/api"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}

data = {
  "sms": {
    "user": {
      "username": "YOUR_USERNAME"
    },
    "source": "YOUR_SENDER",
    "destinations": {
      "phone": [
        {
          "_": "0551234123"
        }
      ]
    },
    "message": "YOUR_MESSAGE",
  }
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
