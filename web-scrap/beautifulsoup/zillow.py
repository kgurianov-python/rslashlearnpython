import re

import requests
from bs4 import BeautifulSoup
from csv import writer



# Create variables

HEADER = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

url = "https://www.zillow.com/homes/Atlanta,-GA_rb/"
page = requests.get(url, headers=HEADER)
soup = BeautifulSoup(page.content, 'html.parser')
with open('zillow_test.html', 'wb') as f:
    f.write(page.content)
results_container = soup.find("div", {"id": "search-page-list-container"})


lists = results_container.find_all('li', {"class", "with_constellation"})
print(f"{len(lists)=}")


with open("attl_housing.csv", 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    headings = ['price', 'address', 'home_type', 'realty_property']
    thewriter.writerow(headings)

    for li in lists:
        print(f"{li=}")
        try:
            price = li.find('span', {"data-test" : "property-card-price"}).text
            address = li.find('address', {"data-test" : "property-card-addr"}).text
            home_type = li.find('div', string=re.compile(f'MLS ID.*')).text
            realty_property = li.find('ul').text.strip()

            info = [price, address, home_type, realty_property]
            print(info)
            thewriter.writerow(info)
        except AttributeError as e:
            print("empty element")

