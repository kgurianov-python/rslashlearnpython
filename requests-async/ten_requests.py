"""
https://www.reddit.com/r/learnpython/comments/12h0iuc/comment/jfoae1h/?utm_source=share&utm_medium=web2x&context=3

I want to send 10 HTTP POST requests to different URLs, at the same time. Something like

request1 = requests.post(URL, data = payload)
...
request10 = requests.post(URL10, data = payload10)
All at the same time.

Could anyone guide me on how to do this?

"""
import asyncio
import itertools

import aiohttp
from bs4 import BeautifulSoup
import logging

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')

URLS = ['https://prime-numbers.info/list/primes',
        "https://prime-numbers.info/list/primes-page-1",
        "https://prime-numbers.info/list/primes-page-2",
        "https://prime-numbers.info/list/primes-page-3",
        "https://prime-numbers.info/list/primes-page-4",
        "https://prime-numbers.info/list/primes-page-5",
        "https://prime-numbers.info/list/primes-page-6",
        "https://prime-numbers.info/list/primes-page-7",
        "https://prime-numbers.info/list/primes-page-8",
        "https://prime-numbers.info/list/primes-page-9",
        ]

def parse_primes(html: bytes) -> (str, [str]):
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    container = soup.find('div', {"id": "main"})
    title = container.find('h1').text
    primes_container = container.select_one('#main > div.row > div > div:nth-child(9)')

    primes = [a.text for a in primes_container.find_all('a')]
    return title, primes


async def get_url(url, session):
    logger.info(f"Retrieving {url}")
    resp = await session.get(url)
    logger.info(f"Got response")
    return await resp.read()


async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*map(get_url, URLS, itertools.repeat(session)))

    for result in results:
        logger.info(parse_primes(result))


if __name__ == '__main__':
    asyncio.run(main())
