"""
    Dr. Jones found a mysterious temple deep in the jungle. On the entrance are symbols
    representing different variables: x, y, z.
    To open door, he must assign values to each variable so their product equals 30.
    Help Indy determine variable values!
        x = ?
        y = ??
       zZ = ???
    # Bonus: What are all possible combinations of x, y, z that solve this puzzle?
    PYTHON101 Scrimba.com/learn/python
"""
import logging.config
import math
import time
from itertools import combinations, product
from typing import Collection, Callable

logging.config.fileConfig('logger.cfg', disable_existing_loggers=False)
logger = logging.getLogger("indiana_jones")


# Generators

def get_multiples_bruteforce_all(target: int) -> Collection[int]:
    for x in range(1, target + 1):
        for y in range(1, target + 1):
            for z in range(1, target + 1):
                if x * y * z == target:
                    yield x, y, z


def get_multiples_bruteforce_all_optimized(target: int) -> Collection[int]:
    for x in range(1, target + 1):
        if target % x == 0:
            for y in range(1, int(target / x) + 1):
                if (target / (x * y)).is_integer():
                    yield x, y, int(target / (x * y))


def get_multiples_bruteforce_unique(target: int) -> Collection[int]:
    for x in range(1, target + 1):
        for y in range(x + 1, target + 1):
            for z in range(y + 1, target + 1):
                if x * y * z == target:
                    yield x, y, z


def get_multiples_bruteforce_unique_optimized(target: int) -> Collection[int]:
    for x in range(1, int(target ** 0.5) + 1):
        if target % x == 0:
            for y in range(x + 1, int(target / x) + 1):
                z = target / (x * y)
                if z.is_integer() and z > y:
                    yield x, y, int(z)


def get_factors(target: int) -> Collection[int]:
    factors = ()
    for divisor in range(1, math.isqrt(target) + 1):
        result, remainder = divmod(target, divisor)
        if remainder == 0:
            factors += (divisor, result)
    return factors


def get_multiples_optimized_all(target: int) -> Collection[tuple[int]]:
    for possibles in product(*(get_factors(target),) * 3, ):
        if math.prod(possibles) == target:
            yield possibles


def get_multiples_optimized_unique(target: int) -> Collection[tuple[int]]:
    for possibles in combinations(get_factors(target), 3):
        if math.prod(possibles) == target:
            yield possibles


# Generic Performance comparison test:

def do_print(results: dict):
    for key, value in results.items():
        logger.info(f"\t{key:<50} duration: {value['duration']:.8f} | result: {value['value']}")


def do_test(target_value: int, strategies: dict, retrieve_method: Callable):
    logger.info(
        f"{'=' * 30} Using Callable `{retrieve_method.__name__}()` for target value `{target_value}` {'=' * 30}")
    for strategy in strategies:
        logger.info(f"Applying strategy: `{strategy}` for {target_value = }:")
        results = {}
        for method in strategies[strategy]:
            start = time.perf_counter()
            try:
                execution_result = retrieve_method(method(target_value))
            except StopIteration:
                execution_result = [None]

            results.update({method.__name__: {'value': execution_result,
                                              'duration': time.perf_counter() - start}})

        do_print(results)


def do_test_get_first(target_value: int, strategies: dict):
    do_test(target_value, strategies, next)


def do_test_get_all_results(target_value, strategies: dict):
    do_test(target_value, strategies, list)


if __name__ == '__main__':
    target_values = (10, 11, 20, 30)
    strategies = {'ALL_COMBINATIONS': (
        get_multiples_bruteforce_all,
        get_multiples_bruteforce_all_optimized,
        get_multiples_optimized_all),
        'UNIQUE_COMBINATIONS': (
            get_multiples_bruteforce_unique,
            get_multiples_bruteforce_unique_optimized,
            get_multiples_optimized_unique)}

    for value in target_values:
        logger.info(f"Value `{value}` factors: {sorted(get_factors(value))}")
        do_test_get_first(value, strategies)
        do_test_get_all_results(value, strategies)
