# Scrapes titles from a webpage using requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
    return titles

if __name__ == "__main__":
    url = "https://example.com"
    print("Titles:", scrape_titles(url))
