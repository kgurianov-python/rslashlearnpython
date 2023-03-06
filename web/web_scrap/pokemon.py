import json
import logging

from bs4 import BeautifulSoup, SoupStrainer, Tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

url = "https://www.tcgplayer.com/search/pokemon/product?q=charizard+vmax&view=grid&productLineName=pokemon&setName=product&page=1"
driver.get(url)

wait = WebDriverWait(driver, timeout=120, poll_frequency=5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

content = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
driver.quit()

soup = BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('section', {"class": "search-results"}))

logger.debug(f"{soup=}")

products: list[Tag] = soup.select('section.search-result__product')

cards = []
for product in products:
    card = {
        'name': product.select_one('span.search-result__title').text,
        'price': product.select_one('span.search-result__market-price--value').text
    }
    cards.append(card)

print(json.dumps(cards, indent=4))
