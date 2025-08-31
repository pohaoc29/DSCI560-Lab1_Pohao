# Po-Hao Chen
# USC ID: 4213309111

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Selenium Attributes
options = Options()
options.add_argument("--headless")  # Not opening the browser window
options.add_argument("--width=1920")
options.add_argument("--height=1080")

service = Service("/snap/bin/geckodriver")  # manually assign geckodriver to void errors

driver = webdriver.Firefox(service=service, options=options)
url = "https://www.cnbc.com/world/?region=world"

print("[INFO] Loading the web page...")
driver.get(url)


# Market Banner Section
# Wait for market banner loading
try:
    print("[INFO] Extracting Market Banner...")
    # Wait for at least one MarketCard-container <a> occur
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#market-data-scroll-container a.MarketCard-container"))
    )
    #print("[INFO] Market Banner data loaded successfully!")
except:
    print("[ERROR] Timeout: Market Banner data not found.")
    driver.quit()
    exit()




# Get HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")



# Find the market banner part
banner = soup.find("div", id="market-data-scroll-container")

if not banner:
    print("[WARNING] Market Banner not found!")
    driver.quit()
    exit()

#print(banner.prettify())


# Write into file
raw_path = "../data/raw_data/web_data.html"
with open(raw_path, "w") as f:
    f.write(banner.prettify())
print(f"[INFO] Market Banner HTML saved to {raw_path}")



# Latest News Section
latest_news_section = soup.find('div', class_="LatestNews-isHomePage LatestNews-isIntlHomepage")
print("[INFO] Extracting Latest News...")

if not latest_news_section:
    print("[WARNING] Latest News not found!")
    driver.quit()
    exit()

#print(latest_news_section.prettify())

# Write into file
with open(raw_path, "a") as f:
    f.write(latest_news_section.prettify())
print(f"[INFO] Latest News HTML saved to {raw_path}")


driver.quit()
