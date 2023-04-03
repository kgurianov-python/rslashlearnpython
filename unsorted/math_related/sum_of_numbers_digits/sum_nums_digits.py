"""
https://www.youtube.com/watch?v=wamTGA2R68s&ab_channel=MindYourDecisions

What is the sum of all 5 digit numbers formed from 1, 2, 3, 4, 5 without repetition? This is an old Amazon interview
question, and versions of it also have been asked in exams.
"""
import copy
import time
from functools import reduce
from itertools import permutations
from typing import Iterable, Collection

from utils_local.timeitt import timeitt


@timeitt(10)
def bruteforce_impl(digits: Collection[int]) -> int:
    """
    Create a list or permutations, convert tules of digits to a number and sum it up
    :param digits: a collection of digits
    :type digits: Iterable
    :return: the sum mof numbers composed of digits
    :rtype: int
    """
    all_permutations = permutations(digits, len(digits))

    def f(x): return sum(val * 10 ** (len(x) - 1 - idx) for idx, val in enumerate(x))

    all_numbers = map(f, all_permutations)
    return sum(all_numbers)


@timeitt(10)
def math_impl(digits: Iterable) -> int:
    """
    for each number in the list:
    sum(number) = num*10^4*4! + num*10^3*4! + num*10^2*4! + num*10^1*4! + num*10^1*4!
        -> num * (10^4 + 10^3 + 10^2 + 10^1 + 10^0) * 4!

    for the entire list = sum(digits) * (10^len(digits-1) + ...+10^0) * (lendigits)!
    :param digits: a collection of digits
    :type digits: Iterable
    :return: the sum mof numbers composed of digits
    :rtype: int
    """

    num_digits =len(digits)
    tens = sum(10 ** (num_digits - idx) for idx in range(1, num_digits + 1))
    fact = reduce(lambda x, y: x * y, range(1, len(digits)), 1)
    # print(n_exp"{tens =}")
    # print(n_exp"{fact =}")

    return sum(digits) * tens * fact


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    test = [1, 2, 3, 4, 5]

    bruteforce_res = bruteforce_impl(test)
    print(f"Bruteforce: {bruteforce_res}")

    math_res = math_impl(test)
    print(f"Math based: {math_res}")
