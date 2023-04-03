"""
https://www.reddit.com/r/learnpython/comments/120oq1u/webscraping_with_python_pulling_extremely/

I'm trying to build a webscraper that pulls up the most recent UFC event.

I am super new to this, I used chat GPT for pretty well everything I have.
Quickly learning it's not as smart as I thought.

Kinda just want to be pointed in the right direction as to how I can pull the data showing the upcoming events.
The only thing remotely close I can see this data pulling is somehow pulling data of events from 2012 (???)

"""

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://www.tapology.com/fightcenter/promotions/1-ultimate-fighting-championship-ufc"
HEADERS = {'Accept-Language': 'en-US',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def get_span_value_by_class(event: Tag, name: str) -> str | None:
    span_tag = event.find('span', {'class': name})
    if span_tag:
        return span_tag.text.strip()
    return None


def extract_data(event: Tag) -> dict[str:str]:
    return {'event_name': get_span_value_by_class(event, 'name'),
            'event_time': get_span_value_by_class(event, 'datetime'),
            'event_broadcast': get_span_value_by_class(event, 'broadcast'),
            'event_venue': get_span_value_by_class(event, 'venue'),
            'event_location': get_span_value_by_class(event, 'venue-location'),
            'event_region': get_span_value_by_class(event, 'region'),
            'event_billing': get_span_value_by_class(event, 'billing'),
            'event_bout': get_span_value_by_class(event, 'bout')
            }


if __name__ == '__main__':
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all contaner for all events
    events_container = soup.find('div', {'id': 'content'})

    # Locate all events
    events = [extract_data(event) for event in events_container.find_all('section', {'class': 'fcListing'})]

    print(*events, sep='\n')
