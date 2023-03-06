import json
import requests
from bs4 import BeautifulSoup

url = "https://www.tcgplayer.com/search/pokemon/product?q=charizard+vmax&view=grid&productLineName=pokemon&setName=product"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print(page.content)

results = soup.find(id="app")
print(results)
cards = results.find_all("section", class_="marketplace__content")

print(cards)

image = []
title = []
price = []

for card in cards:
    image.append(card.find('img')['src'])
    title.append(card.find("span", class_="search-result__title").text)
    price.append(
        card.find("span", class_="search-result__market-price").text)


product = [{"Image": image, "Title": title, "Price": price}]

print(json.dumps(product, indent=4))