import logging
import requests as requests
from bs4 import BeautifulSoup

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('KCL SCrapper')

base_url = 'https://www.kcl.ac.uk'


def get_bio_links(url: str) -> dict[str, str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    people_contaner = soup.find('section', {"class": "block--people-listing"})
    links = people_contaner.find_all('a')
    profile_links: dict[str, str] = {}
    for link in links:
        profile_links[link['title']] = link['href']

    return profile_links
    raise V

def get_email(url: str) -> str:
    logger.debug(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    email = soup.find('article').find('ul', {"class": "list--block"}).find('a')['href']
    return email


def main():
    num_pages = 1
    links: dict[str, str] = {}
    for page in range(1, num_pages + 1):
        url = f'{base_url}/business/people?page={page}'
        get_bio_links(url)
        links.update(get_bio_links(url))

    print(links)

    emails = {}
    for key, val in links.items():
        url = f'{base_url}{val}'
        emails[key] = get_email(url)

    print(emails)


if __name__ == '__main__':
    main()
