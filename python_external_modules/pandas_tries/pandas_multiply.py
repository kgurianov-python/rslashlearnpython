import itertools
import pandas as pd

Column1 = [123456789]

Column2 = [ "5502371844", "8597976554", "7038388199", "-1524069284", "7132920995", "8992837415", "6710764072", "6729819114", "5933538167", "7123342475", "5502309656"]

df = pd.DataFrame(itertools.product(Column1, Column2), columns=['Column1', 'Column2'])

print(df)
df.info()