import requests

amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g., USD): ").upper()
to_curr = input("To currency (e.g., EUR): ").upper()
api_key = 'your_api_key'  # Replace with ExchangeRate-API key
url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}'
response = requests.get(url).json()
if response['result'] == 'success':
    print(f"{amount} {from_curr} = {response['conversion_result']} {to_curr}")
else:
    print("Conversion failed.")