from collections import deque
from string import ascii_lowercase as abc
from typing import Collection

import numpy as numpy


def rotate(offset: int, values: Collection):
    return values[(offset * 2) % len(values):] + values[:(offset * 2) % len(values)]


letters = deque(abc)

two_dim_list = [list(letters) for _ in range(len(letters)) if not letters.rotate(-2)]

print(*two_dim_list, sep='\n')

