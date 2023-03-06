import logging
from collections import Counter
from itertools import product
from math import isqrt

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')
# logger.setLevel(logging.DEBUG)


def get_prime_factors(num):
    factor = 2
    while factor ** 2 <= num:
        if num % factor == 0:
            num //= factor
            yield factor
        else:
            factor += 1
    if num > 1:
        yield num


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(num):
    prime_factors = get_prime_factors(num)
    primes_factors_counts = Counter(prime_factors)
    powers = [[factor ** power for power in range(count + 1)] for factor, count in primes_factors_counts.items()]

    for prime_factor_powers in product(*powers):
        yield prod(prime_factor_powers)


def is_perfect(num):
    if num <=0:
        return False
    return sum(list(get_divisors(num))[:-1]) == num


def is_pronic(num: int) -> bool:
    """

    :param num: value to test
    :type num: int
    :return: result of pronic number validation
    :rtype: bool
    """
    if num % 2:
        return False
    right = isqrt(num) + 1
    while (val := (right - 1) * right) >= num:
        logger.debug(val)
        if val == num:
            return True
        right -= 1
    return False


def main():
    test_bound = 1000
    pronic_numbers = [i for i in range(0, test_bound) if is_pronic(i)]
    perfect_numbers = [i for i in range(0, test_bound) if is_perfect(i)]
    print(list(get_divisors(6)))

    print(pronic_numbers)
    print(perfect_numbers)


if __name__ == '__main__':
    main()
