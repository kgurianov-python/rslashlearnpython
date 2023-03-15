import numpy as np
import pandas as pd

arr = [None] * 5
print(*arr)

df = pd.DataFrame({'A': [(240, 'v'), (240, 'v'), (50.1, 'hz'), (50.1, 'hz'), (50.1, 'mhz'), (50.1,)],
                   'B': [(240, 'v'), (240, 'v'), (50.1, 'hz'), (50.1, 'hz'), (50.1, 'mhz'), (50.1,)],
                   'C': [(240, 'v'), *arr],
                   'D': [(5000,), *arr]})

for column in df:
    df[[f"{column} values", f"{column} denominations"]] = pd.DataFrame(
        df[column].apply(lambda x: (x[0], None) if ((x is not None) and (len(x) == 1)) else x).tolist()).fillna(value=np.nan)

pd.set_option('display.max_columns', None)
print(df)
# df[['A values', 'A denominations']] = pd.DataFrame(df['A'].tolist())
# print(df)
# df[['B values', 'B denominations']] = pd.DataFrame(df['B'].tolist())
# print(df)
# df[['C values', 'C denominations']] = pd.DataFrame(df['C'].tolist())
# print(df)
# df[['D values', 'D denominations']] = pd.DataFrame(df['D'].apply(lambda x: (x[0],0) if ((x is not None) and (len(x) == 1)) else x).tolist())
# print(df)

#
# df2 = pd.DataFrame(df['A'].tolist(), columns=['A values', 'A denominations'])
#
# print(df2)


