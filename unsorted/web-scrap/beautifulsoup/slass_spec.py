import requests
from bs4 import BeautifulSoup, Tag
import re

BASE_URL = "https://ofm.wa.gov/state-human-resources/compensation-job-classes/ClassifiedJobListing/Specifications/10"
HEADER = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def find_tag_by_inner_text(soup: Tag, title: str) -> Tag:
    reg_any = '.*'
    # searching for text inside tag
    element = soup.find(string=re.compile(f'{reg_any}{title}{reg_any}'))
    # element = soup.select_one(string=re.compile(f'{reg_any}{title}{reg_any}'))
        # find(string=re.compile(f'{reg_any}{title}{reg_any}'))

    return element


def main():
    resp = requests.get(BASE_URL, headers=HEADER)
    soup = BeautifulSoup(resp.content, 'html.parser')

    section_name = 'Desirable Qualifications'

    section = find_tag_by_inner_text(soup, section_name)

    print(section.next_element.text)


if __name__ == '__main__':
    main()
