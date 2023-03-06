import json
import logging
from concurrent.futures import ThreadPoolExecutor
import time
from functools import partial

import requests as requests
from bs4 import BeautifulSoup, Tag, SoupStrainer

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Scrapper')
logger.setLevel(logging.DEBUG)

HEADER = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

BASE_URL = "https://en.wikipedia.org/wiki/Link_page"

DEPTH = 7
LINK_POSITION = 18


def main():
    resp = requests.get(BASE_URL, headers=HEADER)

    current_depth = 0
    soup = BeautifulSoup(resp.content, 'html.parser', parse_only=SoupStrainer('a'))
    links = soup('a')
    print(f"{links}")
    # break
    #
    # while current_depth < DEPTH:
    #     try:
    #
    #         link = links[LINK_POSITION]
    #         logger.debug(link.text)
    #         url = link['href']
    #         resp = requests.get(url, headers=HEADER)
    #         soup = BeautifulSoup(resp.content, 'html.parser', parse_only=SoupStrainer('a'))
    #         links = soup.find_all('a')
    #     except:
    #         pass

    logger.info(f"{len(links)=}")


if __name__ == '__main__':
    main()
