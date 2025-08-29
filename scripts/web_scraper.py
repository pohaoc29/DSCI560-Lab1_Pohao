import requests
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/world/?region=world"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


