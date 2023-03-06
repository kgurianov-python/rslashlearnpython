import calendar
import itertools
import os
import shutil
import time
from pathlib import Path
from typing import Callable


def clean(parent_dir):
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)

def timeitt(runs: int = 10, cleanup: Callable = None):
    def decorator(f):
        def wrapper(*args, **kwargs):
            stats = []
            for _ in range(runs):
                cleanup(args[0])
                start = time.perf_counter()
                result = f(*args, **kwargs)
                stats.append(time.perf_counter() - start)

            print(f"{f.__name__} Runs: {runs}; average executions time: {sum(stats) / runs:.8f}")
            return result

        return wrapper

    return decorator


@timeitt(1, clean)
def create_folder_tree(parent_dir, *childdirlists):
    """Takes parent folder string and optional lists of foldernames.
    Adds folders to each previous layer of folders."""

    # Create the parent dir if it does not exist.
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    # Recursively create child directories.
    if childdirlists:
        for child in childdirlists[0]:
            child_dir = os.path.join(parent_dir, child)
            create_folder_tree_starter(child_dir, *childdirlists[1:])


def create_folder_tree_starter(parent_dir, *childdirlists):
    """Takes parent folder string and optional lists of foldernames.
    Adds folders to each previous layer of folders."""

    # Create the parent dir if it does not exist.
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    # Recursively create child directories.
    if childdirlists:
        for child in childdirlists[0]:
            child_dir = os.path.join(parent_dir, child)
            create_folder_tree_starter(child_dir, *childdirlists[1:])


@timeitt(1, clean)
def create_folder_tree_iterative(parent_dir, *args):
    """Takes parent folder string and optional lists of foldernames.
    Adds folders to each previous layer of folders."""
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    base = [parent_dir]
    for subdirs in args:
        base = [os.path.join(*item) for item in itertools.product(base, subdirs)]
        for dir in base:
            if not os.path.exists(dir):
                os.mkdir(dir)


@timeitt(1, clean)
def create_folder_tree_proper_a1brit(parent_dir, *args):
    # paths = [os.path.join(parent_dir, *items) for items in itertools.product(*args)]
    paths = [Path(parent_dir, *items) for items in itertools.product(*args)]
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
        # os.makedirs(path, exist_ok=True)


def main():
    test = ['test2', 'test3', 'test4']
    parent_dir = 'root'
    filetypes = ['text', 'grids', 'images']
    years = [str(year) for year in range(2000, 2023)]
    months = [calendar.month_name[month] for month in range(1, 13)]
    days = [str(day) for day in range(1, 32)]

    create_folder_tree(parent_dir, filetypes, years, months)
    create_folder_tree_iterative(parent_dir, filetypes, years, months)
    create_folder_tree_proper_a1brit(parent_dir, filetypes, years, months)


if __name__ == '__main__':
    main()
