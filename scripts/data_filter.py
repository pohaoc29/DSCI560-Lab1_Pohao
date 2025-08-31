from bs4 import BeautifulSoup
import csv

# Import web_data.html
with open("../data/raw_data/web_data.html", 'r') as f:
    html = f.read()


soup = BeautifulSoup(html, "html.parser")


# Market Banner Section
market_data = []
banner = soup.find("div", id="market-data-scroll-container")

if banner:
    print("Filtering Market Banner...")
    cards = banner.find_all("a", class_="MarketCard-container")
    for card in cards:
        symbol = card.find("span", class_="MarketCard-symbol").text.strip()
        position = card.find("span", class_="MarketCard-stockPosition").text.strip()
        pct = card.find("span", class_="MarketCard-changesPct").text.strip()
        market_data.append([symbol, position, pct])

    with open("../data/processed_data/market_data.csv", 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["symbol", "stockPosition", "changePct"])
        writer.writerows(market_data)

    print("Market data filtered and saved to market_data.csv.")
else:
    print("[Warning] Market Banner div not found in HTML file!")



# Latest News Section
news_data = []
news_list = soup.find("ul", class_="LatestNews-list")

if news_list:
    print("Filtering Latest News List...")
    all_news = news_list.find_all("li", class_="LatestNews-item")
    for news in all_news:
        timestamp = news.find("time", class_="LatestNews-timestamp").text.strip()
        title = news.find("a", class_="LatestNews-headline").text.strip()
        link = news.find("a", class_="LatestNews-headline").get("href")
        news_data.append([timestamp, title, link])

    with open("../data/processed_data/news_data.csv", 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["timestamp", "title", "link"])
        writer.writerows(news_data)

    print("Latest News data filtered and saved to news_data.csv.")
else:
    print("[Warning] Latest News List ul not found in HTML file!")

