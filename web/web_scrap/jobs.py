import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor

import pandas_try as pd
import requests as requests
from bs4 import BeautifulSoup, SoupStrainer

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('THreadPoool')

BASE_URL = 'https://wuzzuf.net/jobs/p/MEdF7MFl6qZV-Python-Developer-GetTechForce-com-Cairo-Egypt?o=2&l=sp&t=sj&a=python|search-v3|navbg'
REG_ANY = '.*'


response = requests.get(BASE_URL)
# print(response.content)

soup = BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('body'))
title = 'Job.*Details'
jobs_title = soup.select_one("h2", string=re.compile(f'{REG_ANY}{title}{REG_ANY}'))
print(soup)
