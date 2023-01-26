import requests as requests
from bs4 import BeautifulSoup

# soup = BeautifulSoup(
#                      '<h3 class="styles_baconCardsWidthByOneHeader__nU9wz"><a class="styles_baconCardsWidthByOneHeaderLink__xuXop" href="https://www.nbcnews.com/select/shopping/best-gluten-free-meal-kit-delivery-services-ncna1294644" target="_self">Looking for gluten-free meal delivery? Start here.</a></h3>'
#                      , features="html.parser")
# attrs = [tag.attrs for tag in soup.findAll('a')]
# for attr in attrs:
#     print(attr['href'])


url = 'https://www.nbcnews.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

nbcnews_headlines = soup.find_all({'h2', 'h3'})

links = []

for line in nbcnews_headlines:
        # href = line.a['href']
        text = line.a.text


print(links)