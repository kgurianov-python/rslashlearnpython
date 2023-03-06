import requests
from bs4 import BeautifulSoup, Tag
import re

BASE_URL = "https://www.ssga.com/us/en/intermediary/etfs/funds/the-communication-services-select-sector-spdr-fund-xlc"
HEADER = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def find_tag_by_inner_text(soup: Tag, title: str, target_tag_name: str = 'section') -> Tag:
    reg_any = '.*'

    # searching for test inside tag
    # element = soup.find(string=re.compile(f'{reg_any}{title}{reg_any}'))
    element = soup.select_one("h2", string=re.compile(f'{reg_any}{title}{reg_any}'))

    print(f"{element.name=}")
    while (element is not None) and (element.name != target_tag_name):
        element = element.parent

    return element


def main():
    resp = requests.get(BASE_URL, headers=HEADER)

    soup = BeautifulSoup(resp.content, 'html.parser')

    section_name = 'Index Characteristics'
    value_name = 'Price/Earnings'

    # we want to locate the parent element with tag <section/> and do search from there
    index_chars_section = find_tag_by_inner_text(soup, section_name)

    # we want to locate the <tr/> parent tag which contains our data
    p_e_table_row = find_tag_by_inner_text(index_chars_section, value_name, 'tr')

    p_e_value = p_e_table_row.find('td', class_='data').text

    print(f'\'{value_name}\' value from section \"{section_name}\" is: {p_e_value}')


if __name__ == '__main__':
    main()
