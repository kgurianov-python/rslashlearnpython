from enum import Enum
from typing import Any

from unsorted.python_data_types.python_collections import itertools_tries


class Operation(Enum):
    ADD = '+'
    MULTIPLY = '*'
    DIVIDE = '/'
    SUBTRACT = '-'


def add(left: int, right: int) -> Any:
    return left + right


def calculate(operation: Operation, left: int, right: int) -> Any:
    expr = f'{left}{operation.value}{right}'
    print(f'{expr=}')
    return eval(expr)


def two_args(arg1, arg2):
    return f"{arg1}, {arg2}"


values = [(1, 2),
          (3, 4),
          (5, 6),
          (7, 8)]

arguments = {"one": ["one", "two", "three"],
             "two": ["four", "five"],
             "three": ["six", "seven"]}


def main():
    # res = itertools.starmap(add, values)
    # print(f'{list(res)}')
    #
    # res = itertools.starmap(partial(calculate, Operation.ADD), values)
    # print(f'{list(res)}')

    list_of_args = [item for item in arguments.items()]
    for item in list_of_args:
        print(type(item))

    print(*list_of_args, sep="\n")

    strings = list(itertools_tries.starmap(two_args, list_of_args))

    print(strings)



if __name__ == '__main__':
    main()
