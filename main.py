import requests

url = "https://v6.exchangerate-api.com/v6/15cc4157a9e4f6b5c7641356/latest/USD"

response = requests.get(url)



target_currency = input("write your currency").upper()
amount = float(input("write amount"))

if response.status_code == 200:
    data = response.json()
    live_rate = data["conversion_rates"][target_currency]
else:
    print("something wrong")
converted_amount = amount * live_rate
print(converted_amount)



