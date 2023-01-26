import requests
from bs4 import BeautifulSoup

header = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX 10.15)'}


### Header might need to be changed for it to work appropriately. This works for me

def main():
    resp = requests.get('https://www.imdb.com/name/nm0034023', headers=header)

    soup = BeautifulSoup(resp.content, 'html.parser')

    # Finds the tag that delimits the jobs
    movie_list = soup.find(class_='ipc-accordion__item__content')
    print(f'{movie_list=}')

    # Makes a list of each individual job
    movies = movie_list.find_all(class_='ipc_metadata-list-summary-item__c')

    print(f'{movies=}')


if __name__ == '__main__':
    main()
