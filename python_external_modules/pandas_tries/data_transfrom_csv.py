"""
https://www.reddit.com/r/learnpython/comments/11ou4ux/convert_dataframe_consisting_of_tuples_into/


"""
import numpy as np
import pandas as pd
import re

df = pd.read_csv('teksttall3.csv', sep=';')
df

# change ',' to '.' and make text lower
df['Kol2'] = df['Kol1'].str.lower().str.replace(',', '.')

# find the pattern i want
pattern = r'(\d+(?:.\d+)?)(?:\s*(v|hz|mhz))?'
df['numbers_units'] = df['Kol2'].apply(lambda x: re.findall(pattern, x))

df = df.drop(['Kol1', 'Kol2'], axis=1)
print(df)

# this is the data I wanted to extract from the text rows

# split the list of tuples into seperate columns
df_new = df['numbers_units'].apply(pd.Series)
df_new.columns = ['A', 'B', 'C', 'D']
print(df_new)

# And now I want to split this again into seperate columns.
pd.set_option('display.max_columns', None)
for column in df_new:
    print(f"{column} :{df_new[column].tolist()}")
    df_new[[f"{column} values", f"{column} denominations"]] = pd.DataFrame(
        df_new[column].tolist()).fillna(value=np.nan)

print(df_new)
