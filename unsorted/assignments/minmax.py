import time
from math import inf
from typing import Collection, Callable


def minmax_pythonic(vals: Collection) -> int:
    val_min = vals[0]
    val_max = vals[0]
    sum = 0
    for val in vals:
        val_min = min(val, val_min)
        val_max = max(val, val_max)
        sum += val
    return sum - (val_max + val_min)


def minmax_sum(vals: Collection) -> int:
    return sum(vals) - (min(vals) + max(vals))


def minmax_list_op(listacle):
    addt = 0
    listacle.remove(max(listacle))
    listacle.remove(min(listacle))
    for num in listacle:
        addt += num
    return addt


def minmax_sorted_sliced(vals: Collection) -> int:
    return sum(sorted(vals)[1: -1])


def time_it(f: Callable, vals: Collection) -> int:
    start = time.perf_counter()
    f(vals)
    return time.perf_counter() - start


test = list(range(1_000_000, 0, -1))

functions = [minmax_pythonic, minmax_sum, minmax_list_op, minmax_sorted_sliced]
for function in functions:
    print(f"{function.__name__:<20} time: {time_it(function, test):.8f}")
