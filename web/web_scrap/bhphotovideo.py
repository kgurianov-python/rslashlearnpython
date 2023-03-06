import requests
from bs4 import BeautifulSoup

BOUNDARY = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
HEADERS = {'Accept-Language': 'en-US',
          'User-Agent': ''}

url = 'https://www.bhphotovideo.com/c/product/1274705-REG/canon_eos_5d_mark_iv.html?sts=pi'
result = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(result.content, "html.parser")
with open('bhphotovideo.html', 'wb') as f:
    f.write(result.content)

price = soup.find('div', 'pricesContainer_L0iytPTSvv')

print(f"{price.text=}")