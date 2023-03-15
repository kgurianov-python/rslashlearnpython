"""
https://www.reddit.com/r/learnpython/comments/11pyvpq/trying_to_scrape_allmusic_and_code_only_returns/
"""

from requests_html import HTMLSession

url = 'https://www.allmusic.com/genres'

session = HTMLSession()
r = session.get(url)
r.html.render()

genres = r.html.find('.genre')

for genre in genres:
    print(genre.find('h2', first=True).text)
