import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.tradingview.com/symbols/FX-NAS100/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_open = soup.findAll('div', {"class":"js-symbol-open"})

    print(f'{data_open=}')


if __name__ == '__main__':
    main()
