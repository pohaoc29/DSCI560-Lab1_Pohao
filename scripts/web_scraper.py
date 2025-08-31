# Po-Hao Chen
# USC ID: 4213309111
import requests
from bs4 import BeautifulSoup

# Input the URL
url = "https://www.cnbc.com/world/?region=world"

# Add headers to avoid “Access Denied” errors
headers = {
    "User-Agent": "MMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) "
                  "Gecko/20100101 "
                  "Firefox/142.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.cnbc.com/"
}

response = requests.get(url, headers=headers)
#print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')


# Market Banner Section
market_banner = soup.find("div", id="market-data-scroll-container")
markets = market_banner.find_all("a")

#print(market_banner.prettify())  # print the market banner HTML
# write into web_data.html file
with open('../data/raw_data/web_data_no_banner.html', 'w') as f:
    f.write(market_banner.prettify())

# Letest News Section
latest_news_section = soup.find('div', class_="LatestNews-isHomePage LatestNews-isIntlHomepage")

#print(latest_news_section.prettify())  # print the latest news HTML
# write into web_data.html file
with open('../data/raw_data/web_data_no_banner.html', 'a') as f:
    f.write(latest_news_section.prettify())
