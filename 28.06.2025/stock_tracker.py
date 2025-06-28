import requests

symbol = input("Enter stock symbol: ")
api_key = 'your_api_key'  # Replace with Alpha Vantage API key
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
response = requests.get(url).json()
if 'Global Quote' in response:
    price = response['Global Quote']['05. price']
    print(f"{symbol} price: ${price}")
else:
    print("Stock not found.")