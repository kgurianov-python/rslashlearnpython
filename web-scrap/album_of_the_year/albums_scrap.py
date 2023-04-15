"""
https://www.reddit.com/r/learnpython/comments/12llc10/need_help_with_python_webscraping/

I would like to preface this by saying that I am very much a beginner in web-scraping, and therefore may just be completely lost, and ignorant about what I am going to talk about :)

So, I am currently trying to scrape the following website: https://www.albumoftheyear.org

I have been running into A LOT of forbidden issues for this website, and I am not entirely sure why too. The weird thing though, and where I ultimately need some help, is that whenever I run a same request through both urllib.request, and the requests library, I get two completely different results.

With urllib.request, I always get 200 status codes, and can parse through the entire website without any issues, however with the requests library (and also with Postman & Go Colly) I keep getting 403 forbidden, even when using the exact same request as the successful one.

Here is the code that showcases the two requests, with the first one having a successful response, while the second always failing :(

from urllib.request import Request, urlopen
import requests

headers = {
 "User-Agent": "Mozilla/6.0",
}

# First request using urllib.request -> Success 200
test = Request('https://www.albumoftheyear.org', headers=headers)
res = urlopen(test)
print(res.status)

# Second request using requests -> Forbidden 403
req = requests.get('https://www.albumoftheyear.org', headers=headers)
print(req.status_code)
I would like to use the requests library to continue this webscraping project, however I can't seem to get it working. Any insights on how to fix this, or why this is happening would be very much appreciated!
"""
import logging
import requests
from bs4 import BeautifulSoup

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')

headers = {
    "User-agent": "i-do-not-care"
}

req = requests.get('https://www.albumoftheyear.org', headers=headers)
req.raise_for_status()

logger.info(f"{req.status_code = }")
soup = BeautifulSoup(req.content, "html.parser", from_encoding="utf_8")
content_container = soup.find('div', {"id": "centerContent"})
albums = content_container.find_all('div', {"class": "albumBlock"})
for album in albums[:5]:
    title = album.find("div", {"class": "artistTitle"}).text
    ratings_tags = album.find("div", {"class": "ratingRowContainer"}).find_all('div', {"class": "ratingRow"})
    ratings = {rating.find('div', {"class": "ratingText"}).text: rating.find('div', {"class": "ratingBlock"}).text for
               rating in ratings_tags}
    logger.info(f"{title}, {ratings}")
