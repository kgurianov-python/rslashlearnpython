import copy
import logging
from itertools import islice
from typing import Callable
import time

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
ARR_SIZE = 10

array = [[1, 2, 3, 4, 5, 6],
         [4, 5, 6, 7, 2, 8],
         [7, 8, 9, 0, 1, 4],
         [0, 1, 2, 3, 1, 2],
         [1, 1, 1, 4, 5, 5],
         [1, 2, 3, 4, 5, 5]]

template = list(range(10))
array = [[template[(i + 3 * k) % len(template)] for i in range(ARR_SIZE)] for k in range(ARR_SIZE)]


# array = [[752, 899], [535, 963]]

def timeitt(runs: int = 100):
    def decorator(f):
        def wrapper(*args, **kwargs):
            stats = []
            for _ in range(runs):
                data = copy.deepcopy(args[0])
                start = time.perf_counter()
                result = f(data, *args[1:], **kwargs)
                end = time.perf_counter()
                logger.debug(result)
                stats.append(end - start)
            logger.info(f"{f.__name__} | {runs} runs | AVG run time: {sum(stats) / runs:.8f}")
            return result
        return wrapper
    return decorator


def transpose_left(arr: list[list[int]] = None) -> list[list[int]]:
    if not arr:
        return []
    result = [[row[idx] for row in arr] for idx in range(len(arr[0]) - 1, -1, -1)]
    return result


def transpose_left_zip(arr: list[list[int]] = None) -> list[list[int]]:
    result = list(zip(*arr))
    result.reverse()
    return result


def transpose_left_shift(arr: list[list[int]] = None, shift: int = 0) -> list[list[int]]:
    result = [[row[idx] for row in islice(arr, shift, None)] for idx in
              range(len(arr[0]) - 1, -1, -1)]
    return result


def transpose_left_shift_zip(arr: list[list[int]] = None, shift: int = 0) -> list[list[int]]:
    result = list(zip(*islice(arr, shift, None)))
    result.reverse()
    return result


@timeitt()
def snail_pop(arr: list[list[int]]) -> [int]:
    # result = arr.pop(0)
    result = []
    while arr:
        result.extend(arr.pop(0))
        arr = transpose_left(arr)
        # result.extend(arr.pop(0))
    return result


@timeitt()
def snail_pop_zip(arr: list[list[int]]) -> [int]:
    result = []
    while arr:
        result.extend(arr.pop(0))
        arr = transpose_left_zip(arr)
    return result


@timeitt()
def snail_shift(arr: list[list[int]]) -> [int]:
    result = []
    while arr:
        result.extend(arr[0])
        arr = transpose_left_shift(arr, 1)
    return result


@timeitt()
def snail_shift_zip(arr: list[list[int]]) -> [int]:
    result = []
    while arr:
        result.extend(arr[0])
        arr = transpose_left_shift_zip(arr, 1)
    return result


if __name__ == '__main__':
    tests = [snail_pop, snail_pop_zip, snail_shift, snail_shift_zip]
    for test in tests:
        logger.info(test(array))
