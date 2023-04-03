from typing import Collection, Iterable, Sequence


def variable_args(args):
    if not isinstance(args, list):
        args = [args]

    for arg in args:
        print(arg)


def variable_args_unpack(*args):
    for arg in args:
        print(arg)


variable_args_unpack("a single argument")
arg_list = ("tuple argument 1", "tuple argument 2", "tuple argument 3")
variable_args_unpack(*arg_list)
arg_list = ["list argument 1", "list argument 2", "list argument 3"]
variable_args_unpack(*arg_list)

with open("food_list.txt", "a") as file:
