import requests

url = "https://019sms.co.il/api"

payload = {
    "getApiToken": {
        "user": {
            "username": "YOUR_USERNAME",
            "password": "YOUR_PASSWORD"
        },
        "username": "YOUR_USERNAME",
        "action": "new"
    }
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"  # מבקש תגובה בפורמט JSON
}

response = requests.post(url, json=payload, headers=headers)

try:
    data = response.json()
    if data.get("status") == 0:
        token = data["message"]
        expiration = data.get("expiration_date")
        print("✅ הטוקן שלך הוא:", token)
        print("📅 תוקף עד:", expiration)
    else:
        print("❌ שגיאה בקבלת טוקן:", data)
except ValueError:
    print("❌ תגובת JSON לא תקינה:", response.text)
