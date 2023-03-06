import requests
from bs4 import BeautifulSoup

header = {'Accept-Language': 'en-US',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


### Header might need to be changed for it to work appropriately. This works for me

def main():
    resp = requests.get('https://www.imdb.com/name/nm0034023', headers=header)
    print(f'{resp=}')

    soup = BeautifulSoup(resp.content, 'html.parser')

    # Finds the tag that delimits the jobs
    movie_list = soup.find(class_='ipc-accordion__item__content')
    print(f'{movie_list=}')

    # Makes a list of each individual job
    movies = movie_list.find_all(class_='ipc-metadata-list-summary-item')

    print(f'{len(movies)=}')


if __name__ == '__main__':
    main()
