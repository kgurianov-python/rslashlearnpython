import logging

import numpy as np
import pandas as pd

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)


def pivot(frame: pd.DataFrame):
    rows, cols = frame.shape
    data = {
        "value": frame.to_numpy().ravel("F"),
        "series": np.asarray(frame.columns).repeat(rows),
        "time": np.tile(np.asarray(frame.index), cols),
    }
    print(np.asarray(frame.columns).repeat(rows))
    return pd.DataFrame(data, columns=["series", "time", "value"]).set_index(['series', 'time'])


with open('data.csv', 'r') as f:
    data = pd.read_csv(f, index_col=0)

pivoted = pivot(data)
print(pivoted)

with open('export.csv', 'w') as wf:
    pivoted.to_csv(wf, lineterminator='\n')

