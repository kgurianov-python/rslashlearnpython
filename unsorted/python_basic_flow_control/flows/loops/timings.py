import os
import random
import sys
import time
import logging
from collections import defaultdict
from typing import Callable

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('for_loop_timer_logger')


def do_for_len(vals: list[int]) -> None:
    for i in range(len(vals)):
        print(f'{i}, {vals[i]}')


def do_for_enumerate(vals: list[int]) -> None:
    for i, val in enumerate(vals):
        print(f'{i}, {val}')


def main():
    functions: [Callable] = [do_for_enumerate, do_for_len]
    max_array_size: int = 10000000 
    max_runs: int = 10
    vals: list[int] = list(range(max_array_size))
    tmp = sys.stdout

    stats: {Callable: {str: int}} = defaultdict(lambda: defaultdict(lambda: 0))

    logger.info(f'Starting 10 runs for each func')
    try:
        f = open(os.devnull, 'w')
        while functions:
            func = random.choice(functions)
            if stats[func]['runs'] >= max_runs:
                functions.remove(func)
                continue

            sys.stdout = f
            start = time.perf_counter()
            func(vals)
            delta = time.perf_counter() - start
            sys.stdout = tmp

            logger.info(f"Run {func.__name__:20}, {stats[func]['runs'] + 1}/{max_runs}, {delta=}")
            stats[func]['runs'] += 1
            stats[func]['sum'] += delta
    except Exception as e:
        logger.error(e)
    finally:
        sys.stdout = tmp
        for func in stats:
            logging.info(f"Iterations {func.__name__}: {max_array_size:,}, ETA: {stats[func]['sum'] / stats[func]['runs']:.8f}")


if __name__ == '__main__':
    main()
