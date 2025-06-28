import requests

url = input("Enter URL to shorten: ")
api_url = f'http://tinyurl.com/api-create.php?url={url}'
response = requests.get(api_url)
if response.status_code == 200:
    print("Shortened URL:", response.text)
else:
    print("Error shortening URL.")