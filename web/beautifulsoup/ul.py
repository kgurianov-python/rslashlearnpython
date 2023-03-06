from bs4 import BeautifulSoup

with open("uls.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    ul_list = soup.find('ul', {"class": "list-unstiled"})
    list_items = ul_list.find_all('li')
    last_item = list_items[-1]
    print(last_item.text)
