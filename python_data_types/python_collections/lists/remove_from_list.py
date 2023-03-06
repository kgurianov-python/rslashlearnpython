import math
import time
from tqdm import tqdm
from typing import Callable


def remove_element_comprehension(nums: list[int], val: int):
    return [x for x in nums if x != val]


def remove_element_while(nums: list[int], val: int):
    while val in nums:
        nums.remove(val)
    return nums


def remove_element_cached_count(nums: list[int], val: int):
    count_vals = nums.count(val)
    for _ in range(count_vals):
        nums.remove(val)
    return nums


def do_tests(f: Callable, list_size: int, val: int, runs: int = 10) -> (str, float):
    results = []
    for _ in tqdm(range(runs), desc=f"{f.__name__:30} Array Size:\t{list_size:,}"):
        test_list = [val] * (list_size - 1) + [2]
        # print(len(test_list))
        start = time.perf_counter()
        res = f(test_list, val)
        results.append(time.perf_counter() - start)
    return sum(results) / len(results)


LIST_SIZE = 100000 * 2


def main():
    val = 3

    funcs = (remove_element_comprehension,
             remove_element_cached_count,
             remove_element_while)

    list_sizes = (10, 100, 1000, 10000, 100000, 200000)
    for list_size in list_sizes:
        print("\n")
        for func in funcs:
            duration = do_tests(func, list_size, val)
            # results.append(f"Function: {name:30} Array size: {LIST_SIZE:10} Duration: {duration:.8f}")
            time.sleep(1)
            print(f"Average duration: {duration:.8f} seconds")
            time.sleep(1)

    # print(*results, sep='\n')


if __name__ == '__main__':
    main()
