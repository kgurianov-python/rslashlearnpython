"""
A mathematician tells a census taker he has 3 children.
The product of their ages is 72 and the sum of their ages is the house number.

The census taker tries to figure it out but explains he still does not know.

The mathematician says, "Of course not. I forgot to tell you my oldest child loves
chocolate chip cookies."

Now the census taker figures it out. What are the ages of the children?

https://www.youtube.com/watch?v=XCUD-4J2aZY&ab_channel=MindYourDecisions
"""
from collections import Counter
from functools import reduce
from itertools import product

CHILDREN = 3
TARGET = 72


def get_divisors_cobinations(target: int, count: int = CHILDREN, divisors: list[int] = None,
                             current_combination: list[int] = None,
                             combinations: set[tuple[int]] = None) -> set[tuple[int]]:
    if divisors is None:
        divisors = sorted(get_divisors_from_factors(target))

    if current_combination is None:
        current_combination = []

    if combinations is None:
        combinations = []

    if len(current_combination) >= count:
        if target == 1:
            combinations.append(tuple(current_combination))
        return

    for idx, divisor in enumerate(divisors):
        new_target, remainder = divmod(target, divisor)
        if remainder:
            continue

        current_combination.append(divisor)
        get_divisors_cobinations(new_target, count, divisors[idx:], current_combination, combinations)
        current_combination.pop()

    return combinations


def get_divisors_from_factors(target):
    factors = []
    factor = 2
    while target > 1:
        res, remainder = divmod(target, factor)
        if remainder == 0:
            target = res
            factors.append(factor)
        else:
            factor += 1

    powered = ([factor ** power for power in range(powers + 1)] for factor, powers in
               Counter(factors).items())
    return list(map(lambda x: reduce(lambda a, b: a * b, x), product(*powered)))


if __name__ == '__main__':
    print(get_divisors_from_factors(72))

    print(*sorted(get_divisors_cobinations(TARGET, CHILDREN)), sep="\n")
