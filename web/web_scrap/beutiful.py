import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor

import pandas_try as pd
import requests as requests
from bs4 import BeautifulSoup

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('THreadPoool')

# soup = BeautifulSoup(
#                      '<h3 class="styles_baconCardsWidthByOneHeader__nU9wz"><a class="styles_baconCardsWidthByOneHeaderLink__xuXop" href="https://www.nbcnews.com/select/shopping/best-gluten-free-meal-kit-delivery-services-ncna1294644" target="_self">Looking for gluten-free meal delivery? Start here.</a></h3>'
#                      , features="html.parser")
# attrs = [tag.attrs for tag in soup.findAll('a')]
# for attr in attrs:
#     print(attr['href'])
global_links = {}


class PrimesExtractor:
    url: str

    def __init__(self, url):
        self.url = url

    def run(self) -> (dict[str], list[str]):
        res = {}
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_row = soup.select_one('div.row')
        for link in div_row.select('div div:nth-child(9) p a[href]'):
            numbers = re.compile(r'\d+(?:\.\d+)?')
            key = numbers.findall(link['title'])[0]
            res[key] = f'{link.text}'

        return res, res.keys()


def get_primes(url: str) -> None:
    logger.debug(f'Retrieving page [{url}]')

    try:
        res = PrimesExtractor(url).run()[1]
        logger.debug(f'{res=}')
        logger.debug(f'{PrimesExtractor(url).url=}')

        return res
    except Exception as e:
        logging.error(e)


def get_all_primes(links: list[str]) -> None:
    for url in links:
        get_primes(url)


def get_all_primes_thread(links: list[str]):
    with ThreadPoolExecutor(max_workers=80) as executor:
        try:
            executor.map(get_primes, links)
        except Exception as e:
            print(e)

    return links


def get_the_links():
    datasets = ["domains_1.csv", "domains_2.csv", ]
    urls = []
    for dataset in datasets:
        urls = pd.read_csv(dataset, header=None).to_numpy().flatten()

    # print(f'{len(urls)} {urls=}')
    # start = time.perf_counter()
    # get_all_primes(urls)
    # delta = time.perf_counter() - start
    #
    # print(f'{len(global_links)=}, {delta:.10f}')

    start = time.perf_counter()
    get_all_primes_thread(urls)
    delta = time.perf_counter() - start

    print(f'{len(global_links)=}, {delta:.10f}')
    # print(f'{global_links=}')


def main():
    # datasets = ["domains_1.csv", "domains_2.csv",]
    # for dataset in datasets:
    #     with open(dataset, 'w') as json_config:
    #         for i in range(80):
    #             json_config.write(f'https://prime-numbers.info/list/primes-page-{i}\n')

    get_the_links()


if __name__ == '__main__':
    main()
