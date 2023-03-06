import json
import requests
from bs4 import BeautifulSoup

# URL = "https://www.ebay.com/sch/i.html?_nkw=justin+herbert+national+treasures+rpa&_in_kw=4&_sacat=64482&LH_Complete=1&LH_Sold=1"
URL = "https://www.ebay.com/sh/research?marketplace=EBAY-US&keywords=Justin%2BHerbert%2BNational%2BTreasures%2BRPA&dayRange=180&endDate=1675705127122&startDate=1660149527122&categoryId=0&offset=0&limit=50&tabName=SOLD&tz=Europe%2FKiev"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="srp-river-results")
listings = results.find_all("div", class_="s-item__wrapper clearfix")
product = []
for listing in listings:
    title_element = listing.find("div", class_="s-item__title")
    price_element = listing.find("span", class_="s-item__price")
    print(f"Title: {title_element.text}; Price {price_element.text}")
    product.append({"title": title_element.text, "price": price_element.text})

# title = [listing.find("div", class_="s-item__title").text for listing in listings]
# price = [listing.find("span", class_="s-item__price").text for listing in listings]
# product = [{"title": title, "price": price}]

print(json.dumps(product, indent=4))


def main():
    pass


if __name__ == '__main__':
    main()
