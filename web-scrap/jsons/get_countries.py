import pandas as pd
import requests

all_countries = requests.get('https://restcountries.com/v3.1/all').json()
countries_list = [{'name': country['name']['common'], 'continent': country['region']} for country in all_countries]
print(countries_list)
df = pd.DataFrame(countries_list).sort_values('name').reset_index(drop=True)
print(df.head(10))