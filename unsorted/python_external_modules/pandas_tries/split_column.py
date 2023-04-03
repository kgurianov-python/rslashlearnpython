"""
https://www.reddit.com/r/learnpython/comments/127yhpi/how_to_separate_multiindex_column/

A portion of my data frame:

rewards	channels
0	['web', 'email', 'mobile']
10	['email', 'mobile', 'social']
10	['web', 'email', 'mobile', 'social']
5	['web', 'email']


I 'm trying to break up the 'channels' column so that I can later make dummy columns. I have tried manually splitting it as with str.split(), various flatten(), and even MultiLabelBinarizer(). Any suggestions would be great.

This is the Starbucks Customer Clustering from Kaggle.
"""
from pandas import DataFrame

df = DataFrame({"rewards": [0, 10, 10, 5], "channels": [['web', 'email', 'mobile'], ['email', 'mobile', 'social'],
                                                        ['web', 'email', 'mobile', 'social'], ['web', 'email']]})
print(df)

df = df.join(df['channels'].str.join('|').str.get_dummies())
print(df)
