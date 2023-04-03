from itertools import pairwise, chain
from typing import TypeVar

T = TypeVar("T")


def sel_reverse(items: list[T], width: int) -> list[T]:
    if width <= 0:
        return items
    result = [item for sublist in [list(reversed(items[x:y])) for x, y in pairwise(range(0, len(items) + width, width))]
              for item in sublist]
    return result


def sel_reverse_nested(items: list[T], width: int) -> list[T]:
    result = []
    for x, y in pairwise(range(0, len(items) + width, width)):
        result.extend(reversed(items[x:y]))
    return result


def sel_reverse_comp(items: list[T], width: int) -> list[T]:
    lists = (list(reversed(items[x:y])) for x, y in pairwise(range(0, len(items) + width, width)))
    return list(chain.from_iterable(lists))


print(sel_reverse_comp([1, 2, 3, 4, 5, 6], 2))
print(sel_reverse_comp([2, 4, 6, 8, 10, 12, 14, 16], 3))
print(sel_reverse_comp([2, 4, 6, 8, 10, 12, 14, 16], 4))
print(sel_reverse_comp([2, 4, 6, 8, 10, 12, 14, 16, 18, 21], 5))
print(sel_reverse_comp([2, 4, 6, 8, 10, 12, 14, 16, 18, 21, 25], 6))
print(sel_reverse_comp([2, 4, 6, 8, 10, 12, 14, 16, 18, 21, 25, 27], 7))


print([1, 2, 3, 4, 5, 6][5:3:-1])
print([1, 2, 3, 4, 5, 6][3:1:-1])
print([1, 2, 3, 4, 5, 6][1::-1])