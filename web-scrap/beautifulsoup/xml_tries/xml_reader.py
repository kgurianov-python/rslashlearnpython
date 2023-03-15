from bs4 import BeautifulSoup as bs

with open(r'file.xml', 'r', encoding="latin-1") as file:
    contents = file.read()
    soup = bs(contents, features='lxml-xml')
    all_dids = soup.find_all("did")

    for dids in all_dids:
        unitids = dids.find_all('unitid', {'label': 'Digital ID'})
        print(unitids)
