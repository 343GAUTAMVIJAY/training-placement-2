import requests

url = input("Enter URL: ")
try:
    response = requests.get(url, timeout=5)
    print(f"Status: {response.status_code} {'OK' if response.status_code == 200 else 'Error'}")
except requests.RequestException:
    print("URL unreachable.")