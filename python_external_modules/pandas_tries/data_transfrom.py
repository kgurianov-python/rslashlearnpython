import ast
import itertools
import re
import string

import numpy as np
import pandas as pd
from ast import literal_eval as make_tuple

pd.set_option('display.max_columns', None)

df = pd.read_csv('data_transform.csv', sep=';')
# print(df)
df['Kol2'] = df['Kol1'].str.lower().str.replace(',', '.')
pattern = r'(\d+(?:.\d+)?)(?:\s*(v|hz|mhz))?'
print(df)
seq = df['Kol2'].apply(lambda x: re.findall(pattern, x)).tolist()
print(seq)
seq = np.array(seq).T
print(seq)
# df_new = pd.DataFrame(seq,['A','B','C','D'])
# print(df_new)

#
#
# for column in df_new:
#     print(f"{column} :{df_new[column].tolist()}")
#     df_new[[f"{column} values", f"{column} denominations"]] = pd.DataFrame(
#         df_new[column].apply(lambda x: (x[0], None) if ((x is not None) and (len(x) == 1)) else x).tolist()).fillna(value=np.nan)
#
# print(df_new)
