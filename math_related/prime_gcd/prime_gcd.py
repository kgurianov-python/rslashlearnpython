"""
https://www.reddit.com/r/learnpython/comments/11sw0g9/need_help_getting_gcd_from_a_list_of_prime/
ur instructor told us to get prime factors from two inputs X and Y. Then he told us

"Using the lists of prime factors, create a program that would print the Greatest Common Divisor (GCD)

GCD(x_factor,y_factor)". Any help in solving this?
"""
from collections import defaultdict, Counter
from adv_python.decors import timeitt


def get_prime_factors(value: int) -> list[int]:
    result = []
    candidate = 2
    while value % candidate == 0:
        result.append(candidate)
        value //= candidate

    candidate = 3
    while candidate ** 2 <= value:
        quotient, remainder = divmod(value, candidate)
        if not remainder:
            result.append(candidate)
            value = quotient
        else:
            candidate += 2

    if value != 1:
        result.append(value)

    return result


def list_to_dict_counter(value: list[int]) -> dict[int:int]:
    return Counter(value)

@timeitt
def get_gcd(left: list[int], right: list[int]) -> int:
    result = 1
    counter_left = list_to_dict_counter(left)
    counter_right = list_to_dict_counter(right)
    merged_dict = {k: min(counter_left[k], counter_right[k]) for k in counter_left.keys() & counter_right.keys()}
    for key, value in merged_dict.items():
        result *= key ** value

    return result


if __name__ == '__main__':
    left_value = 48
    right_value = 180
    print(f"The GCD for {left_value} and {right_value} is: {get_gcd(get_prime_factors(left_value), get_prime_factors(right_value))}")
